import cv2
import mediapipe as mp

image = cv2.imread(r'Chapter_03_Face_anonymizer\FrontFace.png')

if image is None:
    print("Error: Could not display the image.")
else:
    mp_face_detection = mp.solutions.face_detection
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        out = face_detection.process(img_rgb)

        if out.detections:
            for detection in out.detections:
             bbox = detection.location_data.relative_bounding_box

             height, width, _ = image.shape
             x = int(bbox.xmin * width)
             y = int(bbox.ymin * height)
             w_box = int(bbox.width * width)
             h_box = int(bbox.height * height)

             image[y:y + h_box, x:x + w_box] = cv2.blur(image[y:y + h_box, x:x + w_box], (30, 30))

        else:
            print("No faces detected.")

    cv2.imshow('Face with Box', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
