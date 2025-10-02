import cv2
import mediapipe as mp

cap = cv2.VideoCapture(r"Chapter_04_Face_Detection\video\4.webm")
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.75)

while True:
    success, frame = cap.read()
    if not success:
        print("Not getting the frames...")
        break

    imRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = faceDetection.process(imRGB)
    print(result)

    if result.detections:
        for id, detection in enumerate(result.detections):
            # mpDraw.draw_detection(frame, detection)
            bboxC = detection.location_data.relative_bounding_box
            h, w, _ = frame.shape
            bbox = int(bboxC.xmin * w), int(bboxC.ymin * h),\
                   int(bboxC.width * w), int(bboxC.height * h)
            cv2.rectangle(frame, bbox, (0, 0, 255), 2)
            cv2.putText(frame, f'{int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()
