import cv2

cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("Error: Could not open video capture")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('Video Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()



# cv2.waitKey(1): Waits 1 millisecond for a key press.
#                 If a key is pressed, it returns a key code.
#                 If no key is pressed, it returns -1.

# & 0xFF: This is a bitmask.
#         It makes sure we only get the last 8 bits of the key code.
#         This helps avoid issues on different systems (like Windows vs Linux).

# ord('s'): ord('s') means "give me the ASCII value of 's'".
#           's' has an ASCII value of 115.