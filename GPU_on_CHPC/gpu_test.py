import torch

def check_gpu():
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print(f"Using GPU: {torch.cuda.get_device_name(0)}")
    else:
        device = torch.device("cpu")
        print("GPU not available, using CPU.")

    # Allocate a tensor on GPU and perform a simple computation
    x = torch.rand(10000, 10000, device=device)
    y = torch.rand(10000, 10000, device=device)
    z = torch.matmul(x, y)
    
    print(f"Computation complete. Tensor shape: {z.shape}")

if __name__ == "__main__":
    check_gpu()

