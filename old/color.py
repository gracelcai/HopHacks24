import numpy as np
import cv2

# cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture("clips/clip6.mp4")

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_gray = np.array([0, 0, 40])   
    upper_gray = np.array([180, 40, 120])

    mask = cv2.inRange(hsv, lower_gray, upper_gray)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()