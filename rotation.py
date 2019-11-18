import matplotlib
import numpy as np
import cv2
import matplotlib.pyplot as plt

img= cv2.imread('/home/ngoc/PycharmProjects/123.jpeg')
rows, cols = img.shape[:2]
M= cv2.getRotationMatrix2D((cols/2, rows/2), 180,1)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
