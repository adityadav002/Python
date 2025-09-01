import cv2

# Read the image from file : cv2.read('path', flags)

image = cv2.imread('Chapter_01\Keanu-Reeves.jpeg')        

if image is None:
    print("Error: Could not read the image.")
else:
    print("Image read successfully.")