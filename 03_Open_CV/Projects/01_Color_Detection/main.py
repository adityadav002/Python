import cv2
from PIL import Image
from utils import get_limits

yellow = [0, 255, 255]
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Not reading frames...")
        break

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_limit, upper_limit= get_limits(color=yellow)
    mask = cv2.inRange(hsv_img, lower_limit, upper_limit)
    mask_ = Image.fromarray(mask)
    box = mask_.getbbox()

    if  box is not None:
        x1, y1, x2, y2 = box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break 

cap.release()
cv2.destroyAllWindows()