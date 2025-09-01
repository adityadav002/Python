import numpy as np

# np.delete(arr_name, index) - Deletes the element at the specified index from the array and returns a new array.

arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)
new_arr = np.delete(arr, 2) 
print("Array after deletion:", new_arr)


arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nOriginal 2D array:\n", arr_2d)
new_arr_2d = np.delete(arr_2d, 1, axis=0) 
print("2D array after deleting row 1:\n", new_arr_2d)
new_arr_2d_col = np.delete(arr_2d, 1, axis=1) 
print("2D array after deleting column 1:\n", new_arr_2d_col)
# Note: The original array remains unchanged; np.delete() returns a new array.