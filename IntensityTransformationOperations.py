import cv2
import numpy as np

class IntensityTransOpe:

    def __init__(self):
        self.path = "/home/tuna/Desktop/Image Processing/Image_Processing/IntensityTranOpe.jpg"
        self.image = cv2.imread(self.path)
        cv2.imshow("original image", self.image)

    def log_transformations(self):
        c = 255/(np.log(1 + np.max(self.image))) # c = 255/(log (1 + m)) , c is a scaling constant and m is the maximum pixel value in the image.
        log_transformed = c * np.log(1+ self.image) # s = clog(1+r) Here, s is the output intensity, r>=0 is the input intensity of the pixel.
        log_transformed = np.array(log_transformed, dtype = np.uint8)

        cv2.imshow("transformed image", log_transformed)
    
    def power_law_transformation(self): # Power-Law (Gamma) Transformation
        for gamma in [0.1, 0.5, 1.2, 2.2]:
            gamma_corrected = np.array(255 * (self.image / 255) ** gamma, dtype = "uint8")

            cv2.imshow("Gamma Transformated" + str(gamma) + ".jpg", gamma_corrected)
    
    def piecewise_linear_transformation(self):
        pass


if __name__ == "__main__":
    InTrOp = IntensityTransOpe()
    #InTrOp.log_transformations()
    InTrOp.power_law_transformation()

    if cv2.waitKey(0) & 0xFF == ord("x"):
        cv2.destroyAllWindows()