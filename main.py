import time

from main_utils import *


# Create four threads as follows
cam1 = Cameras("Camera1", 0)
cam2 = Cameras("Camera2", 0)
cam3 = Cameras("Camera3", 0)
cam4 = Cameras("Camera4", 0)
time.sleep(3)
Cameras.check_cams()


#frame_width = 320
#frame_height = 240
#thread_list = [thread1, thread2, thread3, thread4]
#key = ord('a')
#while (key != ord('q')):
#    for instance in thread_list:
#        ret, frame = instance.cap.read()
#        if ret:
#            frame = cv2.resize(frame, (frame_width, frame_height))
#            cv2.imwrite("test.jpeg", frame)
#            cv2.imshow(instance.previewName, frame)
#    key = cv2.waitKey(2) & 0xFF


for x in range(0, 1005, 67):
    #take picture
    if (os.name != "posix"): #REMOVE: here for mac testing
        subprocess.run(["ticcmd", "--position-relative", f"{x}", "--resume"])
    if x >= 201:
        cam1.takePicture()
        cam2.takePicture()
        cam3.takePicture()
        cam4.takePicture()
    print(f"Position: {x}")
