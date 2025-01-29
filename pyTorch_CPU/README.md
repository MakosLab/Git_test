## 1. Set Up a conda environment for pyTorch_CPU
      source /share/apps/modulefiles/conda_init.sh 

## 2. Create and activate pyTorch environment
      conda create --name pytorch_cpu python=3.10 -y
      conda activate pytorch_cpu

## 3. Install pyTorch with CUDA support:

      conda install pytorch torchvision torchaudio cpuonly -c pytorch

## 5. Print the pyTorch version

      python -c "import torch; print(torch.__version__)"

If installed correctly, this will print the PyTorch version.

## 5. Run your script 

      python pytorch_cpu_test.py


