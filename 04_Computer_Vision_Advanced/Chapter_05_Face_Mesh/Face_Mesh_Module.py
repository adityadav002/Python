import cv2
import mediapipe as mp
from mediapipe.python.solutions.face_mesh_connections import FACEMESH_TESSELATION

class faceMeshDetector():
    def __init__(self, staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5):
        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(
            static_image_mode=self.staticMode,
            max_num_faces=self.maxFaces,
            min_detection_confidence=self.minDetectionCon,
            min_tracking_confidence=self.minTrackCon
        )
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    def findFaceMesh(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(imgRGB)

        if results.multi_face_landmarks:
            for facelms in results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, facelms, FACEMESH_TESSELATION, self.drawSpec, self.drawSpec)
                for id, lm in enumerate(facelms.landmark):
                    h, w, _ = img.shape
                    x, y = int(lm.x * w), int(lm.y * h)
                    # print(id, x, y)
        return img


def main():
    cap = cv2.VideoCapture(r"Chapter_05_Face_Mesh\video\3.webm")
    detection = faceMeshDetector()
    while True:
        success, frame = cap.read()
        img = detection.findFaceMesh(frame, True)
        if not success:
            print("Not getting the frames...")
            break

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quitting...")
            break
    cap.release()

cv2.destroyAllWindows()

if __name__ == "__main__":
    main()