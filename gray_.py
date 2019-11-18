import numpy
import cv2 as cv
img = cv.imread('/home/ngoc/PycharmProjects/123.jpeg', 0)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()