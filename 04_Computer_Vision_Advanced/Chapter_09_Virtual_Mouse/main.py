import cv2
import numpy as np
import HandTrackingModule as htm
import autopy

wCam, hCam = 640, 640
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
frameR = 100
smoothening = 15

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

while True:
    success, frame = cap.read()
    if not success:
        print("Not getting frames...")
        break
    img = detector.findHands(frame)
    lmlist, bbox = detector.findPosition(frame)

    if len(lmlist) != 0:
        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]

        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        if fingers[1] == 1 and fingers[2] == 0:
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, wCam-frameR), (0, hScr))

            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            x3 = max(0, min(wScr - 1, x3))
            y3 = max(0, min(hScr - 1, y3))

            autopy.mouse.move(clocX, clocY)
            cv2.circle(img, (x1, y1), 25, (0, 0, 255), -1)
            plocX, plocY = clocX, clocY
        
        if fingers[1] == 1 and fingers[2] == 1:
            length, infoList = detector.findDistance(8, 12, img)
            print(length)
            if length < 75:
                cv2.circle(img, (infoList[4], infoList[5]), 30, (0, 0, 255), -1)
                autopy.mouse.click()
    
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()