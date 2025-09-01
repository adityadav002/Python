import cv2
import numpy as np

image = cv2.imread('Chapter_06\Keanu-Reeves.jpeg', cv2.IMREAD_GRAYSCALE)

median = np.median(image)  # Compute the median of the pixel intensities
sigma = 0.33               # Set the sigma value for threshold calculation
lower = int(max(0, (1.0 - sigma) * median))     # Calculate lower threshold
upper = int(min(255, (1.0 + sigma) * median))   # Calculate upper threshold

if image is None:
    print("Image not found")
    exit()
else:
    blurred = cv2.GaussianBlur(image, (5, 5), 1.4)  # Apply Gaussian blur to reduce noise
    edges = cv2.Canny(blurred, lower, upper)        # Perform Canny edge detection

    cv2.imshow('Original Image', image)
    cv2.imshow('Canny Edges', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# cv2.Canny(image-source, threshold1, threshold2)
# threshold1: Lower threshold for the hysteresis procedure.
# threshold2: Upper threshold for the hysteresis procedure.
# Edges with intensity gradient above threshold2 are considered strong edges.
# Edges with intensity gradient between threshold1 and threshold2 are considered weak edges.
# Weak edges connected to strong edges are retained, while others are discarded. 