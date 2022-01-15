import cv2
import numpy as np
import matplotlib.pyplot as plt



class ForegroundExtraction:

    def __init__(self):
        self.path = "/home/tuna/Desktop/Image Processing/Image_Processing/foregrd_extrac.jpg"
        self.image = cv2.imread(self.path)
    
    def foreground_extraction(self):
        mask = np.zeros(self.image.shape[:2], np.uint8)
        print(mask.shape)
        cv2.imshow("fa", mask)

        background_model = np.zeros((1,65), np.float64) # np.float64 default
        foreground_model = np.zeros((1,65), np.float64)

        rectangle = (20, 100, 150, 150) # ROI >> where the values are entered as (startingPoint_x, startingPoint_y, width, height)

        cv2.grabCut(self.image, mask, rectangle, background_model, foreground_model, 3, cv2.GC_INIT_WITH_RECT) # cv2.GC_INIT_WITH_RECT is used because of the rectangle mode is used 

        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")

        self.image = self.image * mask2[:, :, np.newaxis]

        plt.imshow(self.image)
        plt.colorbar()
        plt.show()

if __name__ == "__main__":
    fground_extrac = ForegroundExtraction()
    fground_extrac.foreground_extraction()

    if cv2.waitKey(0) & 0xFF == ord("x"):
        cv2.destroyAllWindows()

'''
Syntax: cv2.grabCut(image, mask, rectangle, backgroundModel, foregroundModel, iterationCount[, mode])

Parameters:

image: Input 8-bit 3-channel image.
mask: Input/output 8-bit single-channel mask. The mask is initialized by the function when mode is set to GC_INIT_WITH_RECT. Its elements may have one of following values:
GC_BGD defines an obvious background pixels.
GC_FGD defines an obvious foreground (object) pixel.
GC_PR_BGD defines a possible background pixel.
GC_PR_FGD defines a possible foreground pixel.
rectangle: It is the region of interest containing a segmented object. The pixels outside of the ROI are marked as obvious background. The parameter is only used when mode==GC_INIT_WITH_RECT.
backgroundModel: Temporary array for the background model.
foregroundModel: Temporary array for the foreground model.
iterationCount: Number of iterations the algorithm should make before returning the result. Note that the result can be refined with further calls with mode==GC_INIT_WITH_MASK or mode==GC_EVAL.
mode: It defines the Operation mode. It can be one of the following:
GC_INIT_WITH_RECT: The function initializes the state and the mask using the provided rectangle. After that it runs iterCount iterations of the algorithm.
GC_INIT_WITH_MASK: The function initializes the state using the provided mask. Note that GC_INIT_WITH_RECT and GC_INIT_WITH_MASK can be combined.
Then, all the pixels outside of the ROI are automatically initialized with GC_BGD.
GC_EVAL: The value means that the algorithm should just resume.
'''