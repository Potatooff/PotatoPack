import customtkinter as c
from src.app.Fonts import *
from src.app.Images import *
from src.utils.useful import *
from src.app.components.shared import *
from typing import Optional, Tuple, Union
from random import choice as random_choice
from src.app.components.settings import Component_SettingsPage
from src.app.components.chathistory import Component_Chat_History



class Component_Sidebar(c.CTkFrame):

    def __init__(
            self, 
            master: any, 
            width: int, 
            height: int, 
            corner_radius: int | str | None = None, 
            border_width: int | str | None = None, 
            bg_color: str | Tuple[str, str] = "transparent", 
            fg_color: str | Tuple[str, str] | None = None, 
            border_color: str | Tuple[str, str] | None = None, 
            background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
            overwrite_preferred_drawing_method: str | None = None, 
            **kwargs
    ) -> None:
        
        super().__init__(
            master, 
            width, 
            height, 
            corner_radius, 
            border_width, 
            bg_color, 
            fg_color, 
            border_color, 
            background_corner_colors, 
            overwrite_preferred_drawing_method, 
            **kwargs
        )


        # Main Grid Layout
        self.grid_rowconfigure((1, 2, 3, 4), weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=1)


        # New chat & close sidebar
        self.top_bar = Component_TopBar(self, width=200, height=50, fg_color=SIDEBAR_BG_COLOR)
        self.top_bar.grid(row=0, column=0, padx=0, pady=5)


        # List of chat session 
        self.section = Component_Section(self, width=200, height=50, fg_color=SIDEBAR_BG_COLOR, item_list="")
        self.section.grid(row=1, rowspan=4, column=0, padx=0, pady=5, sticky="nsew")
     

        # User profile frame
        self.profile_bar = Component_ProfileBar(self, width=200, height=50, fg_color=SIDEBAR_BG_COLOR)
        self.profile_bar.grid(row=5, column=0, padx=0, pady=0, sticky="nsew")


        # Button when sidebar is collapsed
        self.show_sidebar_button = c.CTkButton(self.master, text="",image=open_sidebar_icon,fg_color=BG_COLOR, width=50, hover=False,
                                                      command=self.show_sidebar_button_on_click)
        
        self.count = 0
        # FUNCTIONALITY
    def new_chat_button_on_click(self) -> None:
        """ Add a new chat session tab with a random title"""
        count = self.count + 1
        self.section.add_session_tab(f"Item {count}")
        self.count += 1
        
    def close_sidebar_button_on_click(self) -> None:
        """ Close sidebar when button get clicked"""

        self.grid_forget()
        self.show_sidebar_button.grid(row=0, rowspan=6, column=0, padx=0, pady=0)

    def show_sidebar_button_on_click(self) -> None:
        """ Show sidebar when button get clicked"""
        
        self.show_sidebar_button.grid_forget()
        self.grid(row=0, rowspan=6, column=0, padx=0, pady=0, sticky="nsew")



        

# This is TOP BAR OF THE SIDEBAR
class Component_TopBar(c.CTkFrame):
    def __init__(
            self, 
            master: any, 
            width: int, 
            height: int, 
            corner_radius: int | str | None = None, 
            border_width: int | str | None = None, 
            bg_color: str | Tuple[str, str] = "transparent", 
            fg_color: str | Tuple[str, str] | None = None, 
            border_color: str | Tuple[str, str] | None = None, 
            background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
            overwrite_preferred_drawing_method: str | None = None, 
            **kwargs
    ) -> None:
        
        super().__init__(
            master, 
            width, 
            height, 
            corner_radius, 
            border_width, 
            bg_color, 
            fg_color, 
            border_color, 
            background_corner_colors, 
            overwrite_preferred_drawing_method, 
            **kwargs
        )

        # Main Grid Layout
        self.grid_columnconfigure((0, 1), weight=0)
        

        # New chat session button
        self.new_chat_button = c.CTkButton(self, text="New chat", width=150, command=self.master.new_chat_button_on_click,
                                            fg_color=SIDEBAR_BG_COLOR, corner_radius=5, image=new_chat_icon, compound="left",
                                            anchor="w",font=(font_raleway_var, 15), hover=False)
        
        self.new_chat_button.grid(row=0, column=0, padx=(10, 0), pady=(10, 10), sticky="w")


        # Close sidebar button
        self.collapse_sidebar_button = c.CTkButton(self, text=" ", width=50, image=close_sidebar_icon, compound="right",
                                                   anchor="e", fg_color=SIDEBAR_BG_COLOR, corner_radius=5, hover=False, 
                                                   command=self.master.close_sidebar_button_on_click)
        
        self.collapse_sidebar_button.grid(row=0, column=1, padx=(5, 2), pady=(0, 2), sticky="ne")




