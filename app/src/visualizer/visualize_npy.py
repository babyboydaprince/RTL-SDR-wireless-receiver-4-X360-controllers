import numpy as np

# Replace with the path to your captured signal file
file_path = './captured_signal.npy'

# Load the data from the .npy file
signal_data = np.load(file_path)

# Print the loaded data (or part of it if it’s large)
print(signal_data)

# Optionally, inspect the shape of the array
print("Shape of the signal data:", signal_data.shape)
