import numpy as np
import cv2
cap = cv2.VideoCapture(0)  # number of camera that is being used to capture the video 0 being default for only one camera

while True:
    ret , frame = cap.read()
    image = np.zeros(frame.shape, dtype=np.uint8)

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()