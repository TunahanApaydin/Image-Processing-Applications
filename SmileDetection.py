import cv2

class Detection:

	def __init__(self):
		self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
		self.smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
	
	def face_detection(self, gray, frame):
		faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)

			roi_gray = gray[y:y+h, x:x+w]
			roi_frame = frame[y:y+h, x:x+w]

			smiles = self.smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

			for (sx, sy, sw, sh) in smiles:
				cv2.rectangle(roi_frame, (sx, sy), ((sx + sw), (sy + sh)), (0, 255, 0), 2)

		return frame
	
	def smile_detection(self, gray, frame):
		smiles = self.smile_cascade.detectMultiScale(gray, 1.8, 20)

		for (x, y, w, h) in smiles:
			cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)

		return frame


if __name__ == "__main__":
	capture = cv2.VideoCapture(0)
	detection = Detection()

	while True:
		ret, frame = capture.read()

		if ret == True:
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			canvas = detection.face_detection(gray, frame)

			cv2.imshow("Detection", canvas)
		
		if cv2.waitKey(10) & 0xFF == ord("x"):
			capture.release()
			cv2.destroyAllWindows()