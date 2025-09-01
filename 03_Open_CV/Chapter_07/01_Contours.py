import cv2

image = cv2.imread('Chapter_07\shape.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh_img = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

contour, heirarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image, contour, -1, (0, 255, 0), 3)

cv2.imshow('Contour', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# contour: List of all detected contours (each is a set of points).
# heirarchy: Information about the nested structure of contours (like shapes inside shapes).
# cv2.RETR_TREE: Retrieves all contours and builds a tree structure.
# cv2.CHAIN_APPROX_SIMPLE: Compresses the contour points (saves memory).

# image: The original image where contours will be drawn.
# contour: The list of contours to draw.
# -1: Draw all contours. You can use 0, 1, 2... to draw a specific one.
# (0, 255, 0): The color of the contour — green in this case (BGR format).
# 3: The thickness of the lines.