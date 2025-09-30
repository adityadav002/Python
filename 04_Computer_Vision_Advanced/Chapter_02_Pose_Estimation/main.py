import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('./Chapter_02_Pose_Estimation/video/3.mp4')

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

target_width = 640
target_height = 640
pTime = 0

while True:
    success, frame = cap.read()
    if not success:
        print("Error: Cannot read frame or end of video.")
        break

    resized_frame = cv2.resize(frame, (target_width, target_height))
    imgRGB = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
    result = pose.process(imgRGB)

    if result.pose_landmarks:
        mpDraw.draw_landmarks(resized_frame, result.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(result.pose_landmarks.landmark):
            h, w, _ = resized_frame.shape
            print(id, lm)
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv2.circle(resized_frame, (cx, cy), 3, (255, 0, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(resized_frame, f'FPS: {int(fps)}', (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

    cv2.imshow('Pose Estimation Video', resized_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
