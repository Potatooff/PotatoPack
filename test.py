import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.s = customtkinter.CTkScrollableFrame(self)
        self.s.grid(row=0, column=0, sticky="nsew")

        self.s.grid_rowconfigure(0, weight=0)  # configure grid system
        self.s.grid_columnconfigure(0, weight=0)

        self.textbox = customtkinter.CTkLabel(master=self.s, width=600, corner_radius=0, text="    Some example text!\n" * 50, justify="left", anchor="w")
        self.textbox.grid(row=0, column=0, sticky="nsew")
        #self.textbox.insert("0.0", "Some example text!\n" * 50)


app = App()
app.mainloop()