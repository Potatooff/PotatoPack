# Libraries Import
import customtkinter as c
from typing import Tuple, Optional


# Files import
from src.app.Fonts import *
from src.app.components.shared import *
from src.app.Images import about_icon

class Settings_AboutPage(c.CTkFrame):
        
    def __init__(
            self, 
            master: any, 
            **kwargs
    ) -> None:
        
        super().__init__(
            master,  
            **kwargs
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


        # Button
        self.button: c.CTkButton = c.CTkButton(self, image=about_icon, fg_color=BG_COLOR, text="  About", border_width=3,
                                               compound="left", anchor="w", font=(font_raleway_var, 22), height=75
                                              )
        
        self.button.grid(row=0, column=0, padx=10, pady=0, sticky="nsew")