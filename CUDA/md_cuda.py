import numpy as np
from numba import cuda
import math

# Simulation parameters
N = 1024         # Number of particles
dim = 3          # 3D simulation
box = 10.0       # Size of the simulation box (assumed cubic)
mass = 1.0       # Mass of each particle
epsilon = 1.0    # Depth of the Lennard-Jones potential well
sigma = 1.0      # Finite distance at which the inter-particle potential is zero
cutoff = 2.5 * sigma  # Cutoff distance for the potential
dt = 0.005       # Time step
nsteps = 1000    # Number of simulation steps

# Initialize positions and velocities
positions = np.random.rand(N, dim).astype(np.float32) * box
velocities = (np.random.rand(N, dim).astype(np.float32) - 0.5) * 0.1
forces = np.zeros((N, dim), dtype=np.float32)

# Transfer data to the GPU
d_positions = cuda.to_device(positions)
d_velocities = cuda.to_device(velocities)
d_forces = cuda.to_device(forces)

threads_per_block = 128
blocks = (N + threads_per_block - 1) // threads_per_block

@cuda.jit
def compute_forces(positions, forces, box, epsilon, sigma, cutoff):
    """
    Compute the Lennard-Jones force on each particle.
    Uses a simple all-pairs approach with periodic boundaries.
    """
    i = cuda.grid(1)
    if i < positions.shape[0]:
        fx = 0.0
        fy = 0.0
        fz = 0.0
        for j in range(positions.shape[0]):
            if i != j:
                # Calculate displacement
                dx = positions[j, 0] - positions[i, 0]
                dy = positions[j, 1] - positions[i, 1]
                dz = positions[j, 2] - positions[i, 2]
                # Apply the minimum image convention
                dx = dx - box * round(dx / box)
                dy = dy - box * round(dy / box)
                dz = dz - box * round(dz / box)
                r2 = dx * dx + dy * dy + dz * dz
                if r2 < cutoff * cutoff and r2 > 1e-12:
                    inv_r2 = 1.0 / r2
                    inv_r6 = inv_r2 * inv_r2 * inv_r2
                    # Compute Lennard-Jones force: F = 24*epsilon/r^2 * inv_r6 * (2*(sigma^6)*inv_r6 - 1)
                    force_scalar = 24.0 * epsilon * inv_r2 * inv_r6 * (2.0 * (sigma ** 6) * inv_r6 - 1.0)
                    fx += force_scalar * dx
                    fy += force_scalar * dy
                    fz += force_scalar * dz
        forces[i, 0] = fx
        forces[i, 1] = fy
        forces[i, 2] = fz

@cuda.jit
def integrate(positions, velocities, forces, mass, dt, box):
    """
    Integrate positions and update velocities (half-step) using a velocity-Verlet scheme.
    """
    i = cuda.grid(1)
    if i < positions.shape[0]:
        # Update velocity (half-step)
        velocities[i, 0] += 0.5 * forces[i, 0] / mass * dt
        velocities[i, 1] += 0.5 * forces[i, 1] / mass * dt
        velocities[i, 2] += 0.5 * forces[i, 2] / mass * dt
        # Update position
        positions[i, 0] += velocities[i, 0] * dt
        positions[i, 1] += velocities[i, 1] * dt
        positions[i, 2] += velocities[i, 2] * dt
        # Apply periodic boundary conditions
        positions[i, 0] = positions[i, 0] % box
        positions[i, 1] = positions[i, 1] % box
        positions[i, 2] = positions[i, 2] % box

@cuda.jit
def finalize_velocity(velocities, forces, mass, dt):
    """
    Finalize the velocity update using the new forces.
    """
    i = cuda.grid(1)
    if i < velocities.shape[0]:
        velocities[i, 0] += 0.5 * forces[i, 0] / mass * dt
        velocities[i, 1] += 0.5 * forces[i, 1] / mass * dt
        velocities[i, 2] += 0.5 * forces[i, 2] / mass * dt

# Main simulation loop
for step in range(nsteps):
    # Compute forces at current positions
    compute_forces[blocks, threads_per_block](d_positions, d_forces, box, epsilon, sigma, cutoff)
    cuda.synchronize()
    
    # Integrate positions and perform half-step velocity update
    integrate[blocks, threads_per_block](d_positions, d_velocities, d_forces, mass, dt, box)
    cuda.synchronize()
    
    # Recompute forces after position update
    compute_forces[blocks, threads_per_block](d_positions, d_forces, box, epsilon, sigma, cutoff)
    cuda.synchronize()
    
    # Finalize velocity update using new forces
    finalize_velocity[blocks, threads_per_block](d_velocities, d_forces, mass, dt)
    cuda.synchronize()
    
    # Optionally, print the position of the first particle every 100 steps
    if step % 100 == 0:
        d_positions.copy_to_host(positions)
        print("Step:", step, "Positions[0]:", positions[0])

print("Simulation complete")

