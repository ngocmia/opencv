# import the necessary packages
import numpy as np
import argparse
import cv2
import time

cap = cv2.VideoCapture(0)
while (True):
    ret, frame = cap.read()
    output = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    gray = cv2.medianBlur(gray, 5)
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3)

    kernel = np.ones((5,5), np.uint8)
    gray = cv2.erode(gray, kernel, iterations=1)
    # gray = erosion

    gray = cv2.dilate(gray, kernel, iterations=1)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1=110, param2=75, minRadius=0, maxRadius=0)

    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:

            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            # time.sleep(0.5)
            print "Column Number: "
            print x
            print "Row Number: "
            print y
            print "Radius is: "
            print r

        # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()