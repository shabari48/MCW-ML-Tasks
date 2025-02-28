import cv2

class FaceDetector:

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

    def detect_eyes(self, frame, face_x, face_y, face_w, face_h):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eye_frame = gray[face_y:face_y+face_h, face_x:face_x+face_w]
        return self.eye_cascade.detectMultiScale(eye_frame)