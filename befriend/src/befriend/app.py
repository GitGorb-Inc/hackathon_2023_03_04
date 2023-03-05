import customtkinter
import tkinter
from sys import platform
from PIL import Image

customtkinter.set_default_color_theme("befriend_theme.json")

customtkinter.set_appearance_mode("light")
customtkinter.set_widget_scaling(0.6)  # widget dimensions and text size
customtkinter.set_window_scaling(0.6)  # window geometry dimensions


class NavigationBarFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # widgets


class AchievementsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self,text="Achievements")
        self.label.grid(row=0, column=0, padx=20)


class SettingsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self, text="Settings")
        self.label.grid(row=0, column=0, padx=20)


class ChatsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self,text="Chats")
        self.label.grid(row=0, column=0, padx=20)


class FriendsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self,text="Friends")
        self.label.grid(row=0, column=0, padx=20)

class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self, text="Home")
        self.label.grid(row=0, column=0, padx=20)


class BeFriend(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("BeFriend - Friend Finder for the socially inept")
        self.geometry("720x1280")
        self.resizable(False, False)
        # self.iconbitmap("/resources/file.ico")

        self.CLI = customtkinter.CTkButton(master=self, text="CLI", command=self.CLI_callback)
        # navigationBar
        self.navigationBar = NavigationBarFrame(master=self, fg_color="#477998", corner_radius=25, width=720, height=200)

        # frames
        self.home = HomeFrame(master=self, corner_radius=0, fg_color="transparent")
        self.settings = SettingsFrame(master=self, corner_radius=0, fg_color="transparent")
        self.chats = ChatsFrame(master=self, corner_radius=0, fg_color="transparent")
        self.achievements = AchievementsFrame(master=self, corner_radius=0, fg_color="transparent")
        self.friends = FriendsFrame(master=self, corner_radius=0, fg_color="transparent")

        # frame switching
        # self.select_frame_by_name("home")



        # geometry
        self.CLI.place(x=0, y=0)
        self.navigationBar.place(x=0, y=1180)

    # widget methods
    def CLI_callback(self):
        dialog = customtkinter.CTkInputDialog(text="Enter command", title="Development Console")
        cmd = dialog.get_input()
        print(cmd)

    # def select_frame_by_name(self, name):
        # set button color for selected button
        # self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        # self.settings_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")
        # self.chats_button.configure(fg_color=("gray75", "gray25") if name == "chats" else "transparent")
        # self.achievements_button.configure(fg_color=("gray75", "gray25") if name == "achievements" else "transparent")
        # self.friends_button.configure(fg_color=("gray75", "gray25") if name == "friends" else "transparent")

        # show selected frame
        # if name == "home":
        #     self.home_frame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     self.home_frame.grid_forget()
        # if name == "frame_2":
        #     self.second_frame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     self.second_frame.grid_forget()
        # if name == "frame_3":
        #     self.third_frame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def settings_button_event(self):
        self.select_frame_by_name("settings")

    def chats_button_event(self):
        self.select_frame_by_name("chats")

    def achievements_button_event(self):
        self.select_frame_by_name("achievements")

    def friends_button_event(self):
        self.select_frame_by_name("friends")

def main():
    return BeFriend()
