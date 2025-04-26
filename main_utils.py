import os
import pathlib
import sys

import cv2


images_dir = pathlib.Path(__file__.split("main_utils.py")[0]) / "images"
# Define classes
class Cameras():
    cam_list = list()
    images_dir = pathlib.Path(__file__.split("main_utils.py")[0]) / "images"
    all_dirs_in_split = [dir for dir in next(os.walk(images_dir))[1] if dir[0] != "."]

    def __init__(self, previewName, camID):
        # instance variables
        self.previewName = previewName
        self.camID = camID
        self.cap = cv2.VideoCapture(self.camID)
        self.img_count = 1

        # append cam to class list of cams
        Cameras.cam_list.append(self.cap)

    def __del__(self):
        """Essentially desctructor, cleanup all resources"""
        self.cap.release()

    def run(self):
        print ("Starting " + self.previewName+"\n")
        self.camPreview()

    def takePicture(self):
        _, frame = self.cap.read()
        image_path = str(Cameras.images_dir / f"{self.previewName}_{self.img_count}.jpeg")
        cv2.imwrite(image_path, frame)
        self.img_count += 1

    def camPreview(self):
        cv2.namedWindow(self.previewName)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        rval, frame = self.cap.read()

        while rval:
            cv2.imshow(self.previewName, frame)
            rval, frame = self.cap.read()
            key = cv2.waitKey(20)
            if key == 27:  # exit on ESC
                break
        cv2.destroyWindow(self.previewName)

    @classmethod
    def check_cams(cls):
        """Check all cameras to make sure they're working"""
        for count, cam in enumerate(cls.cam_list, 1):
            try:
                ret, _ = cam.read()
                if not ret:
                    raise Exception(f"Camera{count} had an issue getting the cam to read")
            except Exception as e:
                print(e)
