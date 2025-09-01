import cv2

image = cv2.imread('Chapter_01\Keanu-Reeves.jpeg')

if image is None:
    print("Error: Could not display the image.")
else:
    cv2.imshow('Keanu Reeves', image)  # Display the image in a window
    cv2.waitKey(0)                     # Wait for a key press to close the window(image)
    cv2.destroyAllWindows()            # Close all OpenCV windows
    