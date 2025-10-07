import cv2
import numpy as np
import os
import HandTrackingModule as htm

# 1. Load header images
folderPath = "Chapter_08_AI_Virtual_Painter/assests"
headerList = []
for imgName in sorted(os.listdir(folderPath)):
    img = cv2.imread(os.path.join(folderPath, imgName))
    headerList.append(cv2.resize(img, (1280, 125)))

# Default values
header = headerList[0]
drawColor = (0, 0, 255)  # Red

# 2. Webcam setup
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

# 3. Hand detector
detector = htm.handDetector(detectionCon=0.85)
xp, yp = 0, 0  # Previous positions
imgCanvas = np.zeros((720, 1280, 3), np.uint8)  # Blank canvas

brushThickness = 15
eraserThickness = 50

while True:
    # 4. Read frame and flip
    success, frame = cap.read()
    if not success:
        print("Not getting the frame...")
        break

    # 5. Detect hands and positions
    frame = detector.findHands(frame, draw=False)
    lmList = detector.findPosition(frame, draw=False)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]   # Index tip
        x2, y2 = lmList[12][1:]  # Middle tip

        fingers = detector.fingersUp()

        # 6. Selection mode – two fingers up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0  # Reset previous position

            cv2.rectangle(frame, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

            # Check toolbar area
            if y1 < 125:
                if 250 < x1 < 450:
                    header = headerList[0]
                    drawColor = (0, 0, 255)  # Red
                elif 550 < x1 < 750:
                    header = headerList[1]
                    drawColor = (255, 0, 0)    # Blue
                elif 800 < x1 < 950:
                    header = headerList[2]
                    drawColor = (0, 255, 0)    # Green
                elif 1050 < x1 < 1200:
                    header = headerList[3]
                    drawColor = (0, 0, 0)      # Eraser

        # 7. Drawing mode – only index finger up
        if fingers[1] and not fingers[2]:
            cv2.circle(frame, (x1, y1), 15, drawColor, cv2.FILLED)

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):  # Eraser
                cv2.line(frame, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(frame, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp, yp = x1, y1

    # 8. Combine canvas and webcam
    grayCanvas = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(grayCanvas, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)

    frame = cv2.bitwise_and(frame, imgInv)
    frame = cv2.bitwise_or(frame, imgCanvas)

    frame[0:125, 0:1280] = header

    # 10. Show frame
    cv2.imshow("AI Virtual Painter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()
