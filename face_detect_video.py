import imutils
import cv2

# Define paths
video_path = ('/home/ngoc/PycharmProjects/video1.mp4')
cascade_path =cv2.CascadeClassifier("/home/ngoc/PycharmProjects/hello/venv/lib/python3.5/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# Construct the face detector
# Load the video
camera = cv2.VideoCapture(0)

while True:
    # Grab the current frame
    (ok, frame) = camera.read()

    # If a frame does not exist, video is over
    if not ok:
        break

    # Resize the frame and convert it to greyscale
    frame = imutils.resize(frame, width=600)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image and clone the frame
    face_boxes = cascade_path.detectMultiScale(gray, 1.3 ,5)
    clone = frame.copy()

    # Draw the face bounding boxes
    for (x, y, w, h) in face_boxes:
        cv2.rectangle(clone, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show our detected faces
    cv2.imshow("Face", clone)

    # Ff the 'q' key is pressed, stop the loop
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()