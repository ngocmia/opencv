import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([29, 86, 6])
    upper_green = np.array([64, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(img, img, mask=mask)
    ret, thresh = cv2.threshold(mask, 127,255,cv2.THRESH_BINARY)
    image, contour, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contour:
        (x,y), radius = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))
        radius = int(radius)
        mask = cv2.circle(mask, center, radius, (0,255,0), 2)
    cv2.drawContours(frame, contour, -1, (255, 0 ,0), 1)
    cv2.imshow('frame',mask)

    cv2.imshow('orginal', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
