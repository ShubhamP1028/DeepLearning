import numpy as np
import cv2
cap = cv2.VideoCapture(0)  # number of camera that is being used to capture the video 0 being default for only one camera

while True:
    ret , frame = cap.read()
    width = int(cap.get(3))
    height= int(cap.get(4))

    start_point = (0, 0)
    end_point = (width, height)
    circ_color = (120, 0, 0)
    line_color = (0,120,0)
    rect_color = (0,0, 120)  # BGR format
    center = (200,200)
    radius = 50
    thickness = 14
    line = cv2.line(frame, start_point, end_point, line_color, thickness)
    circ = cv2.circle(frame, center, radius, circ_color, thickness)
    rect = cv2.rectangle(frame, start_point, end_point, rect_color, thickness)
    image = np.zeros(frame.shape, dtype=np.uint8)
    small_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = small_frame
    image[height//2:, :width//2] = cv2.rotate(small_frame, cv2.ROTATE_180)    
    image[:height//2, width//2:] = cv2.rotate(small_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = cv2.rotate(small_frame, cv2.ROTATE_180)
    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()