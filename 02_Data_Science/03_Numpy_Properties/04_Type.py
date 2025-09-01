import numpy as np

arr = np.array([1, 2, 3.61, 4, 5])
print(arr)
print(arr.dtype) 

int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)

