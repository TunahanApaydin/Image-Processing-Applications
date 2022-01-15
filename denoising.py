import cv2
import numpy as np

class denoising:

    def __init__(self):
        self.path = "/home/tuna/Desktop/Image Processing/Image_Processing/lena_noisy_img.jpeg"

    def denoising(self):
        image = cv2.imread(self.path)

        img = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 55)

        cv2.imshow("Denoising", np.hstack((image, img)))

        '''
        Syntax: cv2.fastNlMeansDenoisingColored( P1, P2, float P3, float P4, int P5, int P6)
        Parameters:
        P1 – Source Image Array
        P2 – Destination Image Array
        P3 – Size in pixels of the template patch that is used to compute weights.
        P4 – Size in pixels of the window that is used to compute a weighted average for the given pixel.
        P5 – Parameter regulating filter strength for luminance component.
        P6 – Same as above but for color components // Not used in a grayscale image.
        '''

if __name__ == "__main__":
    d = denoising()
    d.denoising()

    if cv2.waitKey(0) & 0xFF == ord("x"):
        cv2.destroyAllWindows()