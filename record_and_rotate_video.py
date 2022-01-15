import cv2


class videoOperations:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        self.video_name = "video_test6.avi"

    def record_camera(self):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        videoRecord = cv2.VideoWriter(self.video_name, fourcc, 9.0, (640, 480))

        while(self.camera.isOpened()):
            ret, computer_cam = self.camera.read()

            if ret == True:
                videoRecord.write(computer_cam)
                cv2.imshow('Recording...', computer_cam)

                if cv2.waitKey(1) & 0xFF == ord('x'):
                    break

        self.camera.release()
        videoRecord.release()
        cv2.destroyAllWindows()

    def rotate_video(self):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        videoRecord = cv2.VideoWriter(self.video_name, fourcc, 9.0, (640, 480))

        while(self.camera.isOpened()):
            ret, computer_cam = self.camera.read()

            if ret == True:
                computer_cam = cv2.flip(computer_cam, 1) # 0: x ekseninde döndürür. 1: y ekseninde döndürür. -1: iki eksende de döndürür.
                videoRecord.write(computer_cam)
                cv2.imshow('Recording...', computer_cam)

                if cv2.waitKey(1) & 0xFF == ord('x'):
                    break

        self.camera.release()
        videoRecord.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    VO = videoOperations()
    #VO.record_camera()
    VO.rotate_video()