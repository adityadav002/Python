import cv2

image = cv2.imread('Chapter_01\Keanu-Reeves.jpeg')

if image is not None:
    h, w, c = image.shape  # h: height, w: width, c: channels 
    print(f"Image load successfully:\nHeight: {h}\nWidth: {w}\nChannels: {c}")
else:
    print("Error: Image not found or unable to load.")