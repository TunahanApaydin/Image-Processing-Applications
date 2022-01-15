import cv2

camera = cv2.VideoCapture(0)

def resize(video_image, rate):
    width = int((video_image.shape[1] * rate) / 100)
    height = int((video_image.shape[0] * rate) / 100)
    new_size = (width, height)
    return cv2.resize(video_image, new_size, interpolation= cv2.INTER_AREA)

def set_solubility_1080p():
    camera.set(3, 1920) # 3 genişlik değeri için
    camera.set(4, 1080) # 4 yükseklik değeri için

def set_solubility(width, height):
    camera.set(3, width)
    camera.set(4, height)

#set_solubility_1080p()
set_solubility(1280, 720)

while True:
    ret, video_image = camera.read()
    sized_vid_img = resize(video_image, 30) #Parametre olarak gönderdiğim 30 değeri ile mevcut görüntünün çerçeve boyutunun %30 oranı kadar yeni bir çerçeve boyutu ortaya çıkacaktır.
    cv2.imshow("Kamera Goruntusu", video_image)
    cv2.imshow("Yeniden Boyutlandirilmis Goruntu", sized_vid_img)

    if cv2.waitKey(20) & 0xFF  == ord('x'):
        break

camera.release()
cv2.destroyAllWindows()    