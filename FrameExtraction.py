import cv2

class FrameExtraction:
    def __init__(self):
        self.path = "/home/tuna/Desktop/Image Processing/project/solidWhiteRight.mp4"
    
    def frame_capture(self):
        video = cv2.VideoCapture(self.path)
        count = 0

        while True:
            ret, frame = video.read()
            if ret == True:
                cv2.imwrite("/home/tuna/Desktop/Image Processing/Image_Processing/test_frames/frame%d.jpg" % count, frame)
                count += 1
            else:
                break
        

if __name__ == "__main__":
    fe = FrameExtraction()
    fe.frame_capture()
