import numpy as np
import cv2

img =cv2.imread('/home/ngoc/PycharmProjects/jiyeon.jpeg')
cv2.imshow('original', img)
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

rect = (11,15,175,274)
cv2.grabCut(img, mask, rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = (mask==2)|(mask==0)
img[mask2] =255
cv2.imshow('foreground', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




