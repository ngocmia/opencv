import multiprocessing
import cv2


def filter (image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11,11),0)
    thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
    return thresh

def inpainted(image, thresh):
    img= cv2.inpaint(image, thresh, 25, cv2.INPAINT_TELEA)
    return img

cap = cv2.VideoCapture(0)
ret, image = cap.read()
queue = multiprocessing.Queue()
thresh = queue.put(image)
p1 = multiprocessing.Process(target=filter, args=(image, ))
p1.start()
p1.join()
img= inpainted(image, thresh)
p2 = multiprocessing.Process(target=inpainted, args=(image, thresh))
img = multiprocessing.Queue()

p2.start()
p2.join()

while (cap.isOpened()):
    cv2.imshow("preview", img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
