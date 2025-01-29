import torch

# Check if PyTorch is using CPU
print(f"Is CUDA available? {torch.cuda.is_available()}")
print(f"Device being used: {torch.device('cpu')}")

# Create a simple tensor
x = torch.tensor([1.0, 2.0, 3.0])
print(f"Tensor: {x}")

# Perform a basic operation
y = x * 2
print(f"Tensor after multiplication: {y}")

# Print PyTorch version
print(f"PyTorch Version: {torch.__version__}")
