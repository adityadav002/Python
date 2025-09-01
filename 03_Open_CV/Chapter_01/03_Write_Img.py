import cv2

image = cv2.imread('Chapter_01\Keanu-Reeves.jpeg')

if image is not None:
    new_img = cv2.imwrite('Keanu-Reeves_copy.jpeg', image)  # Write image to file system
    if(new_img):
        print("Image written to file system successfully.")
    else:
        print("Error in writing image to file system.")
else:
    print("Error in reading image file.")
