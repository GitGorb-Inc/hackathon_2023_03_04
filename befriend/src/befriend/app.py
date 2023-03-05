import customtkinter
import os
from PIL import Image
# import tkinter
# from sys import platform

customtkinter.set_default_color_theme("befriend_theme.json")

customtkinter.set_appearance_mode("light")
customtkinter.set_widget_scaling(0.6)  # widget dimensions and text size
customtkinter.set_window_scaling(0.6)  # window geometry dimensions


class NavigationBarFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure((0, 7), weight=0)
        self.grid_columnconfigure((3, 4), weight=0)
        self.grid_columnconfigure((1, 2, 5, 6), weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources/nav_bar")
        self.home_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(80, 80))
        self.settings_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "settings.png")), size=(80, 80))
        self.messages_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "messages.png")), size=(80, 80))
        self.achievements_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "achievements.png")), size=(80, 80))
        self.friends_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "friends.png")), size=(80, 80))

        # widgets
        self.settings_button = customtkinter.CTkButton(master=self, text="", corner_radius=20, height=80, width=80,
                                                       fg_color="transparent", command=self.settings_button_event,
                                                       hover_color="#589ac4", image=self.settings_image)
        self.messages_button = customtkinter.CTkButton(master=self, text="", corner_radius=20, height=80, width=80,
                                                       fg_color="transparent", command=self.messages_button_event,
                                                       hover_color="#589ac4", image=self.messages_image)
        self.achievements_button = customtkinter.CTkButton(master=self, text="", corner_radius=20, height=80, width=80,
                                                           fg_color="transparent", hover_color="#589ac4", command=self.achievements_button_event,
                                                           image=self.achievements_image)
        self.friends_button = customtkinter.CTkButton(master=self, text="", corner_radius=20, height=80, width=80,
                                                      fg_color="transparent", command=self.friends_button_event,
                                                      hover_color="#589ac4", image=self.friends_image)
        self.row_filler = customtkinter.CTkLabel(master=self, text="\n", width=720, height=100)
        self.home_spacer = customtkinter.CTkLabel(master=self, text="\n", width=150)
        self.home_bg = customtkinter.CTkLabel(master=self, text="\n", width=150, height=150, corner_radius=75, fg_color="gray95")

        # geometry
        self.settings_button.grid(row=0, column=6, padx=10, pady=10)
        self.messages_button.grid(row=0, column=1, padx=10, pady=10)
        self.achievements_button.grid(row=0, column=5, padx=10, pady=10)
        self.friends_button.grid(row=0, column=2, padx=10, pady=10)
        self.row_filler.grid(row=1, column=0, columnspan=8)
        self.home_spacer.grid(row=0, column=3, columnspan=2)
        self.home_bg.place(anchor="center", x=360)

    def select_frame_by_name(self, name):
        # set button color for selected button
        # self.home_button.configure(fg_color="#589ac4" if name == "home" else "transparent")
        self.settings_button.configure(fg_color="#589ac4" if name == "settings" else "transparent")
        self.messages_button.configure(fg_color="#589ac4" if name == "messages" else "transparent")
        self.achievements_button.configure(fg_color="#589ac4" if name == "achievements" else "transparent")
        self.friends_button.configure(fg_color="#589ac4" if name == "friends" else "transparent")

        # show selected frame
        # if name == "home":
        #     HomeFrame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     HomeFrame.grid_forget()
        if name == "settings":
            SettingsFrame.grid(row=0, column=1, sticky="nsew")
        else:
            SettingsFrame.grid_forget()
        if name == "messages":
            MessagesFrame.grid(row=0, column=1, sticky="nsew")
        else:
            MessagesFrame.grid_forget()
        if name == "achievements":
            AchievementsFrame.grid(row=0, column=1, sticky="nsew")
        else:
            AchievementsFrame.grid_forget()
        if name == "friends":
            FriendsFrame.grid(row=0, column=1, sticky="nsew")
        else:
            FriendsFrame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def settings_button_event(self):
        self.select_frame_by_name("settings")

    def messages_button_event(self):
        self.select_frame_by_name("messages")

    def achievements_button_event(self):
        self.select_frame_by_name("achievements")

    def friends_button_event(self):
        self.select_frame_by_name("friends")







class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self, text="Home")
        self.label.grid(row=0, column=0, padx=20)


class SettingsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self, text="Settings")
        self.label.grid(row=0, column=0, padx=20)


class MessagesFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self, text="Messages")
        self.label.grid(row=0, column=0, padx=20)


class AchievementsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self, text="Achievements")
        self.label.grid(row=0, column=0, padx=20)


class FriendsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self, text="Friends")
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
        self.messages = MessagesFrame(master=self, corner_radius=0, fg_color="transparent")
        self.achievements = AchievementsFrame(master=self, corner_radius=0, fg_color="transparent")
        self.friends = FriendsFrame(master=self, corner_radius=0, fg_color="transparent")

        # frame switching

        # geometry
        self.CLI.place(x=0, y=0)
        self.navigationBar.place(x=0, y=1180)

    # widget methods
    def CLI_callback(self):
        dialog = customtkinter.CTkInputDialog(text="Enter command", title="Development Console")
        cmd = dialog.get_input()
        print(cmd)

def main():
    return BeFriend()
