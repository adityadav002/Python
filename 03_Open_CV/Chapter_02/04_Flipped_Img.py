import cv2

image = cv2.imread('Chapter_02\image\Keanu-Cropped.jpeg')

if image is None:
    print("Could not read the image.")
else:
    flip_horizontal = cv2.flip(image, 1)  # Flip the image horizontally
    flip_vertical = cv2.flip(image, 0)    # Flip the image vertically
    flip_both = cv2.flip(image, -1)       # Flip the image both horizontally and vertically

    cv2.imshow('Original Image', image)
    cv2.imshow('Flipped Horizontally', flip_horizontal)
    cv2.imshow('Flipped Vertically', flip_vertical)
    cv2.imshow('Flipped Both', flip_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()