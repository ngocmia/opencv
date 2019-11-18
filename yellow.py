import cv2
import numpy as np

img = cv2.imread('/home/ngoc/PycharmProjects/pikachu.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_yellow = np.array([20,50,20])
upper_yellow = np.array([40, 255, 255])
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
res = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
