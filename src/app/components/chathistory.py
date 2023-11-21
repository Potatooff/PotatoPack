import customtkinter as c
from typing import Tuple
from src.app.components.shared import BG_COLOR
from src.app.Fonts import font_ArchitectsDaughter_var, font_nunito_var
from src.app.components.DefaultChat import Component_Welcome_Screen_Label

from random import randint as random_int

class Component_Chat_History(c.CTkFrame):

    def __init__(
            self, 
            master: any, 
            item_list: list = [],
            **kwargs
    ) -> None:
        
        super().__init__(
            master,
            **kwargs
        )
        # Once created
        self.bg = Component_Welcome_Screen_Label(self, text="PotatoGPT on Sterium", font=(font_ArchitectsDaughter_var, 44), fg_color=BG_COLOR)
        self.bg.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.bg_bool = True

        # Chat blocs
        self.chat_blocks_list = []

        # MAIN GRID LAYOUT
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1,weight=1)

    def add_user_message(self, message: str) -> None:
        if self.bg:
            self.bg.grid_forget()
            self.bg_bool = False
        
        container = c.CTkFrame(self, corner_radius=10)
        container.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Container grid layout
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Message
        user_query = c.CTkLabel(container, text=message, font=(font_nunito_var, 16))
        user_query.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        ...

    def add_bot_message(self, message: str, image: any = None) -> None:
        ...