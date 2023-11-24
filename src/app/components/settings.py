# Libraries import
import customtkinter as c

# Files Imports
from src.app.Fonts import *
from src.app.Images import *
from src.utils.useful import *
from src.app.components.shared import *

# Settings Pages
from src.app.components.SettingsPage.user import Settings_UserPage
from src.app.components.SettingsPage.general import Settings_GeneralPage
from src.app.components.SettingsPage.help import Settings_HelpPage
from src.app.components.SettingsPage.about import Settings_AboutPage


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
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((1, 2, 3), weight=1)


        # This is the title
        self.title_text: c.CTkLabel = c.CTkLabel(self, text="Settings", font=("Montserrat", 20), fg_color=BG_COLOR)
        self.title_text.grid(row=0, column=0, columnspan=2, padx=0, pady=(15, 15), sticky="new")


        self.main_container: c.CTkFrame = c.CTkFrame(self, fg_color=BG_COLOR)
        self.main_container.grid(row=1, column=0, columnspan=2, rowspan=4, padx=15, pady=(0, 15), sticky="nsew")

        # Main container grid layout
        self.main_container.grid_columnconfigure(0, weight=1)
        self.main_container.grid_rowconfigure((0, 1, 2, 3, 4), weight=0)


        # User settings
        self.user_settings_frame = Settings_UserPage(self.main_container, height=75, fg_color=BG_COLOR)
        self.user_settings_frame.grid(row=0, column=0, pady=15, sticky="nsew")

        # General settings
        self.general_settings_frame = Settings_GeneralPage(self.main_container, height=75, fg_color=BG_COLOR)
        self.general_settings_frame.grid(row=1, column=0, pady=15, sticky="nsew")

        # Help settings
        self.help_settings_frame = Settings_HelpPage(self.main_container, height=75, fg_color=BG_COLOR)
        self.help_settings_frame.grid(row=2, column=0, pady=15, sticky="nsew")

        # About settings
        self.about_settings_frame = Settings_AboutPage(self.main_container, height=75, fg_color=BG_COLOR)
        self.about_settings_frame.grid(row=3, column=0, pady=15, sticky="nsew")

