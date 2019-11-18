# import the necessary packages
from shapeDetector import ShapeDetector
import imutils
import cv2

image = cv2.imread("/home/ngoc/PycharmProjects/567.jpg")
cv2.imshow('original', image)
gray = cv2.Canny(image, 50, 200)
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:16]
sd = ShapeDetector()

for c in cnts:

    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    shape = sd.detect(c)
    c = c.astype("int")
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.imshow("Image", image)
    cv2.imshow("gray", gray)

cv2.waitKey(0)