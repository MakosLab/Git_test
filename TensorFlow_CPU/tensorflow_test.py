import tensorflow as tf

# Check if TensorFlow is using the CPU
print("TensorFlow version:", tf.__version__)
print("Is TensorFlow using GPU? ", tf.config.list_physical_devices('GPU'))
print("Available devices:", tf.config.list_physical_devices())

# Simple TensorFlow computation
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 6], [7, 8]])
result = tf.matmul(a, b)

print("Matrix multiplication result:\n", result.numpy())


