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
        

        # FUNCTIONALITY
    def new_chat_button_on_click(self) -> None:
        """ Add a new chat session tab with a random title"""

        self.section.add_item(random_choice(
            ["test", "bonjour", "Salutation", 
             "Comment tuer des enfants", "How to k...?",
             "Greetings"
            ])
        )
        
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

        # Initialization of variables
        self.chat_conversation: list = []
        self.chat_conversation_row: list = []

        # This initializes the chat history with the stored sessions
        for i, item in enumerate(item_list):
            self.add_item(item)




    
    def remove_item(self, item) -> None:
        """Remove a chat session tab and destroy associated chat history"""

        for frame_holder, _, chatbox in self.chat_conversation_row:
            if item == frame_holder.grid_slaves(row=0, column=0)[0].cget("text"):
                frame_holder.destroy()
                chatbox.destroy()  # Destroy associated chat history box
                self.chat_conversation.remove(frame_holder)
                self.chat_conversation_row.remove((frame_holder, _, chatbox))



    
    def add_item(self, item) -> None:
        """Add a new chat session tab with a random title"""


        # Functionality
        def open_chat_session() -> None:
            """Open chat session when the button is clicked"""
            try:
                for frame_holder, _, chatbox in self.chat_conversation_row:
                        chatbox.grid_forget()  # Destroy associated chat history box
            except:
                pass

            frame_holder_chatbox.grid(row=0, rowspan=5, column=1, padx=(0, 0), pady=0, sticky="nsew")

        def close_chat_session() -> None:
            """Close chat session tab when the button is clicked"""
            self.master.master.master.master.default_chat_history.grid(row=0, rowspan=5, column=1, padx=(0, 0), pady=0, sticky="nsew")
            if frame_holder.winfo_exists():  # Check if the widget still exists
                frame_holder.destroy()
                frame_holder_chatbox.destroy()
                self.chat_conversation.remove(frame_holder)
                self.chat_conversation_row = [(frame, i, chatbox) for i, (frame, _, chatbox) in enumerate(self.chat_conversation_row)]  # Update chat_conversation_row


        
        

        frame_holder_chatbox = Component_Chat_History(self.master.master.master.master, fg_color=BG_COLOR)  # This is the chat session / history

        # This is the container
        frame_holder = c.CTkFrame(self, fg_color=SIDEBAR_BUTTON_BG_COLOR, corner_radius=8)
        frame_holder.grid_columnconfigure((0, 1), weight=1)

        # New button to open chat session
        self.open_chat_button = c.CTkButton(frame_holder, text=f"   {truncate_string(item)}", width=150,
                                            fg_color=SIDEBAR_BUTTON_BG_COLOR,
                                            corner_radius=5, image=potato_icon, compound="left", anchor="w", hover=False,
                                            font=(font_raleway_var, 13),
                                            command=open_chat_session)

        self.open_chat_button.grid(row=0, column=0, padx=(10, 0), pady=(10, 10), sticky="w")

        # Close button to close chat session
        self.close_chat_tab = c.CTkButton(frame_holder, text="", width=50, image=close_sidebar_icon, compound="right",
                                        anchor="e",
                                        fg_color=SIDEBAR_BUTTON_BG_COLOR, corner_radius=5, hover=False,
                                        command=close_chat_session)

        self.close_chat_tab.grid(row=0, column=1, padx=(5, 2), pady=(3, 3), sticky="e")

        try:
            for k in self.chat_conversation_row:
                k[0].grid_forget()
                k[0].grid(row=(k[1] + 1), column=0, pady=5, padx=0, sticky="ew")
                self.chat_conversation_row[self.chat_conversation_row.index(k)] = (k[0], k[1] + 1, k[2])  # Update chat_conversation_row

        except Exception as e:
            pass#print(e)  # this is just a warning

        frame_holder.grid(row=0, column=0, pady=5, padx=0, sticky="ew")

        self.chat_conversation.insert(0, frame_holder)  # Insert at the beginning of the list
        self.chat_conversation_row.insert(0, (frame_holder, 0, frame_holder_chatbox))  # Insert at the beginning of the list (name, updated row, chatbox)
    



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
        self.seperator = c.CTkButton(self, fg_color="#CCCCCC", height=3,text="", corner_radius=40, hover=False, state="disabled")
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


        
