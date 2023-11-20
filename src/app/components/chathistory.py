import customtkinter as c
from typing import Tuple

from random import randint as random_int

class Component_Chat_History(c.CTkFrame):

    def __init__(
            self, 
            master: any, 
            **kwargs
    ) -> None:
        
        super().__init__(
            master,
            **kwargs
        )

        self.label = c.CTkLabel(self, text=random_int(0, 10000))
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")