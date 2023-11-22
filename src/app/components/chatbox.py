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
                                               fg_color=chat_box_chat_entry_BG_COLOR, wrap="word", tabs=2)
        
        self.user_input_text_box.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # This is button to send input
        self.user_input_send_button = c.CTkButton(self, text=" ", width=50, height=45, image=send_message_icon, corner_radius=10, fg_color=BG_COLOR,
                                                  hover=False, command=self.user_input_send_button_on_click)
        self.user_input_send_button.grid(row=0, column=1, padx=(5, 20),pady=(20, 0))
        

        # This is warning text
        self.user_warning_text = c.CTkLabel(self, text=warning_message_for_user, text_color="#CCCCCC", font=(font_montserrat_var, 14))
        self.user_warning_text.grid(row=1, column=0, columnspan=2, padx=0, pady=(5, 5), sticky="nsew")

        # ChatBox shortcuts

        self.user_input_text_box.bind("<Return>", self.user_input_send_button_on_click)
        self.user_input_text_box.bind("<Tab>", self.insert_tab)
        self.user_input_text_box.bind("<Shift-Return>", self.user_input_text_box_newline)

    def insert_tab(self, event):
        text = event.widget
        text.insert(c.INSERT, "    ")  # Insert four spaces for each press of the Tab key
        return 'break'
    
    def user_input_text_box_newline(self, event):
        text = event.widget
        text.insert(c.INSERT, "\n")

    def get_user_input(self) -> str:
        return self.user_input_text_box.get("1.0", "end-1c")
    

    def clear_user_input(self) -> None:
        self.user_input_text_box.delete("0.0", 'end')



    def get_actual_chat_history(self):
        start_row, rowspan = 0, 5
        widgets_in_range = [self.master.grid_slaves(row=0, column=1) for row in range(start_row, start_row + rowspan)]
        widgets_in_range = [widget for sublist in widgets_in_range for widget in sublist]
        if widgets_in_range:
            return widgets_in_range
            


    def user_input_send_button_on_click(self, event = None) -> None:
        inp: str = self.get_user_input()

        if inp is not None and inp != "" and inp != "\n" and inp.strip():
            self.clear_user_input()
            print(inp)

            chat_history = self.get_actual_chat_history()
            if chat_history:
                if chat_history[0] != self.master.default_chat_history:

                    chat_history[0].add_user_message(message=inp)
                
                else:
                    self.master.default_chat_history.grid_forget()
                    self.master.window_sidebar.new_chat_button_on_click()
                    chat_history = self.get_actual_chat_history()
                    if chat_history:
                        chat_history[0].add_user_message(message=str(inp))
        
            