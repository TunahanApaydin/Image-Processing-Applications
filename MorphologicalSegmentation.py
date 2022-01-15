import cv2
import numpy as np
import matplotlib.pyplot as plt

class MorphSeg:
    
    def __init__(self):
        self.path = "/home/tuna/Desktop/Image Processing/Image_Processing/coin_detection.jpg"
        self.image = cv2.imread(self.path)
    
    def morph_segmentation(self):
        down_width = 300
        down_height = 400      
        dimention = (down_width, down_height)

        resized_image = cv2.resize(self.image, dimention, interpolation = cv2.INTER_AREA)

        gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        cv2.imshow("thresh",threshold)

        kernel = np.ones((3, 3), np.uint8)
        closing = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel, iterations = 2)

        background_area = cv2.dilate(closing, kernel, iterations = 1) # Dilation increases object boundary to background.

        dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
        ret, foreground_area = cv2.threshold(dist_transform, 0.02*dist_transform.max(), 255, 0)

        cv2.imshow("Segmentation", foreground_area)

        return foreground_area

if __name__ == "__main__":
    MS = MorphSeg()
    MS.morph_segmentation()

    if cv2.waitKey(0) & 0xFF == ord("x"):
        cv2.destroyAllWindows()