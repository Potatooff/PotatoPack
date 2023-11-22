import customtkinter as c
from typing import Optional, Tuple, Union
from src.app.components.shared import BG_COLOR
from src.app.Images import send_queries_icon
from src.app.Fonts import font_ArchitectsDaughter_var, font_quicksand_var


class Component_Welcome_Screen_Label(c.CTkLabel):
    def __init__(
            self, 
            master: any, 

            **kwargs
    ) -> None:
        
        super().__init__(
            master,  
            **kwargs
        )

        


class Component_Welcome_Screen_Queries_Button(c.CTkFrame):

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
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 3, 4, 5, 6), weight=1)


        self.query_button_1: c.CTkButton = c.CTkButton(self, text="How to use Onlyfan?", height=40, width=150, fg_color=BG_COLOR,
                                          image=send_queries_icon, compound="right", font=(font_quicksand_var, 16), border_color="#6b6c7b",
                                          border_width=2, corner_radius=8)
        self.query_button_3: c.CTkButton = c.CTkButton(self, text="Why did my wife left me?", height=40, width=150, fg_color=BG_COLOR,
                                          image=send_queries_icon, compound="right", font=(font_quicksand_var, 16), border_color="#6b6c7b",
                                          border_width=2, corner_radius=8)
        
        self.query_button_1.grid(row=0, column=1, padx=(20, 15), pady=20, sticky="nsew")
        self.query_button_3.grid(row=0, column=3, padx=(20, 15), pady=20, sticky="nsew")

        # TODO Make this works!


class Component_Welcome_Screen(c.CTkFrame):

    def __init__(
            self, 
            master: any, 
            **kwargs
    ) -> None:
        
        super().__init__(
            master,
            **kwargs
        )


        # Main Grid Layout
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)


        # Default label
        self.default_label: Component_Welcome_Screen_Label = Component_Welcome_Screen_Label(self, font=(font_ArchitectsDaughter_var, 44), text="PotatoGPT", fg_color=BG_COLOR)
        self.default_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(150, 20), sticky="nsew")


        # Pack of queries
        self.queries: Component_Welcome_Screen_Queries_Button = Component_Welcome_Screen_Queries_Button(self, fg_color=BG_COLOR)
        self.queries.grid(row=1, column=0, columnspan=2, padx=(80, 0), pady=0, sticky="sew")
