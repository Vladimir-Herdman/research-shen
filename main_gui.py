import subprocess
import threading
import time
from warnings import deprecated

import customtkinter
from PIL import Image

from main_utils import *


customtkinter.set_appearance_mode("light")


class MyTitleShowerFrame(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(self, text=title, fg_color="gray70", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.file_name = customtkinter.CTkLabel(self, text=f"Tester title")
        self.file_name.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.save_location = customtkinter.CTkLabel(self, text=f"{Cameras.images_dir}{self.file_name.cget('text')}")
        self.save_location.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew")

    def set_name(self, test_name="NONE", brightness_values: list[str]=["NONE", "NONE"], extra_entry="NONE"):
        if (brightness_values[0] == ""): brightness_values = ["NONE", brightness_values[1]]
        if (brightness_values[1] == ""): brightness_values = [brightness_values[0], "NONE"]
        if (test_name == ""): test_name = "NONE"
        if (extra_entry == ""): extra_entry = "NONE"
        name = ""
        if ("Brightness" in test_name):
            if ("Artificial" in test_name):
                print(repr(brightness_values[0]), repr(brightness_values[1]))
                print(repr(brightness_values))
                for item in brightness_values: print(item)
                print(type(brightness_values))
                name = f"A-Brightness({brightness_values[0]},{brightness_values[1]})"
            else:
                name = f"P-Brightness({extra_entry})"
            self.update_names(name)
            return
        elif ("Angle" in test_name):
            name = f"Angle-{extra_entry}"
            self.update_names(name)
        elif ("Distance" in test_name):
            name = f"Distance-{extra_entry}"
            self.update_names(name)
        elif ("Background" in test_name):
            name = f"Background-{extra_entry}"
            self.update_names(name)
        else:
            name = f"{extra_entry}"
            self.update_names(name)

    def update_names(self, name):
        self.file_name.configure(text=name)
        self.save_location.configure(text=f"{Cameras.images_dir}\{name}")

#@deprecated("No longer in use, just an example to how to use customtkinter inheritance")
#class MyRadiobuttonFrame(customtkinter.CTkFrame):
#    def __init__(self, master, title, values):
#        super().__init__(master)
#        self.grid_columnconfigure(0, weight=1)
#        self.values = values
#        self.title = title
#        self.radiobuttons = []
#        self.variable = customtkinter.StringVar(value="Custom")
#
#        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray70", corner_radius=6)
#        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
#
#        for i, value in enumerate(self.values):
#            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
#            radiobutton.grid(row=i + 1, column=0, padx=10, pady=10, sticky="w")
#            self.radiobuttons.append(radiobutton)
#
#    def get(self):
#        return self.variable.get()

#@deprecated("No longer in use, just an example to how to use customtkinter inheritance")
#class MyDoubleRadiobuttonFrame(customtkinter.CTkFrame):
#    def __init__(self, master, title, leftvalues, rightvalues, custom: bool):
#        super().__init__(master)
#        self.grid_columnconfigure(0, weight=1)
#        self.custom = custom
#        if not custom:
#            self.leftvalues = leftvalues
#            self.rightvalues = rightvalues
#            self.title = title
#            self.leftradiobuttons = []
#            self.rightradiobuttons = []
#            self.leftvariable = customtkinter.StringVar(value="")
#            self.rightvariable = customtkinter.StringVar(value="")
#
#            self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray70", corner_radius=6)
#            self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)
#
#            for i, value in enumerate(self.leftvalues):
#                radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.leftvariable)
#                radiobutton.grid(row=i + 1, column=0, padx=10, pady=10, sticky="w")
#                self.leftradiobuttons.append(radiobutton)
#
#            for i, value in enumerate(self.rightvalues):
#                radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.rightvariable)
#                radiobutton.grid(row=i + 1, column=1, padx=(10, 200), pady=10, sticky="w")
#                self.rightradiobuttons.append(radiobutton)
#        else:
#            self.title = title
#            self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray70", corner_radius=6)
#            self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)
#            self.variable_one = customtkinter.StringVar(value="Brightness one")
#            self.variable_two = customtkinter.StringVar(value="Brightness two")
#
#            self.entry_one = customtkinter.CTkEntry(self, height=28, placeholder_text="Brightness one", textvariable=self.variable_one)
#            self.entry_one.grid(row=1, column=0, padx=(20, 10), pady=10, sticky='w')
#
#            self.entry_two = customtkinter.CTkEntry(self, height=28, placeholder_text="Brightness two", textvariable=self.variable_two)
#            self.entry_two.grid(row=1, column=1, padx=(20, 10), pady=10, sticky='w')
#
#    def get(self) -> list[str]:
#        if not self.custom:
#            return str((self.leftvariable.get(), self.rightvariable.get()))
#        else:
#            return [self.variable_one.get(), self.variable_two.get()]

class MyEntryFrame(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray70", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.entry = customtkinter.CTkEntry(self, height=28, placeholder_text="Custom name", textvariable=self.variable)
        self.entry.grid(row=1, column=0, padx=100, pady=10, sticky='we', columnspan=2)

    def get(self):
        return self.variable.get()

    def get_entry(self):
        return self.entry

class MyCamerasPreviewFrame(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.title = title

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray70", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)

        cam_a_label = customtkinter.CTkLabel(self, text="cam_a", fg_color="gray70", corner_radius=6)
        cam_a_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.cam_a = customtkinter.CTkLabel(self, text="", height=150, fg_color="gray70", corner_radius=6)
        self.cam_a.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew")

        #cam_b_label = customtkinter.CTkLabel(self, text="cam_b", fg_color="gray70", corner_radius=6)
        #cam_b_label.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="ew")
        #self.cam_b = customtkinter.CTkLabel(self, text="", height=150, fg_color="gray70", corner_radius=6)
        #self.cam_b.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="ew")

        #cam_c_label = customtkinter.CTkLabel(self, text="cam_c", fg_color="gray70", corner_radius=6)
        #cam_c_label.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="ew")
        #self.cam_c = customtkinter.CTkLabel(self, text="", height=150, fg_color="gray70", corner_radius=6)
        #self.cam_c.grid(row=4, column=0, padx=10, pady=(10, 10), sticky="ew")

        #cam_d_label = customtkinter.CTkLabel(self, text="cam_d", fg_color="gray70", corner_radius=6)
        #cam_d_label.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="ew")
        #self.cam_d = customtkinter.CTkLabel(self, text="", height=150, fg_color="gray70", corner_radius=6)
        #self.cam_d.grid(row=4, column=1, padx=10, pady=(10, 10), sticky="ew")

    def set_images(self, a: str):
        img_a = Image.open(a)
        ctk_img_a = customtkinter.CTkImage(light_image=img_a, dark_image=img_a, size=(200, 150))

        #img_b = Image.open(b)
        #ctk_img_b = customtkinter.CTkImage(light_image=img_b, dark_image=img_b, size=(200, 150))

        #img_c = Image.open(c)
        #ctk_img_c = customtkinter.CTkImage(light_image=img_c, dark_image=img_c, size=(200, 150))

        #img_d = Image.open(d)
        #ctk_img_d = customtkinter.CTkImage(light_image=img_d, dark_image=img_d, size=(200, 150))

        self.cam_a.configure(image=ctk_img_a)
        #self.cam_b.configure(image=ctk_img_b)
        #self.cam_c.configure(image=ctk_img_c)
        #self.cam_d.configure(image=ctk_img_d)

class MyLoadingFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=465, height=400)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.loading = True
        self.loading_main = "Connecting to cameras"
        self.loading_dots = "."

        self.title = customtkinter.CTkLabel(self, text=f"{self.loading_main}{self.loading_dots}", font=("Arial", 24), fg_color="gray70", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nesw", columnspan=2)

        threading.Thread(target=self.update_loading, daemon=True).start()
        #self.after_idle(lambda: threading.Thread(target=self.connect_cams, daemon=True).start())

    def set(self, new_text: str):
        self.title.configure(text=new_text)

    def update_loading(self):
        while (self.loading):
            if (len(self.loading_dots) >= 4):
                self.loading_dots = "."

            self.title.configure(text=f"{self.loading_main}{self.loading_dots}")
            self.loading_dots += "."

            time.sleep(0.5)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        overall_colspan = 2

        self.title("Run Hand Scanner Application")
        self.geometry("1400x460")
        self.grid_columnconfigure([0, 1, 3], weight=1)
        self.grid_rowconfigure(0, weight=1)

        #self.brightness = MyDoubleRadiobuttonFrame(self, "Brightness values", 
        #    leftvalues=["40", "50", "60", "70"], 
        #    rightvalues=["20", "30", "40", "50"], 
        #    custom=True)
        #self.brightness.grid(row=2, column=0, padx=(0, 10), pady=(10, 0), sticky="nesw", columnspan=overall_colspan)

        #self.test_name = MyRadiobuttonFrame(self, "Test Name", 
        #    values=["Artificial Brightness", "Physical Brightness", "Camera Angle", "Distance", "Background", "Custom"])
        #self.test_name.grid(row=1, column=0, padx=(0, 10), pady=(10, 0), sticky="nesw", columnspan=overall_colspan)

        self.preview_cameras = MyCamerasPreviewFrame(self, "Preview Cameras")
        self.preview_cameras.grid(row = 3, column=3, padx=(0, 10), pady=(10, 0), sticky="nesw", columnspan=overall_colspan, rowspan=4)

        self.loading_cams_frame = MyLoadingFrame(self)
        self.loading_cams_frame.grid(row = 3, column=3, padx=(0, 10), pady=(10, 0), sticky="nesw", columnspan=overall_colspan, rowspan=4)

        self.extra_entry = MyEntryFrame(self, "Test Name")
        self.extra_entry.grid(row=3, column=0, padx=(0, 10), pady=(10, 0), sticky="nesw", columnspan=overall_colspan)

        self.show_title = MyTitleShowerFrame(self, "Current title and save location")
        self.show_title.grid(row=4, column=0, padx=(0, 10), pady=(10, 0), sticky="nesw", columnspan=overall_colspan)

        self.run_button = customtkinter.CTkButton(self, text="Run Program", command=self.run_button_func, corner_radius=35, height=100, width=70, fg_color="#0f7d21", hover_color="darkgreen")
        self.run_button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

        self.preview_button = customtkinter.CTkButton(self, text="Preview", command=self.preview_cameras_func, corner_radius=35, height=100, width=70, fg_color="#6564aa", hover_color="darkblue")
        self.preview_button.grid(row=5, column=1, padx=10, pady=10, sticky="we")

        self.quit_button = customtkinter.CTkButton(self, text="Quit Program", command=self.quit_button_func, corner_radius=35, height=100, width=70, fg_color="red", hover_color="darkred")
        self.quit_button.grid(row=6, column=0, padx=10, pady=10, sticky="sew", columnspan=overall_colspan)

        self.bind("<Button-1>", self.change_save_name)
        self.extra_entry.get_entry().bind("<KeyRelease>", self.change_save_name)

        self.focus_force(); self.change_save_name()
        self.bind("<q>", lambda event: self.quit_button_func())
        self.protocol("WM_DELETE_WINDOW", self.quit_button_func)

        #TODO: print connecting to ui here where images would go
        self.after_idle(lambda: threading.Thread(target=self.connect_cams, daemon=True).start())

    def change_save_name(self, *args):
        #self.show_title.set_name(test_name=self.test_name.get(), brightness_values=self.brightness.get(), extra_entry=self.extra_entry.get())
        self.show_title.set_name(extra_entry=self.extra_entry.get())

    def connect_cams(self):
        try:
            self.cam1 = Cameras("Camera1", 2) #TODO: replace with proper numbers
            #self.cam2 = Cameras("Camera2", 2) #
            #self.cam3 = Cameras("Camera3", 3) #
            #self.cam4 = Cameras("Camera4", 4) #
            time.sleep(3)
            Cameras.check_cams()
        except Exception:
            pass

        if(self.cam1.cap.isOpened()):
            self.loading_cams_frame.loading = False
            self.loading_cams_frame.title.configure(fg_color="#33cc33", text="Connected")
            time.sleep(1)
            self.preview_cameras_func()
        else:
            self.loading_cams_frame.loading = False
            self.loading_cams_frame.title.configure(fg_color="#c23427", text="Failure connecting to cameras")

    def run_button_func(self):
        distance = 3460
        step_by = 64
        try:
            for x in range(0, distance, step_by):
                #take picture
                if (os.name != "posix"): #REMOVE: here for mac testing
                    subprocess.run(["ticcmd", "--position-relative", f"{x}", "--resume"])
                if x >= 201:
                    self.cam1.takePicture()
                    #self.cam2.takePicture()
                    #self.cam3.takePicture()
                    #self.cam4.takePicture()
                print(f"Position: {x}")
        except Exception as e:
            print(e)
        # Send back to start
        try:
            for x in range(0, distance, step_by):
                #take picture
                if (os.name != "posix"): #REMOVE: here for mac testing
                    subprocess.run(["ticcmd", "--position-relative", f"{-x}", "--resume"])
                if x >= 201:
                    self.cam1.takePicture()
                    #self.cam2.takePicture()
                    #self.cam3.takePicture()
                    #self.cam4.takePicture()
                print(f"Position: {-x}")
        except Exception as e:
            print(e)

    def preview_cameras_func(self):
        if (hasattr(self, "cam1") and self.cam1.cap.isOpened()):
            _, frame_a = self.cam1.cap.read()
            #_, frame_b = self.cam2.cap.read()
            #_, frame_c = self.cam3.cap.read()
            #_, frame_d = self.cam4.cap.read()

            image_path_a = str(Cameras.images_dir / "cam_preview_a.jpeg")
            #image_path_b = str(Cameras.images_dir / "cam_preview_b.jpeg")
            #image_path_c = str(Cameras.images_dir / "cam_preview_c.jpeg")
            #image_path_d = str(Cameras.images_dir / "cam_preview_d.jpeg")

            cv2.imwrite(image_path_a, frame_a)
            #cv2.imwrite(image_path_b, frame_b)
            #cv2.imwrite(image_path_c, frame_c)
            #cv2.imwrite(image_path_d, frame_d)

            self.preview_cameras.set_images(image_path_a)
            self.loading_cams_frame.destroy()
        else:
            print("failure showing images, not all cameras connected")

    def quit_button_func(self):
        try:
            os.remove(str(images_dir / "cam_preview_a.jpeg"))
            #os.remove(str(images_dir / "cam_preview_b.jpeg"))
            #os.remove(str(images_dir / "cam_preview_c.jpeg"))
            #os.remove(str(images_dir / "cam_preview_d.jpeg"))
        except Exception:
            pass

        try:
            self.cam1.cap.release()
            #self.cam2.cap.release()
            #self.cam3.cap.release()
            #self.cam4.cap.release()
        except Exception as e:
            pass
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
    cv2.destroyAllWindows()
