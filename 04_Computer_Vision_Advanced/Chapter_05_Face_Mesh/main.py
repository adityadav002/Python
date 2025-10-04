import cv2
import mediapipe as mp
from mediapipe.python.solutions.face_mesh_connections import FACEMESH_TESSELATION

cap = cv2.VideoCapture(r"Chapter_05_Face_Mesh\video\3.webm")

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1) 

while True:
    success, frame = cap.read()
    if not success:
        print("Not getting the frames...")
        break
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)

    if results.multi_face_landmarks:
        for facelms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(frame, facelms, FACEMESH_TESSELATION, drawSpec, drawSpec)

            for id, lm in enumerate(facelms.landmark):
                # print(lm)
                h, w, _ = frame.shape
                x, y = int(lm.x * w), int(lm.y * h)
                print(id, x, y)


    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()
