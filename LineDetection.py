import cv2
import numpy as np

class LineDetection:

    def __init__(self):
        self.path = "/home/tuna/Desktop/Image Processing/Image_Processing/straight_lines.jpg"
        self.image = cv2.imread(self.path)
    
    def hough_line_detection(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 150, apertureSize = 3)
        lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

        for r, theta in lines[:,0]: # ?
            cost = np.cos(theta)
            sint = np.sin(theta)

            rcost = cost * r
            rsint = sint * r

            x1 = int(rcost - 1000 * sint) # (rcos(theta)-1000sin(theta))
            y1 = int(rsint + 1000 * cost) # (rsin(theta)+1000cos(theta))

            x2 = int(rcost + 1000 * sint) # (rcos(theta)+1000sin(theta))
            y2 = int(rsint - 1000 * cost) # (rsin(theta)-1000cos(theta))

            cv2.line(self.image, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.imshow("lines", self.image)


if __name__ == "__main__":
    LD = LineDetection()
    LD.hough_line_detection()

    if cv2.waitKey(0) & 0xFF == ord("x"):
        cv2.destroyAllWindows()