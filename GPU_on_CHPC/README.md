## 1. Set Up a Conda Environment for PyTorch
      source /share/apps/modulefiles/conda_init.sh 
      conda create --name pytorch_gpu python=3.9 -y
      conda activate pytorch_gpu

## 2. Install PyTorch with CUDA support:

    conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

## 3. Check that PyTorch detects the GPU

      python -c "import torch; print(torch.cuda.is_available())"

If it prints 'True', then PyTorch is ready to use your GPU.

## 4. Submit your job. 

      sbatch run_gpu.sh

## 5. You can verify the GPU Usage

      nvidia-smi
