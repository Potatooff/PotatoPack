import customtkinter as c
from src.app.Fonts import *
from src.app.Images import *
from src.utils.useful import *
from src.app.components.shared import *





class Component_ChatBox(c.CTkFrame):

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
        self.grid_rowconfigure((0, 1), weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        # This is user input entry box
        self.user_input_text_box = c.CTkTextbox(self, font=(font_nunito_var, 16), height=35, corner_radius=10, border_width=2, border_color="#6b6c7b",
                                               fg_color=chat_box_chat_entry_BG_COLOR)
        
        self.user_input_text_box.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # This is button to send input
        self.user_input_send_button = c.CTkButton(self, text=" ", width=50, height=45, image=send_message_icon, corner_radius=10, fg_color=BG_COLOR,
                                                  hover=False)
        self.user_input_send_button.grid(row=0, column=1, padx=(5, 20),pady=(20, 0))
        

        # This is warning text
        self.user_warning_text = c.CTkLabel(self, text=warning_message_for_user, text_color="#CCCCCC", font=(font_montserrat_var, 14))
        self.user_warning_text.grid(row=1, column=0, columnspan=2, padx=0, pady=(5, 5), sticky="nsew")