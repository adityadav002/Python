import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))      # To get the width of the frames of the video.
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))    # To get the height of the frames of the video.

codec = cv2.VideoWriter_fourcc(*'mp4v')   # Define the codec and create VideoWriter object.The output is stored in 'output.avi' file.
recorder = cv2.VideoWriter('output.mp4', codec, 20.0, (frame_width, frame_height))
          #cv2.VideoWritter(filename, fourcc, fps, frameSize).

while True:
    success, image = camera.read()

    if not success:
        break

    recorder.write(image)   # Write the frame into the file 'output.avi'
    cv2.imshow('Recording...', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

camera.release()
recorder.release()
cv2.destroyAllWindows() 