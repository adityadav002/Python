import cv2

image = cv2.imread('Chapter_05\Keanu-Reeves.jpeg')

if image is None:
    print("Could not read the image.")
    exit()
else:
    blurred_img = cv2.GaussianBlur(image, (13, 13), 9)
    cv2.imshow('Original Image', image  )
    cv2.imshow('Blurred Image', blurred_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# cv2.GaussianBlur(image-source, (kernel_width, kernel_height), sigmaX)
# kernel size should be positive and odd numbers.
# sigmaX more the value, more the blur effect.