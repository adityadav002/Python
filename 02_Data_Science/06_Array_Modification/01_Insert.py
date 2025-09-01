import numpy as np

arr = np.array([1, 2, 3, 4, 5])
new_arr = np.insert(arr, 2, 10)
print(new_arr)  

# axis parameter example, 0 for rows, 1 for columns
arr_2d = np.array([[1, 2], [3, 4]])
new_arr_2d = np.insert(arr_2d, 1, [10, 20], axis=0)  
print(new_arr_2d)

new_arr_2d_col = np.insert(arr_2d, 1, [10, 20], axis=1)  
print(new_arr_2d_col)