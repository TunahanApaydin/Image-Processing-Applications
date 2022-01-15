import cv2
import numpy as np

class Filtering:

    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        self.path = "/home/tuna/Desktop/Image Processing/Image_Processing/flower.jpeg"
    
    def color_filtering(self):

        while True:
            ret, computer_cam = self.camera.read()
            hsv = cv2.cvtColor(computer_cam, cv2.COLOR_BGR2HSV)
            
            lower_blue = np.array([100,60,60])
            upper_blue = np.array([140,255,255])

            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            filtered_image = cv2.bitwise_and(computer_cam, computer_cam, mask= mask)

            cv2.imshow('Original Video', computer_cam)
            cv2.imshow('Masked Video', mask)
            cv2.imshow('Filtered Video', filtered_image)

            if cv2.waitKey(25) & 0xFF == ord('x'):
                break
        self.camera.release()
        cv2.destroyAllWindows()

    def blurring(self):
        img = cv2.imread(self.path)
        gaussian = cv2.GaussianBlur(img, (9,9), 0)
        median = cv2.medianBlur(img, 9)
        bileteral = cv2.bilateralFilter(img, 9, 75, 75)

        cv2.imshow("Gausian Blur", np.hstack((img, gaussian)))
        cv2.imshow("Median Blur", np.hstack((img, median)))
        cv2.imshow("Bileteral Blur", np.hstack((img, bileteral)))
        #cv2.imshow("Bluring", np.hstack((img, gaussian, median, bileteral)))

if __name__ == '__main__':
    filtering = Filtering()
    filtering.color_filtering()
    #filtering.blurring()

    if cv2.waitKey(0) & 0xFF == ord("x"):
        cv2.destroyAllWindows()