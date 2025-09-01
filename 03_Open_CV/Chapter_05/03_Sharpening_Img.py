import cv2
import numpy as np

image = cv2.imread('Chapter_05\Keanu-Reeves.jpeg')

smooth_sharpen = np.array([
    [0, -0.5, 0],
    [-0.5, 3, -0.5],
    [0, -0.5, 0]
])


if image is None:
    print("Could not read the image.")
    exit()
else:
    sharpened_img = cv2.filter2D(image , -1, smooth_sharpen)
    cv2.imshow('Original Image', image)
    cv2.imshow('Sharpened Image', sharpened_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# cv2.filter2D(src, ddepth, kernel)
# ddepth = -1 means the output image will have the same depth as the source image
# kernel = convolution matrix
# A positive value in the kernel emphasizes the corresponding pixel, while a negative value de-emphasizes it.