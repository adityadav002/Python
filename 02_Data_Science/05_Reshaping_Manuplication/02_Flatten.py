'''
.ravel()    Returns a flattened array
.flatten()  Returns a flattened array (copy)
.reshape()  Changes the shape of an array
.resize()   Changes the shape and size of an array
'''

import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:")
print(arr_2d)
print()

# ravel() returns a flattened array (1D)
arr_1d = arr_2d.ravel()
print("Flattened array using ravel():")
print(arr_1d)
print()

# flatten() also returns a flattened array (1D), but is a copy
arr_1d_copy = arr_2d.flatten()
print("Flattened array using flatten():")
print(arr_1d_copy)
print()

# reshape() changes the shape of the array
reshaped_arr = arr_1d.reshape(3, 2)
print("Reshaped array using reshape(3, 2):")
print(reshaped_arr)
print()

# resize() changes the shape and size of the array
arr_2d.resize(3, 2)
print("Resized array using resize(3, 2):")
print(arr_2d)
print()
# Note: resize() modifies the original array, while reshape() returns a new view