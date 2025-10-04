import cv2
import numpy as np
import HandTrackingModule as htm
import math
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

# Webcam resolution
wCam, hCam = 320, 240
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Hand detector
detector = htm.handDetector(detectionCon=0.75)

# Pycaw audio setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

# Volume bar and percentage
volBar = 400
volPer = 0

while True:
    success, frame = cap.read()
    if not success:
        print("Failed to grab frame.")
        break
    
    img = detector.findHands(frame)
    ldm = detector.findPosition(img, draw=False)

    if ldm:
        x1, y1 = ldm[4][1], ldm[4][2]
        x2, y2 = ldm[8][1], ldm[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 12, (0, 255, 0), 3)
        cv2.circle(img, (x2, y2), 12, (0, 255, 0), 3)
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
        cv2.circle(img, (cx, cy), 12, (0, 0, 255), -1)

        # Calculate distance between fingers
        length = math.hypot(x2 - x1, y2 - y1)

        # Map distance to volume scalar (0.0 - 1.0)
        volScalar = np.interp(length, [50, 400], [0.0, 1.0])
        volume.SetMasterVolumeLevelScalar(volScalar, None)

        # Calculate volume bar position and percentage
        volBar = np.interp(volScalar, [0.0, 1.0], [400, 150])
        volPer = int(volScalar * 100)

        if length < 50:
            cv2.circle(img, (cx, cy), 12, (255, 0, 0), -1)

        # Draw volume bar and percentage
        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), -1)
        cv2.putText(img, f'{volPer} %', (40, 140), cv2.FONT_ITALIC, 1, (0, 0, 255), 2)

    cv2.imshow("Volume Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()
