import cv2
import argparse
import mediapipe as mp

def process_img(image, face_detection):
    if image is None:
        print("Error: Could not process the image.")
        return image
    else:
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

                x = max(0, x)
                y = max(0, y)
                x_end = min(width, x + w_box)
                y_end = min(height, y + h_box)

                image[y:y_end, x:x_end] = cv2.blur(image[y:y_end, x:x_end], (100, 100))
        else:
            print("No faces detected.")
        return image

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--mode", default='webcam', help="Mode: 'image', 'video', or 'webcam'")
parser.add_argument("--filePath", default='Chapter_03_Face_anonymizer/front_face.mp4', help="Path to input file (used in image/video modes)")
args = parser.parse_args()

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:

    # IMAGE MODE
    if args.mode == 'image':
        image = cv2.imread(args.filePath)
        image = process_img(image, face_detection)
        cv2.imshow('Face with Blur', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # VIDEO FILE MODE
    elif args.mode == 'video':
        cap = cv2.VideoCapture(args.filePath)
        if not cap.isOpened():
            print("Error: Could not open video file.")
            exit()
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read video frame.")
            cap.release()
            exit()
        height, width, _ = frame.shape
        output_video = cv2.VideoWriter('outputvideo.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 25, (width, height))
        while ret:
            frame = process_img(frame, face_detection)
            output_video.write(frame)
            ret, frame = cap.read()
        cap.release()
        output_video.release()
        print("Video processing complete. Saved as 'outputvideo.mp4'.")

    # WEBCAM MODE
    elif args.mode == 'webcam':
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not access webcam.")
            exit()
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to grab frame from webcam.")
                break
            frame = process_img(frame, face_detection)
            cv2.imshow('Webcam Face Blur', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
