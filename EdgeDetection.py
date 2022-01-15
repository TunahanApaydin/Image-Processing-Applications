import cv2
import numpy as np

class EdgeDetection:

    def __init__(self):
        self.capture = cv2.VideoCapture(0)
    
    def canny_edge_detection(self):

        while True:

            ret, frame = self.capture.read()

            if ret == True:

                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                lower_red = np.array([30, 150, 50])
                upper_red = np.array([255, 255, 180])

                mask = cv2.inRange(hsv, lower_red, upper_red)

                result = cv2.bitwise_and(frame, frame, mask = mask)

                cv2.imshow("Original Frame", frame)

                edges = cv2.Canny(result, 0, 200)

                cv2.imshow("Canny Edges", edges)

            if cv2.waitKey(10) & 0xFF == ord("x"):
                break

        self.capture.release()
        cv2.destroyAllWindows()
    
    def sobel_edge_detection(self):
        while True:

            ret, frame = self.capture.read()

            if ret == True:

                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5) # The second parameter is the depth of the destination image.
                sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5) # When ddepth=-1/CV_64F, the destination image will have the same depth as the source.

                laplacian = cv2.Laplacian(frame, cv2.CV_64F)

                cv2.imshow("Sobelx", sobelx)
                cv2.imshow("Sobely", sobely)
                cv2.imshow("Laplacian", laplacian)
            
            if cv2.waitKey(10) & 0xFF == ord("x"):
                break

        self.capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    ED = EdgeDetection()
    #ED.canny_edge_detection()
    ED.sobel_edge_detection()
