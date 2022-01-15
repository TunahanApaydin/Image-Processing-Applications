import cv2
import numpy as np

class MorphologicalOperations:

    def __init__(self):
        self.capture = cv2.VideoCapture(0)
    
    def morph_operations(self, operation): # Opening is erosion operation followed by dilation operation.
                                           # Closing is defined simply as a dilation followed by an erosion using the same structuring element used in the opening operation.
        while True:
            ret, frame = self.capture.read()

            if ret == True:
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                lower_blue = np.array([110, 50, 50]) # defining the range of masking
                upper_blue = np.array([130, 255, 255])

                mask = cv2.inRange(hsv, lower_blue, upper_blue)

                result = cv2.bitwise_and(frame, frame, mask = mask)

                kernel = np.ones((5, 5), np.uint8)

                operation_res = cv2.morphologyEx(mask, operation, kernel)

                cv2.imshow("mask", mask)
                cv2.imshow("Result", operation_res)

            if cv2.waitKey(10) & 0xFF == ord("x"):
                self.capture.release()
                cv2.destroyAllWindows()

if __name__ == "__main__":
    MO = MorphologicalOperations()
    MO.morph_operations(cv2.MORPH_OPEN)