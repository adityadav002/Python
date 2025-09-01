import cv2

image = cv2.imread('Chapter_06\Keanu-Reeves.jpeg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found")
    exit()
else:
    ret, threshold_img = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

    if not ret:
        print("Thresholding failed")
        exit()
    
    cv2.imshow('Original Image', image)
    cv2.imshow('Threshold Image', threshold_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# cv2.threshold(image-src, threshold-value, max-value, thresholding-type)

# ret: Boolean value indicating if the operation was successful
# threshold_img: Resulting binary image 
# image: Source grayscale image
# threshold-value: if value is 200, If a pixel's brightness is above 200, it becomes 255 (white).
#                                   If it's 200 or below, it becomes 0 (black).
# This turns the image into pure black-and-white
