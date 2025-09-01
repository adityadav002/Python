import numpy as np

'''
np.concatenate((arr1, arr2, ...), axis=0)
    Joins two or more arrays of the same shape along a specified axis.
    Default axis is 0. If axis is None, arrays are flattened before use.
    axios 0 : vertically
    axios 1 : horizontally
'''


arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

new_arr = np.concatenate((arr1, arr2))
print(new_arr)