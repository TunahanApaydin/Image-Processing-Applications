import cv2
import numpy as np

path = "/home/tuna/Desktop/Image Processing/Image_Processing/eroding.png"

img = cv2.imread(path)

kernel = np.ones((5, 5), np.uint8)
kernel2 = np.ones((6, 6), np.uint8)

image = cv2.erode(img, kernel)
image2 = cv2.erode(img, kernel2, cv2.BORDER_REFLECT)

cv2.imshow("Original Image", img)
cv2.imshow("Eroded, Image", image)
cv2.imshow("Eroded Image 2", image2)

if cv2.waitKey(0) & 0xFF == ord("x"):
    cv2.destroyAllWindows()