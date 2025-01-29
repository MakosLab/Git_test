#!/bin/bash
#SBATCH -p gpu
#SBATCH -q gpu
#SBATCH -n 1
#SBATCH -c 12
#SBATCH --mem=45G
#SBATCH --gres=gpu:v100:1
#SBATCH -t 01:00:00  # 1 hour runtime
#SBATCH -o gpu_test.out
#SBATCH -e gpu_test.err

# Load Conda on CHPC and activate your env
source /share/apps/modulefiles/conda_init.sh 
conda activate pytorch_gpu

# run the test script
python gpu_test.py
