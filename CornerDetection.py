import cv2
import numpy as np
import matplotlib.pyplot as plt

class CornerDetection:

    def __init__(self):
        self.path = "/home/tuna/Desktop/Image Processing/Image_Processing/corner.png"
        self.image = cv2.imread(self.path)
    
    def shi_tomasi_corner_detection(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        '''
        Syntax : cv2.goodFeaturesToTrack(gray_img, maxc, Q, minD)
        Parameters :
        gray_img – Grayscale image with integral values
        maxc – Maximum number of corners we want(give negative value to get all the corners>> not working)
        Q – Quality level parameter(preferred value=0.01)
        maxD – Maximum distance(preferred value=10)
        '''
        corners = cv2.goodFeaturesToTrack(gray, 28, 0.01, 10)
        corners = np.int0(corners) # convert corners values to integer so that we will be able to draw circles on them.

        for i in corners:
            x, y = i.ravel()
            cv2.circle(self.image, (x,y), 3, 255, -1) # -1: It is the thickness of the circle border line in px. Thickness of -1 px will fill the circle shape by the specified color.
        plt.imshow(self.image)
        plt.show()

if __name__ == "__main__":
    CD = CornerDetection()
    CD.shi_tomasi_corner_detection()

    if cv2.waitKey(0) & 0xFF == ord("x"):
        cv2.destroyAllWindows()
