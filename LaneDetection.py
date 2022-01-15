import cv2
import numpy as np
import matplotlib.pyplot as plt

class LaneDetection:

    def __init__(self):
        self.path = "/home/tuna/Desktop/Image Processing/Image_Processing/solidWhiteCurve.jpg"
        self.videopath = "/home/tuna/Desktop/Image Processing/Image_Processing/solidWhiteRight.mp4"
        self.image = cv2.imread(self.path)
        #print(self.image.shape) # (540, 960, 3)
        cv2.imshow("original", self.image)

    def Canny(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        canny = cv2.Canny(blur, 50, 150)
        #cv2.imshow("canny", canny)
        return canny
    
    def region_of_interest(self, image):
        height = image.shape[0]
        polygons = np.array([[(100, height), (930, height), (490, 300)]])
        mask = np.zeros_like(image)
        cv2.fillPoly(mask, polygons, 255)
        masked_region = cv2.bitwise_and(image, mask)
        #cv2.imshow("roi",masked_region)
        return masked_region
    
    def make_coordinates(self, image, line_parameters):
        slope, intercept = line_parameters
        y1 = image.shape[0] # Define the height of the lines (the same for both left and right)
        y2 = int(y1*(3/5)) # ?
        x1 = int((y1-intercept)/slope) # Calculate x coordinates by rearranging the equation of a line, from y=mx+b to x = (y-b) / m
        x2 = int((y2-intercept)/slope)

        return np.array([x1,y1,x2,y2])
    
    def average_slope_intercept(self, image, lines):
        left_fit = []
        right_fit = []
        
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            parameters = np.polyfit((x1,x2), (y1,y2), 1)
            
            slope = parameters[0]
            intercept = parameters[1]
            
            if slope < 0:
                left_fit.append((slope, intercept))
            elif slope >= 0:
                right_fit.append((slope, intercept))
                
        left_fit_average = np.average(left_fit, axis=0)
        right_fit_average = np.average(right_fit, axis=0)
            
        left_line = self.make_coordinates(image, left_fit_average)
        right_line = self.make_coordinates(image, right_fit_average)
            
        return np.array([left_line, right_line])

    def display_lines(self, image, lines):
        line_img = np.zeros_like(image)
        #print(lines)
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)
                cv2.line(line_img, (x1, y1), (x2, y2), (255, 0, 0), 10)
        
        return line_img

if __name__ == "__main__":
    LaneD = LaneDetection()

    capture = cv2.VideoCapture(LaneD.videopath)

    while capture.isOpened():
        ret, frame = capture.read()
        #lane_image = np.copy(LaneD.image)
        if ret == True:
            lane_image = np.copy(frame)

            canny_img = LaneD.Canny(lane_image)
            cropped_img = LaneD.region_of_interest(canny_img)

            lines = cv2.HoughLinesP(
                                    cropped_img, # The isolated gradients
                                    rho = 6, # Defining the bin size, 6 is the value for rho
                                    theta = np.pi / 60, # np.pi/180 is the value for theta
                                    threshold = 100, # 160 = min vote, Minimum intersections needed per bin to be considered a line
                                    lines = np.array([]), # Placeholder array
                                    minLineLength = 40, #  Minimum Line length
                                    maxLineGap = 25) # Maximum Line gap
            # lines = cv2.HoughLinesP(cropped_img, 2, np.pi/180, 100, np.array([]), 40, 5)

            averaged_lines = LaneD.average_slope_intercept(lane_image, lines)
            line_img = LaneD.display_lines(lane_image, averaged_lines)
            combo_image = cv2.addWeighted(lane_image, 0.8, line_img, 1, 1)

            cv2.imshow("combo",combo_image)

        if cv2.waitKey(10) & 0xFF == ord("x"):
            capture.release()
            cv2.destroyAllWindows()
