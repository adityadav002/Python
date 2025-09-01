import cv2

image = cv2.imread('Chapter_03\Keanu-Reeves.jpeg')

if image is None:
    print("Could not open or find the image.")
else:
    start_point = (400, 200)
    end_point = (800, 550)
    color = (0, 255, 0)
    thickness = 2
    image_with_rectangle = cv2.rectangle(image, start_point, end_point, color, thickness)

    cv2.imshow('Image with Rectangle', image_with_rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# thickness = -1 will fill the rectangle
# start_point = (x1, y1)
# end_point = (x2, y2)
# 400: left-rigt, 200: up-down
# 800: left-rigt, 550: up-down