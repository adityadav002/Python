import cv2
import numpy as np
import Pose_Estimation_Module as pm

wCam, hCam = 740, 600
cap = cv2.VideoCapture(r"Chapter_07_AI_Trainer\Video\1.mp4")

detector = pm.poseDetection()
count = 0
dir = 0

while True:
    success, frame = cap.read()
    if not success:
        print("Not getting the frame...")
        break
    frame = cv2.resize(frame, (wCam, hCam))
    img = detector.findPose(frame, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        angle = detector.findAngle(img, 12, 14, 16)  # Right Hand
        angle = detector.findAngle(img, 11, 13, 15)  # Left Hand
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (220, 310), (650, 100))

        # check for dumbbell curls
        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1

        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0 

        # Draw Bar
        cv2.rectangle(img, (680, 100), (700, 600), (0, 255, 0), 2)
        cv2.rectangle(img, (680, int(bar)), (700, 600), (0, 255, 0), -1)

        cv2.putText(img, f'{int(count)}', (50, 200), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0), 3)

    cv2.imshow("Video", img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        print("Quitting..,")
        break

cap.release()
cv2.destroyAllWindows()
