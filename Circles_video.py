import cv2
import numpy as np

capture = cv2.VideoCapture(0)
while(capture.isOpened()):
    ret, image = capture.read()
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    output = image.copy()
    grey = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5,5), np.float32)/25
    grey = cv2.filter2D(grey, -1, kernel)
    #grey = cv2.medianBlur(grey, 5)
    #grey = cv2.GaussianBlur(grey, (5,5), 0)
    #grey = cv2.Canny(grey, 200,300)
    circles = cv2.HoughCircles(grey, cv2.HOUGH_GRADIENT, 1, 50, param1=45, param2=110, minRadius=0, maxRadius=0)
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle in the image
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    cv2.imshow("output", output)
    #cv2.imshow("original", image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()



