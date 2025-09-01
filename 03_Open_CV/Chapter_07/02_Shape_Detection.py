import cv2

image = cv2.imread('Chapter_07\shape.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh_img = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

contours, heirarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cornors = len(approx)

    if cornors == 3:
        shape_name = "Triangle"
    elif cornors == 4:
        shape_name = "Rectangle"
    elif cornors == 5:
        shape_name = "Pentagon"
    elif cornors > 5:
        shape_name = "Circle"
    else:
        shape_name = "Shape Not Found"

    cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(image, shape_name, (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow('Contour', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