class Component_Section(c.CTkScrollableFrame):
    def __init__(
            self, 
            master, 
            item_list, 
            **kwargs
        ) -> None:

        super().__init__(
            master, 
            **kwargs
        )

        # MAIN GRID LAYOUT
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)  # Only one row at the top

        for i, item in enumerate(item_list):
            self.add_item(item)

        # List of chat session
        self.session_tabs = []
        


        

    def delete_everything(self):
            """Delete everything in the grid"""
            start_row, rowspan =  0, 5

            widgets_in_range = [self.master.master.master.master.grid_slaves(row=row, column=1) for row in range(start_row, start_row + rowspan)]
            widgets_in_range = [widget for sublist in widgets_in_range for widget in sublist]
            if widgets_in_range:
                for widget in widgets_in_range:
                    widget.grid_forget()
        


    def add_session_tab(self, name) -> None:

        # Functionnality
        def close_session_tab_on_click() -> None:
            """Close the chat session tab when the button get clicked"""
            for i in self.session_tabs:
                if i[0] == session_tab:
                    i[0].destroy()
                    i[1].destroy()
                    self.session_tabs.remove(i)
                    break
            session_tab.destroy()
            if self.session_tabs == []:
                self.master.master.master.master.default_chat_history.grid(row=0, rowspan=5, column=1, padx=(0, 0), pady=0, sticky="nsew")


        def open_chat_history_on_click() -> None:
            """Open the chat history when the button get clicked"""
            self.delete_everything()
            for i in self.session_tabs:
                i[0].configure(fg_color=SIDEBAR_BG_COLOR)

                start_row, rowspan =  0, 1
                widgets_in_range = [i[0].grid_slaves(row=0, column=1) for row in range(start_row, start_row + rowspan)]
                widgets_in_range = [widget for sublist in widgets_in_range for widget in sublist]
                if widgets_in_range:
                    for widget in widgets_in_range:
                        widget.grid_forget()

            chat_history.grid(row=0, rowspan=5, column=1, padx=(0, 0), pady=0, sticky="nsew")
            session_tab.configure(fg_color=SIDEBAR_BUTTON_BG_COLOR)
            close_session_tab.grid(row=0, column=1, padx=(5, 2), pady=(3, 3), sticky="e")
        

        # Every Components
        chat_history = Component_Chat_History(self.master.master.master.master, fg_color=BG_COLOR)#, label_text="PotatoGPT v1.0.0")  # This is the chat session / history
        session_tab = c.CTkFrame(self, fg_color=SIDEBAR_BG_COLOR, corner_radius=8)


        # Session tab grid layout
        session_tab.grid_columnconfigure((0, 1), weight=1)

        # New button to open chat session
        open_chat_history = c.CTkButton(session_tab, text=f"   {truncate_string(name)}", width=150, fg_color="transparent",
                                        corner_radius=5, image=potato_icon, compound="left", anchor="w", hover=False,
                                        font=(font_raleway_var, 13), command=open_chat_history_on_click)
        

        # Close button to close chat session
        close_session_tab = c.CTkButton(session_tab, text="", width=50, image=close_sidebar_icon, compound="right",
                                    anchor="e", fg_color="transparent", corner_radius=5, hover=False,
                                    command=close_session_tab_on_click)


        # ALL GRIDS
        open_chat_history.grid(row=0, column=0, padx=(10, 0), pady=(10, 10), sticky="w")
        session_tab.grid(row=0, column=0, pady=5, padx=0, sticky="ew")
        self.session_tabs.insert(0, (session_tab, chat_history))
        open_chat_history_on_click()


        try:
            row: int = 0
            for i in self.session_tabs:
                i[0].grid_forget()
                i[0].grid(row= (row + 1), column=0, pady=5, padx=0, sticky="ew")
                row += 1

            del row

        except Exception as e:
            print(e)


        


