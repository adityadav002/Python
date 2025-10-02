import cv2
import mediapipe as mp

class faceDetector():
    def __init__(self, minDetectionCon=0.5):
            self.minDetectionCon = minDetectionCon
            self.mpFaceDetection = mp.solutions.face_detection
            self.mpDraw = mp.solutions.drawing_utils
            self.faceDetection = self.mpFaceDetection.FaceDetection(minDetectionCon)

    def findFace(self, img, draw=True):
        imRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.faceDetection.process(imRGB)
        bboxs = []
        if self.result.detections:
            for id, detection in enumerate(self.result.detections):
                # self.mpDraw.draw_detection(img, detection)
                bboxC = detection.location_data.relative_bounding_box
                h, w, _ = img.shape
                bbox = int(bboxC.xmin * w), int(bboxC.ymin * h),\
                    int(bboxC.width * w), int(bboxC.height * h)
                bboxs.append([id, bbox, detection.score])
                if draw:
                    self.cornerDraw(img, bbox)
                cv2.putText(img, f'{int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        return img, bboxs    

    def cornerDraw(self, img, bbox, length=40, thickness=10):
        x, y, w, h = bbox
        x1, y1, = x+w, y+h

        cv2.rectangle(img, bbox, (0, 255, 255), )
        # Top-left
        cv2.line(img, (x,y), (x+length, y), (0,0,255), thickness)
        cv2.line(img, (x,y), (x, y+length), (0,0,255), thickness)

        # Top-Right
        cv2.line(img, (x1,y), (x1-length, y), (0,0,255), thickness)
        cv2.line(img, (x1,y), (x1, y+length), (0,0,255), thickness)

        # Bottom-left
        cv2.line(img, (x,y1), (x+length, y1), (0,0,255), thickness)
        cv2.line(img, (x,y1), (x, y1-length), (0,0,255), thickness)     

        # Bottom-Right
        cv2.line(img, (x1,y1), (x1-length, y1), (0,0,255), thickness)
        cv2.line(img, (x1,y1), (x1, y1-length), (0,0,255), thickness)   

        return img

def main():
    cap = cv2.VideoCapture(r"Chapter_04_Face_Detection\video\4.webm")
    detector = faceDetector()
    while True:
        success, frame = cap.read()
        if not success:
            print("Not getting the frames...")
            break
        img, bboxs = detector.findFace(frame, True)
        # print(bboxs)

        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
           print("Quitting...")
           break
    cap.release()

cv2.destroyAllWindows()

if __name__ == "__main__":
    main()