import cv2

image = cv2.imread('Chapter_02\Keanu-Reeves.jpeg')

if image is None:
    print("Could not read the image.")
else:
    h, w = image.shape[:2]                              # Get image dimensions

    center = (w // 2, h // 2)                           # Calculate the center of the image
    M = cv2.getRotationMatrix2D(center, 45, 1.0)        # Rotate 45 degrees
    rotated_image = cv2.warpAffine(image, M, (w, h))    # Apply the rotation

    cv2.imshow('Rotated Image', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('rotated_image.jpg', rotated_image)     # Save the rotated image
