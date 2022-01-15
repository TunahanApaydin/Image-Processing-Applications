import cv2
import sys

class DotDetection:

    def __init__(self):
        self.path = "/home/tuna/Desktop/Image Processing/Image_Processing/1.jpg"
        self.image = cv2.imread(self.path, 0) # grayscale formatta imge okuma
    
    def count_black_dot(self):
        ret, threshold = cv2.threshold(self.image, 100, 255, cv2.THRESH_BINARY, cv2.THRESH_OTSU) # cv2.THRESH_BINARY >> beyaz nokta saymak için. cv2.THRESH_BINARY_INV >> siyah nokta saymak için
        cv2.imshow("threshold", threshold)

        contours = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[-2]
        maxx = 0
        minn = sys.float_info.max
        xcontours = []

        for cnt in contours:
            inp = cv2.contourArea(cnt)
            if inp > maxx:
                 maxx = inp         
            if inp < minn:
                 minn = inp
        print("max: {} min: {}".format(maxx, minn))

        for cnt in contours:
            if minn <= cv2.contourArea(cnt) and cv2.contourArea(cnt) <= maxx:
                xcontours.append(cnt)
        
        print("number of dots: {}".format(len(xcontours)))


if __name__  == "__main__":
    dot_det = DotDetection()
    dot_det.count_black_dot()

    if cv2.waitKey(0) & 0xFF == ord("x"):
        cv2.destroyAllWindows()
