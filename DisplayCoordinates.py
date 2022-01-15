import cv2

class DisplayCoordinates:
    def __init__(self):
        self.path = "/home/tuna/Desktop/Image Processing/Image_Processing/lena.png"
        self.image = cv2.imread(self.path, 1)
        #cv2.imshow("image", self.image)
    
    def resize_image(self):
        print(self.image.shape) # imgenin shape'ini göster

        scale_percent = 300
        width = int(self.image.shape[1] * scale_percent / 100)
        height = int(self.image.shape[0] * scale_percent / 100)
        dimention = (width, height)

        resized_image = cv2.resize(self.image, dimention, interpolation = cv2.INTER_AREA)
        #cv2.imshow("resized image", self.resized_image)

        return resized_image
    
    def click_event(self, event, x, y, flags, params):
        if event ==  cv2.EVENT_LBUTTONDOWN: # sol click yapıldı mı?
            print(x, " ", y) # koordinatları gösterme

            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(resized_image, str(x) + ',' + str(y), (x,y), font, 1, (255, 0, 0), 2) # imge üzerine yazı ekleme
            cv2.imshow("resized image", resized_image)

        if event == cv2.EVENT_RBUTTONDOWN:
            print(x, " ", y)

            font = cv2.FONT_HERSHEY_COMPLEX

            b = resized_image[y, x, 0]
            g = resized_image[y, x, 1]
            r = resized_image[y, x, 2]

            cv2.putText(resized_image, str(b) + "," + str(g) + "," + str(r), (x,y), font, 1, (int(r), int(g), int(b)), 2)
            cv2.imshow("resized image", resized_image)

if __name__ == "__main__":
    dc = DisplayCoordinates()
    resized_image = dc.resize_image()
    cv2.imshow("resized image", resized_image)

    cv2.namedWindow("resized image", cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback("resized image", dc.click_event)

    if cv2.waitKey(0) & 0xFF == ord("x"):
        cv2.destroyAllWindows()