import cv2
import numpy as np

class FCC:
    def __init__(self):
        self.path = "/home/tuna/Desktop/Image Processing/Image_Processing/contour.jpg"
        self.image = cv2.imread(self.path, cv2.IMREAD_COLOR)
        cv2.imshow("color", self.image)
        self.font = cv2.FONT_HERSHEY_COMPLEX
    
    def find_contours(self):
        grayscale_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray", grayscale_img)

        _, threshold = cv2.threshold(grayscale_img, 110, 255, cv2.THRESH_BINARY)

        contours, _= cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # 3 kanallı imge ile çalışmaz.

        return contours
    
    def find_coordinates(self, contours):
        for cnt in contours:                                                       # cv2.approxPolyDP >> Belirtilen hassasiyetle bir çokgen eğriye/eğrilere yaklaştırır.
            approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) # cv2.arcLength >> Bir kontur çevresini veya bir eğri uzunluğunu hesaplar.
            cv2.drawContours(self.image, [approx], 0, (0, 0, 255), 5)

            n = approx.ravel()
            i = 0

            for j in n:
                if i % 2 == 0:
                    x = n[i]
                    y = n[i + 1]
                    coordinates = str(x) + "," + str(y)

                    if i == 0:
                        cv2.putText(self.image, "Arrow tip", (x, y), self.font, 0.5, (255, 0, 0))
                    else:
                        cv2.putText(self.image, coordinates, (x, y), self.font, 0.5, (0, 255, 0))
                i = i +1
        cv2.imshow("final img", self.image)

if __name__ == "__main__":
    fcc = FCC()
    contours = fcc.find_contours()
    fcc.find_coordinates(contours)

    if cv2.waitKey(0) & 0xFF == ord("x"):
        cv2.destroyAllWindows()