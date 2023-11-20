import customtkinter as c
from src.app.Fonts import *
from src.app.Images import *
from src.utils.useful import *
from src.app.components.shared import *
from typing import Optional, Tuple, Union


class Component_SettingsPage(c.CTkFrame):
    
        def __init__(
                self, 
                master: any, 
                **kwargs
        ) -> None:
            
            super().__init__(
                master,  
                **kwargs
            )


            # MAIN GRID LAYOUT
            self.grid_columnconfigure((0, 1), weight=1)
            self.grid_rowconfigure((0, 1, 2, 3), weight=0)


            # This is the title
            self.title_text = c.CTkLabel(self, text="Settings", font=("Montserrat", 20), fg_color=BG_COLOR)
            self.title_text.grid(row=0, column=0, columnspan=2, padx=0, pady=(20, 20), sticky="nsew")