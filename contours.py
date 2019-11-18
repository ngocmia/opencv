# import the necessary packages
from shapeDetector import ShapeDetector
import argparse
import imutils
import cv2
from imutils.video import VideoStream
import time


capture = cv2.VideoCapture(0)
while (capture.isOpened()):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.Canny(gray, 200,300)
    cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[0:2]
    sd = ShapeDetector()
    for c in cnts:
       M = cv2.moments(c)
       cX = int(M["m10"] / M["m00"])
       cY = int(M["m01"] / M["m00"])
       shapes = sd.detect(c)
       c = c.astype("int")
       cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
       cv2.putText(frame, shapes, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.imshow("Image", frame)
    if cv2.waitKey(25) & 0xFF ==ord('q'):
        break
cv2.destroyAllWindows()
