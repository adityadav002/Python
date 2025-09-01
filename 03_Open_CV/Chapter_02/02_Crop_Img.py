import cv2

image = cv2.imread('Chapter_02\Keanu-Reeves.jpeg')

if image is None:
    print("Could not read the image.")
    exit()
else:
    cropped_image = image[20:600, 380:900]
    cv2.imshow('Cropped Image', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('Keanu-Cropped.jpeg', cropped_image)

# Crop the image to focus on the face region
# Adjust the pixel values in the slicing as needed to get the desired crop
# image[y1:y2, x1:x2], y rows, x columns