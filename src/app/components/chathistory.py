import customtkinter as c
from typing import Tuple
from src.app.components.shared import BG_COLOR
from src.app.Fonts import font_ArchitectsDaughter_var, font_nunito_var
from src.app.components.DefaultChat import Component_Welcome_Screen_Label
from src.app.Images import user_icon

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
        self.bg.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.bg_bool = True

        # Chat blocs
        self.chat_blocks_list = []

        # MAIN GRID LAYOUT
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0,weight=1)

        for i, item in enumerate(item_list):
            self.add_item(item)


    def add_user_message(self, message: str) -> None:
        if self.bg:
            frame_title = c.CTkButton(self, text="PotatoGPT model v1.0.0", font=(font_nunito_var, 16), fg_color=BG_COLOR, border_width=2,
                                      state="disabled", hover=False)
            frame_title.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
            self.bg.grid_forget()
            self.bg_bool = False

            # MAIN GRID LAYOUT
            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=0)  # Only one row at the top
        

        container = c.CTkFrame(self, corner_radius=10, fg_color=BG_COLOR)
        container.grid(row=1, column=0, pady=7, padx=10, sticky="nsew")

        # Container Grid Layout
        container.grid_rowconfigure(0, weight=0)
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=0)
        container.grid_columnconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)

        # Image profile
        user_profile_image = c.CTkLabel(container, image=user_icon, corner_radius=10, fg_color=BG_COLOR, text="")
        user_profile_image.grid(row=0, column=0, padx=5, pady=0, sticky="w")


        # Message
        user_query = c.CTkTextbox(container, font=(font_nunito_var, 16), fg_color=BG_COLOR, text_color="#CCCCCC", 
                                  wrap="word", tabs=2, height=1, width=50)
        user_query.insert(c.INSERT, message) # Insert the message
        user_query.configure(state="disabled")
        user_query.grid(row=0, column=1, padx=3, pady=0, sticky="nsew")


        # Option
        button_delete_msg = c.CTkButton(container, text="X", fg_color="#6b6c7b", corner_radius=10, border_width=0, hover=False)
        button_delete_msg.grid(row=1, column=2, padx=5, pady=0)

        

        self.chat_blocks_list.append(container)

    def add_bot_message(self, message: str, image: any = None) -> None:
        ...