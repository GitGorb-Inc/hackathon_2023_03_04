import customtkinter


class App(customtkinter.CTk):
    licznik = 0
    telnum=0
    def __init__(self):
        super().__init__()

        self.title("[Placeholder]")
        self.minsize(600, 600)

        self.button = customtkinter.CTkButton(master=self, command=self.button_callback)
        self.button.pack(padx=20, pady=20)
        self.slider = customtkinter.CTkSlider(master=self, from_=0, to=999999999, command=self.slider_callback, width=300,number_of_steps=1000000000)
        self.slider.pack(padx=20,pady=40)
    def button_callback(self):
        self.licznik += 1
        print(f"button pressed {self.licznik} times")
    def slider_callback(self,val):
        self.telnum = int(val)
        print(self.telnum)


if __name__ == "__main__":
    app = App()
    app.mainloop()