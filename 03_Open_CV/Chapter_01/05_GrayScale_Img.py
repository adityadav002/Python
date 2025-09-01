import cv2

image = cv2.imread('Chapter_01\Keanu-Reeves.jpeg')

if image is not None:
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    cv2.imshow('Gray Scale Image', gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('Keanu_GrayScale.jpeg', gray_img)
else:
    print("Error: Image not found.")


# Convert the image to gray scale
# cv2.cvtColor(image_name, cv2.COLOR_BGR2GRAY)