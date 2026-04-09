import cv2

cap= cv2.VideoCapture(0)

while True:
    ret, frame= cap.read()
    w = int(cap.get(3))
    h = int(cap.get(4))
    # list me all fonts supported in cv2
    font = cv2.FONT_HERSHEY_SIMPLEX
    # img = cv2.line(frame,(0,0),(w,h), (255,0,0), 5)
    img = cv2.putText(frame, 'Text written on video captured',(50, h - 50), 
                      font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()