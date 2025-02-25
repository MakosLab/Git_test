#!/bin/bash
 
# load the PyTorch module
 
source /apps/profiles/modules_asax.sh.dyn
module load pytorch/2.3.1_gpu_a
 
# run your software here
 
python md_cuda.py > output.log


