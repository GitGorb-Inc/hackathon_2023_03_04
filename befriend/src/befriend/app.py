import customtkinter

customtkinter.set_default_color_theme("befriend_theme.json")
customtkinter.set_appearance_mode("system")

customtkinter.set_widget_scaling(0.5)  # widget dimensions and text size
customtkinter.set_window_scaling(0.5)  # window geometry dimensions

class BeFriend(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("minimal example app")
        self.minsize(720, 1280)

        self.button = customtkinter.CTkButton(master=self, command=self.button_callback)
        self.button.pack(padx=20, pady=20)

    def button_callback(self):
        print("button pressed")

def main():
    return BeFriend()