import cv2

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 600) # camera görüntüsü boyutunu ayarlama
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 600)


while True:
    ret, video_image = camera.read()
    grey_video_img = cv2.cvtColor(video_image, cv2.COLOR_RGB2GRAY) # görütüyü gri tona çekme
    cv2.imshow("Bilgisayar Kamerasi", video_image)
    cv2.imshow("Gri Tonlamali Bilgisayar Kamerasi", grey_video_img)

    if cv2.waitKey(50) & 0xFF == ord('x'):
        break

camera.release()
cv2.destroyAllWindows()