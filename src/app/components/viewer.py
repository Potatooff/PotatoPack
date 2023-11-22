import customtkinter as c


class Window_ImageViewer(c.CTkToplevel):
    def __init__(
            self, 
            image2view,
            *args, 
            **kwargs
        ) -> None:
        super().__init__(
            *args, 
            **kwargs
        )

        self.image2view = image2view
        #self.geometry
        self.title("Image Viewer v1.0.0")
        self.geometry(f"{500}x{500}")


        # MAIN GRID LAYOUT
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Image
        self.image = c.CTkLabel(self, text="", image=self.image2view)
        self.image.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")