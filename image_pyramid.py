import cv2

path = "/home/tuna/Desktop/Ko-Drive/Python_Calismalar/Image_Processing/flower.jpeg"
image = cv2.imread(path)
pyramir_upper_level = cv2.pyrUp(image)
pyramir_lover_level = cv2.pyrDown(image)

cv2.imshow("Piramit ornek resim", image)
#cv2.imshow("Piramit ust seviye", pyramir_upper_level)
#cv2.imshow("Piramit alt seviye", pyramir_lover_level)

cv2.rectangle(image, (50, 30), (100, 120), (125, 40, 30), 3)
cv2.line(image, (50,30), (100, 120), (145, 248, 75), 5)
cv2.circle(image, (75, 75), 20, (0, 0, 150), 5)
cv2.putText(image, "d-d-c", (50, 130), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255), 2, cv2.LINE_4)
cv2.imshow("Dortgen, daire ve cizgi eklenmis resim", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
