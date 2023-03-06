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
        self.home_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(130, 130))
        self.settings_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "settings.png")),
                                                     size=(80, 80))
        self.messages_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "messages.png")),
                                                     size=(80, 80))
        self.achievements_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "achievements.png")),
                                                         size=(80, 80))
        self.friends_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "friends.png")), size=(80, 80))

        # widgets
        self.home_button = customtkinter.CTkButton(master=self, text="", corner_radius=65, height=130, width=130,
                                                       fg_color="transparent", command=self.home_button_event,
                                                       hover_color="#589ac4", image=self.home_image)
        self.settings_button = customtkinter.CTkButton(master=self, text="", corner_radius=20, height=80, width=80,
                                                       fg_color="transparent", command=self.settings_button_event,
                                                       hover_color="#589ac4", image=self.settings_image)
        self.messages_button = customtkinter.CTkButton(master=self, text="", corner_radius=20, height=80, width=80,
                                                       fg_color="transparent", command=self.messages_button_event,
                                                       hover_color="#589ac4", image=self.messages_image)
        self.achievements_button = customtkinter.CTkButton(master=self, text="", corner_radius=20, height=80, width=80,
                                                           fg_color="transparent", hover_color="#589ac4",
                                                           command=self.achievements_button_event,
                                                           image=self.achievements_image)
        self.friends_button = customtkinter.CTkButton(master=self, text="", corner_radius=20, height=80, width=80,
                                                      fg_color="transparent", command=self.friends_button_event,
                                                      hover_color="#589ac4", image=self.friends_image)
        self.row_filler = customtkinter.CTkLabel(master=self, text="\n", width=720, height=100)
        self.home_spacer = customtkinter.CTkLabel(master=self, text="\n", width=150)
        self.home_bg = customtkinter.CTkLabel(master=self, text="\n", width=150, height=150, corner_radius=75,
                                              fg_color="gray95")

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
        self.home_button.configure(fg_color="#589ac4" if name == "home" else "transparent")
        self.settings_button.configure(fg_color="#589ac4" if name == "settings" else "transparent")
        self.messages_button.configure(fg_color="#589ac4" if name == "messages" else "transparent")
        self.achievements_button.configure(fg_color="#589ac4" if name == "achievements" else "transparent")
        self.friends_button.configure(fg_color="#589ac4" if name == "friends" else "transparent")

        # show selected frame
        if name == "home":
            self.master.home.place(anchor="nw", x=20, y=140)
        else:
            self.master.home.place_forget()
        if name == "settings":
            self.master.settings.place(anchor="nw", x=20, y=140)
        else:
            self.master.settings.place_forget()
        if name == "messages":
            self.master.messages.place(anchor="nw", x=20, y=140)
        else:
            self.master.messages.place_forget()
        if name == "achievements":
            self.master.achievements.place(anchor="nw", x=20, y=140)
        else:
            self.master.achievements.place_forget()
        if name == "friends":
            self.master.friends.place(anchor="nw", x=20, y=140)
        else:
            self.master.friends.place_forget()

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
        # widgets
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(71, 100))
        self.logo_text = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo-name.png")), size=(400, 100))
        self.logo_button = customtkinter.CTkButton(master=self, text="", corner_radius=0, height=100, width=71,
                                                   fg_color="transparent", command=self.logo_button_event,
                                                   hover_color="gray95", image=self.logo_image)
        self.logo_text = customtkinter.CTkLabel(master=self, text="", corner_radius=0, height=100, width=400,
                                                fg_color="transparent", image=self.logo_text)

        # frames
        self.navigationBar = NavigationBarFrame(master=self, fg_color="#477998", corner_radius=25, width=720,
                                                height=200)
        self.home = HomeFrame(master=self, corner_radius=0, fg_color="transparent", width=680, height=965)
        self.settings = SettingsFrame(master=self, corner_radius=0, fg_color="transparent", width=680, height=965)
        self.messages = MessagesFrame(master=self, corner_radius=0, fg_color="transparent", width=680, height=965)
        self.achievements = AchievementsFrame(master=self, corner_radius=0, fg_color="transparent", width=680,
                                              height=965)
        self.friends = FriendsFrame(master=self, corner_radius=0, fg_color="transparent", width=680, height=965)

        # frame switching

        # geometry
        # self.CLI.place(x=0, y=0)
        self.navigationBar.place(x=0, y=1180)
        self.logo_text.place(anchor="nw", y=20, x=40)
        self.logo_button.place(anchor="nw", y=20, x=600)
        NavigationBarFrame.home_button.place(anchor="center",x=360,y=1180)

    # widget methods
    def CLI_callback(self):
        dialog = customtkinter.CTkInputDialog(text="Enter command", title="Development Console")
        cmd = dialog.get_input()
        print(cmd)

    def logo_button_event(self):
        print("Logo clicked")


def main():
    return BeFriend()
