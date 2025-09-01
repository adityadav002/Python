import cv2

image = cv2.imread('Chapter_03\Keanu-Reeves.jpeg')

if image is None:
    print("Could not open or find the image.")
else:
    cv2.putText(image, 'Keanu Reeves', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('Image with Text', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# cv2.putText(image_source, 'text', (x, y), fontType, fontScale, color, thickness)
