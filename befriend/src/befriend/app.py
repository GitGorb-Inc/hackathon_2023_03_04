import customtkinter
from sys import platform

customtkinter.set_default_color_theme("befriend_theme.json")

if platform == "linux" or platform == "linux2":
    customtkinter.set_appearance_mode("dark")
else:
    customtkinter.set_appearance_mode("system")

customtkinter.set_widget_scaling(1.1)  # widget dimensions and text size
customtkinter.set_window_scaling(0.6)  # window geometry dimensions

class BeFriend(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("BeFriend - Friend Finder for the socially inept")
        self.geometry("720x1280")
        self.resizable(False, False)
        # self.iconbitmap("/resources/file.ico")

        # widgets
        self.button = customtkinter.CTkButton(master=self, command=self.button_callback)
        self.button.pack(padx=20, pady=20)

    # widget methods
    def button_callback(self):
        print("button pressed")

def main():
    return BeFriend()
