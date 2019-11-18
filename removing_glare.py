import cv2
import multiprocessing
import numpy as np
cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, image= cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11,11),0)
    thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
    inpainted =cv2.inpaint(image, thresh, 25, cv2.INPAINT_TELEA)
    cv2.imshow('anhmoi', inpainted)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()