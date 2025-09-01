import cv2

image = cv2.imread('Chapter_03\Keanu-Reeves.jpeg')

if image is None:
    print("Could not open or find the image.")
else:
    print("Image loaded successfully.")

    start_point = (50, 100)
    end_point = (1000, 430)
    color = (0, 0, 255)  # Blue color in BGR
    thickness = 4

    line_img = cv2.line(image, start_point, end_point, color, thickness)
    cv2.imshow('Line on Image', line_img)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()