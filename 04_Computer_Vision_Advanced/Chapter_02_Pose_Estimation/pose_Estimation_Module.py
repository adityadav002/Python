import cv2
import mediapipe as mp
import time


class poseDetection():
    def __init__(self, mode=False, smooth=True,
             detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(
            static_image_mode=self.mode,
            smooth_landmarks=self.smooth,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
    )

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return lmList


def main():
    cap = cv2.VideoCapture('./Chapter_02_Pose_Estimation/video/4.mp4')
    target_width = 640
    target_height = 640
    pTime = 0
    detector = poseDetection()

    while True:
        success, frame = cap.read()
        if not success:
            print("End of video or cannot read frame.")
            break

        resized_frame = cv2.resize(frame, (target_width, target_height))
        img = detector.findPose(resized_frame)
        lmList = detector.findPosition(img, draw=True)
        print(lmList)

        # FPS Calculation
        cTime = time.time()
        fps = 1 / (cTime - pTime + 1e-5)  # Avoid division by zero
        pTime = cTime

        # Show FPS on frame
        cv2.putText(img, f'FPS: {int(fps)}', (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

        # Display frame
        cv2.imshow('Pose Estimation Video', img)

        # Quit with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quitting...")
            break

    # Release and clean up
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
