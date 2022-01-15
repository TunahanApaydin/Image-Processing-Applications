import cv2

def save_image(path, image, jpg_quality = None, png_compress = None):
    if jpg_quality:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
    elif png_compress:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compress])
    else:
        cv2.imwrite(path, image)

def main():
    path = "/home/tuna/Desktop/Ko-Drive/Python_Calismalar/Image_Processing/flower.jpeg"
    image = cv2.imread(path)
    cv2.imshow("Flower", image)

    last_jpg_path = "/home/tuna/Desktop/Ko-Drive/Python_Calismalar/Image_Processing/flowerJpg.jpg"
    save_image(last_jpg_path, image, jpg_quality = 6)

    last_png_path = "/home/tuna/Desktop/Ko-Drive/Python_Calismalar/Image_Processing/flowerPng.png"
    save_image(last_png_path, image, png_compress = 9)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()