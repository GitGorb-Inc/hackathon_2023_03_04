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
        self.grid_columnconfigure((0, 7), weight=1)
        self.grid_columnconfigure((3, 4), weight=0)
        self.grid_columnconfigure((1, 2, 5, 6), weight=2)
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
        self.home_button = customtkinter.CTkButton(master=self, text="", image=self.home_image,
                                                   fg_color="transparent", command=self.home_button_event,
                                                   hover=False, width=130, height=130, border_width=-1,
                                                   border_spacing=-1)

        # geometry
        self.settings_button.grid(row=0, column=6, padx=10, pady=10)
        self.messages_button.grid(row=0, column=1, padx=10, pady=10)
        self.achievements_button.grid(row=0, column=5, padx=10, pady=10)
        self.friends_button.grid(row=0, column=2, padx=10, pady=10)
        self.row_filler.grid(row=1, column=0, columnspan=8)
        self.home_spacer.grid(row=0, column=3, columnspan=2)
        self.home_button.place(anchor="center", x=360, y=50)
        # self.home_bg.place(anchor="center", x=360)

    def select_frame_by_name(self, name):
        # set button color for selected button
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
        self.title = customtkinter.CTkLabel(master=self, text="Welcome, [Placeholder]", font=("roboto",60))
        self.title2 = customtkinter.CTkLabel(master=self, text="You have 5 friends and 12 points.", font=("roboto",35))
        self.grid_columnconfigure(0, weight=0)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources/PNG")
        self.pfp_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image 11.png")), size=(400, 400))
        self.pfp_button = customtkinter.CTkButton(master=self, text="", corner_radius=0, height=400, width=400,
                                                  fg_color="transparent", hover=False, image=self.pfp_image)
        self.pfp_button.place(anchor="n", relx=0.5, rely=0.1)
        self.title.place(anchor="n", relx=0.5, rely=0.55)
        self.title2.place(anchor="n", relx=0.5, rely=0.65)


class SettingsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.main = self.master.master.master
        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self, text="Settings", font=self.main.title_font, width=640, height=200)
        self.fsize_label = customtkinter.CTkLabel(self, text="Font Size", font=self.main.normal_font, width=640,
                                                  height=50)
        self.fsize_slider = customtkinter.CTkSlider(self, width=400, height=30, from_=8, to=20,
                                                    command=self.adjust_font)
        self.logout = customtkinter.CTkButton(self, width=200, height=80, fg_color="#ff0000", text="Logout",
                                              font=self.main.normal_font)
        self.delete = customtkinter.CTkButton(self, width=200, height=80, fg_color="#ff0000", text="Delete Account",
                                              font=self.main.normal_font)

        self.label.grid(row=0, column=0, sticky="new")
        self.fsize_label.grid(row=1, column=0, pady=20, sticky="new")
        self.fsize_slider.grid(row=2, column=0, pady=10)
        self.logout.grid(row=3, column=0, pady=40)
        self.delete.grid(row=4, column=0, pady=30)

    def adjust_font(self, val):
        val = int(val)
        self.main.title_font = customtkinter.CTkFont(size=5 * val)
        self.main.normal_font = customtkinter.CTkFont(size=3 * val)
        self.label.configure(True, font=self.main.title_font)
        self.fsize_label.configure(True, font=self.main.normal_font)
        self.logout.configure(font=self.main.normal_font,
                              width=80 + 10 * val, height=50 + 3 * val)
        self.delete.configure(font=self.main.normal_font,
                              width=100 + 10 * val, height=50 + 3 * val)


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
        self.label.grid(row=0, column=0, sticky="nsew")


class FriendsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources/PNG")
        self.profile0_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image 6.png")),
                                                     size=(210, 210))
        self.profile1_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image 7.png")),
                                                     size=(210, 210))
        self.profile2_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image 8.png")),
                                                     size=(210, 210))
        self.profile3_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image 9.png")),
                                                     size=(210, 210))
        self.profile4_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image 10.png")),
                                                     size=(210, 210))
        self.profile_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image 12.png")),
                                                    size=(210, 210))

        # widgets
        self.profile0 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                fg_color="transparent", hover=False, image=self.profile0_image)
        self.profile1 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                fg_color="transparent", hover=False, image=self.profile1_image)
        self.profile2 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                fg_color="transparent", hover=False, image=self.profile2_image)
        self.profile3 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                fg_color="transparent", hover=False, image=self.profile3_image)
        self.profile4 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                fg_color="transparent", hover=False, image=self.profile4_image)
        self.profile5 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                fg_color="transparent", hover=False, image=self.profile_image)
        self.profile6 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                fg_color="transparent", hover=False, image=self.profile_image)
        self.profile7 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                fg_color="transparent", hover=False, image=self.profile_image)
        self.profile8 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                fg_color="transparent", hover=False, image=self.profile_image)
        self.profile9 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                fg_color="transparent", hover=False, image=self.profile_image)
        self.profile10 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                 fg_color="transparent", hover=False, image=self.profile_image)
        self.profile11 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                 fg_color="transparent", hover=False, image=self.profile_image)
        self.profile12 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                 fg_color="transparent", hover=False, image=self.profile_image)
        self.profile13 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                 fg_color="transparent", hover=False, image=self.profile_image)
        self.profile14 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                 fg_color="transparent", hover=False, image=self.profile_image)
        self.profile15 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                 fg_color="transparent", hover=False, image=self.profile_image)
        self.profile16 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                 fg_color="transparent", hover=False, image=self.profile_image)
        self.profile17 = customtkinter.CTkButton(master=self, text="", corner_radius=10, height=210, width=210,
                                                 fg_color="transparent", hover=False, image=self.profile_image)

        # geometry
        self.profile0.grid(row=0, column=0, pady=10)
        self.profile1.grid(row=0, column=1, pady=10)
        self.profile2.grid(row=0, column=2, pady=10)
        self.profile3.grid(row=1, column=0, pady=10)
        self.profile4.grid(row=1, column=1, pady=10)
        self.profile5.grid(row=1, column=2, pady=10)
        self.profile6.grid(row=2, column=0, pady=10)
        self.profile7.grid(row=2, column=1, pady=10)
        self.profile8.grid(row=2, column=2, pady=10)
        self.profile9.grid(row=3, column=0, pady=10)
        self.profile10.grid(row=3, column=1, pady=10)
        self.profile11.grid(row=3, column=2, pady=10)
        self.profile12.grid(row=4, column=0, pady=10)
        self.profile13.grid(row=4, column=1, pady=10)
        self.profile14.grid(row=4, column=2, pady=10)
        self.profile15.grid(row=5, column=0, pady=10)
        self.profile16.grid(row=5, column=1, pady=10)
        self.profile17.grid(row=5, column=2, pady=10)


class BeFriend(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("BeFriend - Friend Finder for the socially inept")
        self.geometry("720x1280")
        self.resizable(False, False)
        # self.iconbitmap("/resources/file.ico")
        self.title_font = customtkinter.CTkFont(size=50)
        self.normal_font = customtkinter.CTkFont(size=30)

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
        # self.navigationBar.home_button.place(anchor="center",x=360,y=1180)
        self.navigationBar.select_frame_by_name("home")

    # widget methods
    def CLI_callback(self):
        dialog = customtkinter.CTkInputDialog(text="Enter command", title="Development Console")
        cmd = dialog.get_input()
        print(cmd)

    def logo_button_event(self):
        print("Logo clicked")


def main():
    return BeFriend()