class Component_ProfileBar(c.CTkFrame):
    def __init__(
            self, 
            master: any, 
            width: int, 
            height: int, 
            corner_radius: int | str | None = None, 
            border_width: int | str | None = None, 
            bg_color: str | Tuple[str, str] = "transparent", 
            fg_color: str | Tuple[str, str] | None = None, 
            border_color: str | Tuple[str, str] | None = None, 
            background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
            overwrite_preferred_drawing_method: str | None = None, 
            **kwargs
    ) -> None:
        
        super().__init__(
            master, 
            width, 
            height, 
            corner_radius, 
            border_width, 
            bg_color, 
            fg_color, 
            border_color, 
            background_corner_colors, 
            overwrite_preferred_drawing_method, 
            **kwargs
        )

        # Main Grid Layout
        self.grid_rowconfigure((0, 1), weight=0)
        self.grid_columnconfigure((0, 1), weight=0)

        # This act as a white line
        self.seperator = c.CTkButton(self, fg_color="#CCCCCC", height=3, text="", corner_radius=40, hover=False, state="disabled")
        self.seperator.grid(row=0, column=0, columnspan=2, padx=40, pady=(0, 0), sticky="sew")
        # end of white line

        # User profile image
        self.profile = c.CTkButton(self, image=user_icon, width=50, height=30, fg_color=SIDEBAR_BG_COLOR, corner_radius=5, 
                                   text=f"{truncate_string(input_str=username, username=True)}", compound="left", anchor="sw", 
                                   hover=False,font=(font_raleway_var, 15))
        
        self.profile.grid(row=1, column=0, padx=(10, 0), pady=(5, 5), sticky="sw")

        self.settings_button = c.CTkButton(self, image=settings_icon, width=30, height=30, fg_color=SIDEBAR_BG_COLOR, 
                                           corner_radius=5, text="", hover=False, command=self.settings_button_on_click)
        
        self.settings_button.grid(row=1, column=1, padx=(10, 0), pady=(0, 10), sticky="s")


        # Here is setting page initialization
        self.settings_page = Component_SettingsPage(self.master.master, fg_color=BG_COLOR)
    

    def settings_button_on_click(self) -> None:
        """Open settings page when the button gets clicked"""
        self.master.master.default_chat_history.grid_forget()
        self.master.master.window_chatbox.grid_forget()

        def delete_everything():
            """Delete everything in the grid"""
            row = 0
            start_row = 0
            rowspan = 6
            widgets_in_range = [self.master.master.grid_slaves(row=row, column=1) for row in range(start_row, start_row + rowspan)]
            widgets_in_range = [widget for sublist in widgets_in_range for widget in sublist]
            if widgets_in_range:
                for widget in widgets_in_range:
                    widget.grid_forget()
                    # Use destroy to completely remove and destroy the widget
                    

        delete_everything()
        self.settings_button.configure(image=home_icon, command=self.home_button_on_click)
        self.settings_page.grid(row=0, rowspan=6, column=1, padx=20, pady=0, sticky="nsew")



    def home_button_on_click(self) -> None:
        """Open settings page when button get clicked"""
        self.settings_page.grid_forget()
        self.master.master.default_chat_history.grid(row=0, rowspan=5, column=1, padx=(0, 0), pady=0, sticky="nsew")
        self.master.master.window_chatbox.grid(row=5, column=1, padx=20, pady=0, sticky="nsew")
        self.settings_button.configure(image=settings_icon, command=self.settings_button_on_click)


        
