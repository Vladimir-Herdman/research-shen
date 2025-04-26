import time

from main_utils import *


# Create four threads as follows
cam1 = Cameras("Camera1", 0)
cam2 = Cameras("Camera2", 0)
cam3 = Cameras("Camera3", 0)
cam4 = Cameras("Camera4", 0)
time.sleep(2)
Cameras.check_cams()


frame_width = 320
frame_height = 240
cam_set = [cam1, cam2, cam3, cam4]
key = ord('a')
count = 1
while (key != ord('q')):
    for instance in cam_set:
        ret, frame = instance.cap.read()
        if ret:
            frame = cv2.resize(frame, (frame_width, frame_height))
            path = str(images_dir / (instance.previewName + "_" + str(count) + ".jpeg"))
            cv2.imwrite(path, frame)
    count += 1
    key = cv2.waitKey(2) & 0xFF
