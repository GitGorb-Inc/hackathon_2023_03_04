import customtkinter
import tkinter
from sys import platform
from PIL import Image

customtkinter.set_default_color_theme("befriend_theme.json")

# if platform == "linux" or platform == "linux2":
#     customtkinter.set_appearance_mode("dark")
# else:
#     customtkinter.set_appearance_mode("system")

customtkinter.set_appearance_mode("light")
customtkinter.set_widget_scaling(0.6)  # widget dimensions and text size
customtkinter.set_window_scaling(0.6)  # window geometry dimensions


class BottomBarFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # widgets


class BeFriend(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("BeFriend - Friend Finder for the socially inept")
        self.geometry("720x1280")
        self.resizable(False, False)
        # self.iconbitmap("/resources/file.ico")

        # widgets
        self.button = customtkinter.CTkButton(master=self, text="CLI", command=self.button_callback)
        self.lowerBar = BottomBarFrame(master=self, fg_color="#477998", corner_radius=25, width=720, height=200)
        # geometry
        self.button.place(x=0, y=0)
        self.lowerBar.place(x=0, y=1180)

    # widget methods
    def button_callback(self):
        dialog = customtkinter.CTkInputDialog(text="Enter command", title="Development Console")
        cmd = dialog.get_input()
        print(cmd)

def main():
    return BeFriend()
