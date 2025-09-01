import cv2

image = cv2.imread('Chapter_02\Keanu-Reeves.jpeg')

if image is None:
    print("Image not found.")
else:
    resized_img = cv2.resize(image, (300, 300))
    cv2.imshow('Resized Image', resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('Keanu-resized.jpeg', resized_img)


# cv2.reszie(image_source(name), (width, height))