# Libraries import
import customtkinter as c
from src.app.components.shared import *
from typing import Optional, Tuple, Union

# Files Import
from src.app.Fonts import font_montserrat_var
from src.app.components.sidebarv2 import Component_Sidebar
from src.app.components.chatbox import Component_ChatBox
from src.app.components.DefaultChat import Component_Welcome_Screen


# MAIN WINDOW
class APP_CHAT(c.CTk):
    def __init__(
            self, 
            fg_color: str | Tuple[str, str] | None = None, 
            **kwargs
    ) -> None:
        super().__init__(
            fg_color, 
            **kwargs
        )

        # Window settings
        self.title("POTATO-GPT v1.0.0")
        self.geometry(f"{1300}x{650}")
        self.resizable(False, False)

        # MAIN GRID LAYOUT
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Initialization on main window frame
        self.main: APP_CHAT_MAIN_FRAME = APP_CHAT_MAIN_FRAME(self, fg_color=BG_COLOR)
        self.main.grid(row=0, column=0, sticky="nsew")



# MAIN WINDOW FRAME 
class APP_CHAT_MAIN_FRAME(c.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

         # Main Frame Layout
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1,weight=1)  



        # Window - Sidebar 
        self.window_sidebar: Component_Sidebar = Component_Sidebar(self, width=200, height=self.winfo_height(), fg_color=SIDEBAR_BG_COLOR, corner_radius=0, 
                                                border_width=0) # Width + Height doesnt work here! No fix needed
        
        self.window_sidebar.grid(row=0, rowspan=6, column=0, padx=(0, 0), pady=0, sticky="nsew")


        # Window - Chatbox
        self.window_chatbox: Component_ChatBox = Component_ChatBox(self, height=100, fg_color=BG_COLOR, corner_radius=0, border_width=0)
        self.window_chatbox.grid(row=5, column=1, padx=20, pady=0, sticky="nsew")


        # Window - Home Label
        self.default_chat_history: Component_Welcome_Screen = Component_Welcome_Screen(self, fg_color=BG_COLOR)
        self.default_chat_history.grid(row=0, rowspan=5, column=1, padx=(0, 0), pady=0, sticky="nsew")