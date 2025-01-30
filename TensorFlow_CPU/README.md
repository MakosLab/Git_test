## 1. Load Conda on CHPC or UAHPC
      source /share/apps/modulefiles/conda_init.sh 

## 2. Create and activate environment for TensorFlow
      conda create --name tf_cpu python=3.10 -y
      conda activate tf_cpu

## 3. Install TensorFlow (CPU version)

      pip install tensorflow

## 4. Print TensorFlow version

      python -c "import tensorflow as tf; print(tf.__version__)"

## 5. Install additional liberies
      
      pip install numpy pandas matplotlib scikit-learn

## 6. Run your script 

      python tensorflow_test.py


