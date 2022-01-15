import cv2
import numpy as np
import matplotlib.pyplot as plt

class histogram:

    def __init__(self):
        self.path = "/home/tuna/Desktop/Image Processing/Image_Processing/flower.jpeg"

    def histogram(self):
        img = cv2.imread(self.path, 0)
        hist = cv2.calcHist([img], [0], None, [256], [0, 256]) # (image, channel, mask, histSize, ranges)
        plt.plot(hist)
        plt.show()
        '''
        images : it is the source image of type uint8 or float32 represented as “[img]”.
        channels : it is the index of channel for which we calculate histogram. For grayscale image, its value is [0] and
        color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
        mask : mask image. To find histogram of full image, it is given as “None”.
        histSize : this represents our BIN count. For full scale, we pass [256].
        ranges : this is our RANGE. Normally, it is [0,256].
        '''

    def equalize_histogram(self):
        img = cv2.imread(self.path, 0) #Bu ayarlama sayesinde, yoğunluklar histogram üzerinde daha iyi dağıtılabilir.
        equ = cv2.equalizeHist(img) #Bu, daha düşük yerel kontrastlı alanların daha yüksek bir kontrast kazanmasına izin verir.
        cv2.imshow("Equalize Histogram", np.hstack((img, equ)))

if __name__ == "__main__":
    h = histogram()
    #h.histogram()
    h.equalize_histogram()

    if cv2.waitKey(0) & 0xFF == ord("x"):
        cv2.destroyAllWindows()