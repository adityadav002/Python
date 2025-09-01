import cv2

image = cv2.imread('Chapter_03\Keanu-Reeves.jpeg')

if image is None:
    print("Could not open or find the image.")
else:
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    radius = 200
    color = (0, 255, 0)  
    thickness = 2

    cv2.circle(image, center, radius, color, thickness)

    cv2.imshow('Image with Circle', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()