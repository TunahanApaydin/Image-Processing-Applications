import cv2

image = cv2.imread("/home/tuna/Desktop/Ko-Drive/Python_Calismalar/Image_Processing/flower.jpeg") # '0' imgeyi gri tona çeker.
cv2.imshow("flower", image) # imgeyi gösterir.
#cv2.imwrite("flower_gray.jpeg", image) # imgeyi kaydeder.

height = image.shape[0]
width = image.shape[1]

print("Pİcture height:", height)
print("Picture width:", width)

cv2.waitKey(0)
cv2.destroyAllWindows() 