import cv2
import os
import random
import string
import datetime


def random_str(num):
    dat = string.digits + string.ascii_lowercase + string.ascii_uppercase
    return ''.join([random.choice(dat) for i in range(num)])


def save_frame_camera_cycle(dir_path, cycle):
    ext = 'jpg'
    delay = 1
    window_name = 'get_training_data (demo)'
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path)

    n = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
        if n == cycle:
            n = 0
            cv2.imwrite('{}{}_{}.{}'.format(base_path, datetime.datetime.now().strftime('%m%df'), random_str(5), ext), frame)
        n += 1

    cv2.destroyWindow(window_name)


if __name__ == "__main__":
    save_frame_camera_cycle('datasets/example/', 30)
