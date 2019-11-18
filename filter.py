import numpy as np
import cv2

img = cv2. imread('/home/ngoc/PycharmProjects/123.jpeg')
kernel = np.ones((5,5 ), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)

cv2.imshow('img', img)
cv2.imshow('filter', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()