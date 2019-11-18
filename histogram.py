import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('/home/ngoc/PycharmProjects/345.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_equal_hist = cv2.equalizeHist(gray)
cv2.imshow('histogram',img_equal_hist)
cv2.imshow('original', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()