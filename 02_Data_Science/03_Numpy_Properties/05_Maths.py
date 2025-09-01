import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Sum:", np.sum(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
print("Index of Minimum:", np.argmin(arr))
print("Index of Maximum:", np.argmax(arr))

print(arr.shape)
print(arr.dtype)
print(arr + 10)  # Add 10 to each element
print(arr * 2)   # Multiply each element by 2
print(arr ** 2)  # Square of each element
print(arr % 2)   # Modulus of each element by 2
print(arr // 2)  # Floor division of each element by 2

print(np.sqrt(arr))  # Square root of each element
print(np.log(arr))   # Natural logarithm of each element
print(np.exp(arr))   # Exponential of each element
print(np.sin(arr))   # Sine of each element (in radians)
print(np.cos(arr))   # Cosine of each element (in radians)
print(np.tan(arr))   # Tangent of each element (in radians)
print(np.round(arr / 3, 2))  # Round each element after division by 3 to 2 decimal places
print(np.ceil(arr / 3))  # Ceiling of each element after division by 3
print(np.floor(arr / 3))  # Floor of each element after division by 3
print(np.abs(arr - 3))  # Absolute difference from 3
print(np.clip(arr, 2, 4))  # Clip values to be between 2 and 4
print(np.sort(arr)[::-1])  # Sort in descending order
print(np.unique(arr))  # Unique elements
print(np.cumsum(arr))  # Cumulative sum
print(np.cumprod(arr))  # Cumulative product
print(np.diff(arr))  # Difference between consecutive elements
print(np.where(arr > 3, arr, 0))  # Replace elements greater than 3 with themselves, else 0
print(np.nonzero(arr % 2 == 0))  # Indices of even elements
print(np.histogram(arr, bins=3))  # Histogram with 3 bins
print(np.corrcoef(arr, arr * 2))  # Correlation coefficient with a
print(np.polyfit(arr, arr * 2, 1))  # Linear fit (slope and intercept)
print(np.linalg.norm(arr))  # Euclidean norm
print(np.dot(arr, arr))  # Dot product with itself
print(np.cross(arr[:3], arr[1:4]))  # Cross product of first three and next three elements
print(np.all(arr > 0))  # Check if all elements are greater than 0
print(np.any(arr > 3))  # Check if any element is greater than 3
print(np.isfinite(arr))  # Check if elements are finite
print(np.isnan(arr))  # Check if elements are NaN       