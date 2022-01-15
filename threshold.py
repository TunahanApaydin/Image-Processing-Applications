import cv2
import numpy as np

class thresholding:
    def __init__(self):
        self.path = "/home/tuna/Desktop/Image Processing/Image_Processing/threshold.png"
        self.path2 = "/home/tuna/Desktop/Image Processing/Image_Processing/adaptive_threshold.jpg"

    def simple_threshold(self):
        image = cv2.imread(self.path)
        grayscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # applying different thresholding
        # techniques on the input image
        # all pixels value above 120 will
        # be set to 255
        ret, threshold1 = cv2.threshold(grayscale_img, 120, 255, cv2.THRESH_BINARY)
        ret, threshold2 = cv2.threshold(grayscale_img, 120, 255, cv2.THRESH_BINARY_INV)
        ret, threshold3 = cv2.threshold(grayscale_img, 120, 255, cv2.THRESH_TRUNC)
        ret, threshold4 = cv2.threshold(grayscale_img, 120, 255, cv2.THRESH_TOZERO)
        ret, threshold5 = cv2.threshold(grayscale_img, 120, 255, cv2.THRESH_TOZERO_INV)

        cv2.imshow("Simple Threshold", np.vstack((grayscale_img, threshold1, threshold2, threshold3, threshold4, threshold5)))
    
    def adaptive_threshold(self):
        image = cv2.imread(self.path2)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        threshold1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 201, 5)
        threshold2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 95, 7)

        cv2.imshow("Adaptive Threshold", np.hstack((img, threshold1, threshold2)))

        '''
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C: Threshold Value = (Gaussian-weighted sum of the neighbourhood values – constant value).
        In other words, it is a weighted sum of the blockSize×blockSize neighborhood of a point minus constant.
        thresholdType: The type of thresholding to be applied.
        blockSize: Size of a pixel neighborhood that is used to calculate a threshold value.
        constant: A constant value that is subtracted from the mean or weighted sum of the neighbourhood pixels.
        '''
    def otsu_threshold(self):
        image = cv2.imread(self.path)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        ret, threshold = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY, cv2.THRESH_OTSU)

        cv2.imshow("Otsu Threshold", threshold)

        '''
        Syntax: cv2.threshold(source, thresholdValue, maxVal, thresholdingTechnique)
        Parameters:
        source: Input Image array (must be in Grayscale).
        thresholdValue: Value of Threshold below and above which pixel values will change accordingly.
        maxVal: Maximum value that can be assigned to a pixel.
        thresholdingTechnique: The type of thresholding to be applied.
        '''
        
if __name__ == "__main__":
    t = thresholding()
    #t.simple_threshold()
    #t.adaptive_threshold()
    t.otsu_threshold()

    if cv2.waitKey(0) & 0xFF == ord("x"):
        cv2.destroyAllWindows()