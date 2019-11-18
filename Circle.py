import cv2
import numpy as np

img = cv2.imread('/home/ngoc/PycharmProjects/123.jpeg',0)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
img = cv2.Canny(img, 200,300)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,60, param1=130,param2=25,minRadius=0,maxRadius=80)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),1,(0,0,255),2)
cv2.imshow('original', img)
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
