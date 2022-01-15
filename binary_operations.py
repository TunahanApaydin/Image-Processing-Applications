import cv2
import numpy as np

class binary_operations:

    def __init__(self):
        self.path_1 = "/home/tuna/Desktop/Image Processing/Image_Processing/binary_input_1.png"
        self.path_2 = "/home/tuna/Desktop/Image Processing/Image_Processing/binary_input_2.png"
        self.input_img_1 = cv2.imread(self.path_1)
        self.input_img_2 = cv2.imread(self.path_2)
        self.resize_img = cv2.resize(self.input_img_1, (490, 383))

    def binary_and(self):
        dest_and = cv2.bitwise_and(self.resize_img, self.input_img_2, mask = None)
        cv2.imshow("resized input 1", self.resize_img)
        cv2.imshow("input 2", self.input_img_2)
        cv2.imshow("Bitwise And", dest_and)
    
    def binary_or(self):
        dest_or = cv2.bitwise_or(self.resize_img, self.input_img_2, mask = None)
        cv2.imshow("resized input 1", self.resize_img)
        cv2.imshow("input 2", self.input_img_2)
        cv2.imshow("Bitwise Or", dest_or)
    
    def binary_xor(self):
        dest_xor = cv2.bitwise_xor(self.resize_img, self.input_img_2, mask = None)
        cv2.imshow("resized input 1", self.resize_img)
        cv2.imshow("input 2", self.input_img_2)
        cv2.imshow("Bitwise Xor", dest_xor)
    
    def bitwise_not(self):
        dest_not_1 = cv2.bitwise_not(self.resize_img, mask = None)
        dest_not_2 = cv2.bitwise_not(self.input_img_2, mask = None)
        cv2.imshow("resized input 1", self.resize_img)
        cv2.imshow("input 2", self.input_img_2)
        cv2.imshow("Bitwise Not 1", dest_not_1)
        cv2.imshow("Bitwise Not 2", dest_not_2)


if __name__ == "__main__":
    BO = binary_operations()
    #BO.binary_and()
    #BO.binary_or()
    #BO.binary_xor()
    BO.bitwise_not()

    if cv2.waitKey(0) & 0xFF == ord("x"):
            cv2.destroyAllWindows()