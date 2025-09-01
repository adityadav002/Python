import cv2

image = cv2.imread('Chapter_05\Keanu-Reeves.jpeg')

if image is None:
    print("Could not read the image.")
    exit()
else:
    median_blur = cv2.medianBlur(image, 11)
    cv2.imshow('Original Image', image)
    cv2.imshow('Median Blurred Image', median_blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# cv2.medianBlur(src, ksize[, dst]) -> dst
# ksize must be odd and greater than 1, e.g., 3, 5, 7 ...
# The function smooths an image using the median filter.
# Each channel of a pixel is processed independently.
# The median is calculated by first sorting all the pixel values from the surrounding neighborhood into numerical order
# and then replacing the pixel being considered with the middle pixel value.