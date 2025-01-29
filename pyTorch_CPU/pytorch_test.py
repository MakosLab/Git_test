import torch

# Check if pyTorch is using CPU 
# It should print False because CUDA works on GPUs only
print(f"Is CUDA available? {torch.cuda.is_available()}")
print(f"Device being used: {torch.device('cpu')}")

# Create your first tensor
x = torch.tensor([1.0, 2.0, 3.0])
print(f"Tensor: {x}")

# Let it do the math 
y = x * 2
print(f"Tensor after multiplication: {y}")

# Print pyTorch version beacuse why not 
print(f"PyTorch Version: {torch.__version__}")
