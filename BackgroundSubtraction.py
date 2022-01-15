import cv2
import numpy as np

class BackgroundSubtraction:

    def __init__(self):
        self.path = "/home/tuna/Desktop/Image Processing/Image_Processing/otostop.mp4"
        self.capture = cv2.VideoCapture(0)
        self.capture2 = cv2.VideoCapture(self.path)
    
    def running_avarage(self):
        ret, image = self.capture.read()
        avarage_value = np.float32(image)

        while True:
            ret, image = self.capture.read()
            #cv2.imshow("Original", image)
            '''
            src: The source image. The image can be colored or grayscaled image and either 8-bit or 32-bit floating point.
            dst: The accumulator or the destination image. It is either 32-bit or 64-bit floating point.
            Note: It should have the same channels as that of the source image. Also, the value of dst should be predeclared initially.
            alpha: Weight of the input image. Alpha decides the speed of updating. If you set a lower value for this variable,
            running average will be performed over a larger amount of previous frames and vice-versa.
            '''
            if ret == True:
                cv2.accumulateWeighted(image, avarage_value, 0.02)
                result_frames = cv2.convertScaleAbs(avarage_value) # converting the matrix elements to absolute values and converting the result to 8-bit.

                cv2.imshow("Original", image)
                cv2.imshow("avarage value", result_frames)

            if cv2.waitKey(10) & 0xFF == ord("x"):
                self.capture.release()
                cv2.destroyAllWindows()

    def background_subtractor(self):
        
        fgbg = cv2.createBackgroundSubtractorMOG2()
        
        while(1):
            ret, frame = self.capture2.read()
            if ret == True:
                fgmask = fgbg.apply(frame)
            
                cv2.imshow('fgmask', fgmask)
                cv2.imshow('frame',frame )
            
            if cv2.waitKey(10) & 0xFF == ord("x"):
                self.capture2.release()
                cv2.destroyAllWindows()

if __name__ == "__main__":
    back_sub = BackgroundSubtraction()
    #back_sub.running_avarage()
    back_sub.background_subtractor()

    
