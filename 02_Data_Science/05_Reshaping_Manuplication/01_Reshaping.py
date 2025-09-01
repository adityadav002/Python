import numpy as np

# reshape(rows, columns), doesn't create copy, just changes the view
# original array must have same number of elements as new shape

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
print()