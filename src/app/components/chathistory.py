import customtkinter as c
from typing import Tuple
from src.app.components.viewer import Window_ImageViewer
from src.app.components.shared import BG_COLOR
from src.app.Fonts import (font_ArchitectsDaughter_var,
                           font_nunito_var,
                           font_quicksand_var
                          )
from src.app.components.DefaultChat import Component_Welcome_Screen_Label
from src.app.Images import (user_icon, dustbin_icon, cpu_icon, ai_icon, test_image)

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

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.main = c.CTkScrollableFrame(self, fg_color=BG_COLOR)
        self.main.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")

        
        # Once created
        self.bg = Component_Welcome_Screen_Label(self.main, text="PotatoGPT on Sterium", font=(font_ArchitectsDaughter_var, 44), fg_color=BG_COLOR)
        self.bg.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.bg_bool = True

        # Chat blocs
        self.chat_blocks_list = []

        self.ImageViewer = None

        # MAIN GRID LAYOUT
        self.main.grid_rowconfigure((0, 1), weight=0)
        self.main.grid_columnconfigure(0,weight=1)

        for i, item in enumerate(item_list):
            self.add_item(item)


    def add_user_message(self, message: str) -> None:

        def delete_message() -> None:
            for i in self.chat_blocks_list:
                if i[0] == container:
                    i[0].destroy()
                    self.chat_blocks_list.remove(i)
                    break
            container.destroy()
            if self.chat_blocks_list == []:
                frame_title.grid_forget()
                self.bg.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
                self.bg_bool = True

        if self.bg:
            frame_title = c.CTkFrame(self, fg_color=BG_COLOR)
            frame_title.grid(row=0, column=0, padx=0, pady=0, sticky="new")
            # grid layout frame_title
            frame_title.grid_columnconfigure(0, weight=1)
            frame_title.grid_rowconfigure((0, 1), weight=1)

            information = c.CTkLabel(frame_title, text="PotatoGPT model v1.0.0", font=(font_nunito_var, 16), fg_color=BG_COLOR, text_color="#CCCCCC")
            information.grid(row=0, column=0, padx=20, pady=(3, 0), sticky="nsew")
            seperator2 = c.CTkButton(frame_title, fg_color="#CCCCCC", height=3, text="", corner_radius=40, hover=False, state="disabled",
                                     width=1400)
            seperator2.grid(row=1, column=0, padx=0, pady=(5, 5), sticky="sew")
            self.bg.grid_forget()
            self.bg_bool = False

            # MAIN GRID LAYOUT
            self.main.grid_columnconfigure(0, weight=1)
            self.main.grid_rowconfigure(0, weight=0)  # Only one row at the top
        

        container = c.CTkFrame(self.main, corner_radius=10, fg_color=BG_COLOR)
        container.grid(row=0, column=0, pady=12, padx=10, sticky="new")

        self.chat_blocks_list.append((container, "none"))

        # Container Grid Layout
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure((0, 2), weight=0)
        container.grid_columnconfigure(1, weight=1)

        # Image profile
        user_profile_image = c.CTkLabel(container, image=user_icon, corner_radius=10, fg_color=BG_COLOR, text="", width=30)
        user_profile_image.grid(row=0, column=0, padx=(5, 0), pady=0, sticky="nw")


        # Message
        user_query = c.CTkLabel(container, font=(font_nunito_var, 16), fg_color=BG_COLOR, text_color="#CCCCCC", text=message,
                                justify="left", anchor="w")
        user_query.grid(row=0, column=1, padx=(5, 5), pady=0, sticky="nsew")


        # Option
        button_delete_msg = c.CTkButton(container, text="", fg_color=BG_COLOR, corner_radius=10, border_width=0, hover=False,
                                        width=30, height=30, command=delete_message, image=dustbin_icon)
        button_delete_msg.grid(row=0, column=2, padx=(0, 5), pady=0, sticky="ne")



        try:
            row: int = 0
            for i in self.chat_blocks_list:
                i[0].grid_forget()
                i[0].grid(row=row, column=0, pady=7, padx=10, sticky="new")
                row += 1

            del row
            self.add_bot_message(message=message, image=test_image)

        except Exception as e:
            print(e)

        


    def add_bot_message(self, message: str, image: any = None) -> None:

        def open_image() -> None:
            if self.ImageViewer is None or not self.ImageViewer.winfo_exists():
                self.ImageViewer = Window_ImageViewer(image2view=image)  # create window if its None or destroyed
            else:
                self.ImageViewer.focus()  # if window exists focus it


        def delete_message() -> None:
            for i in self.chat_blocks_list:
                if i[0] == container2:
                    i[0].destroy()
                    self.chat_blocks_list.remove(i)
                    break
            container2.destroy()
            if self.chat_blocks_list == []:
                frame_title.grid_forget()
                self.bg.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
                self.bg_bool = True

        if self.bg:
            frame_title = c.CTkFrame(self, fg_color=BG_COLOR)
            frame_title.grid(row=0, column=0, padx=0, pady=0, sticky="new")
            # grid layout frame_title
            frame_title.grid_columnconfigure(0, weight=1)
            frame_title.grid_rowconfigure((0, 1), weight=1)

            information = c.CTkLabel(frame_title, text="PotatoGPT model v1.0.0", font=(font_quicksand_var, 16), fg_color=BG_COLOR, text_color="#CCCCCC")
            information.grid(row=0, column=0, padx=20, pady=(3, 0), sticky="nsew")
            seperator2 = c.CTkButton(frame_title, fg_color="#CCCCCC", height=3, text="", corner_radius=40, hover=False, state="disabled",
                                     width=1400)
            seperator2.grid(row=1, column=0, padx=0, pady=(5, 5), sticky="sew")
            self.bg.grid_forget()
            self.bg_bool = False

            # MAIN GRID LAYOUT
            self.main.grid_columnconfigure(0, weight=1)
            self.main.grid_rowconfigure(0, weight=0)  # Only one row at the top
        

        container2 = c.CTkFrame(self.main, fg_color="#444654")
        container2.grid(row=0, column=0, pady=12, padx=0, sticky="new")

        self.chat_blocks_list.append((container2, "none"))

        # Container Grid Layout
        container2.grid_rowconfigure(0, weight=1)
        container2.grid_columnconfigure((0, 2), weight=0)
        container2.grid_columnconfigure(1, weight=1)

        # Image profile
        bot_profile_image = c.CTkLabel(container2, image=cpu_icon, corner_radius=10, fg_color="#444654", text="", width=30)
        bot_profile_image.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nw")


        # Message
        if not image:
            bot_answer = c.CTkLabel(container2, font=(font_nunito_var, 16), fg_color="#444654", text_color="#CCCCCC", text=message,
                                    justify="left", anchor="w")
            bot_answer.grid(row=0, column=1, padx=(8, 5), pady=10, sticky="nsew")

        else:
            container2.grid_rowconfigure((0, 1), weight=1)

            bot_answer = c.CTkLabel(container2, font=(font_nunito_var, 16), fg_color="#444654", text_color="#CCCCCC", text=message,
                                    justify="left", anchor="w")
            bot_answer.grid(row=0, column=1, padx=(8, 5), pady=(10, 0), sticky="nsew")

            bot_image = c.CTkButton(container2, image=image, corner_radius=10, fg_color="#444654", text="", compound="left", anchor="w",
                                    command=open_image, hover=False)
            bot_image.grid(row=1, column=1, padx=(8, 5), pady=(5, 10), sticky="nsew")



        # Option
        button_delete_msg = c.CTkButton(container2, text="", fg_color="#444654", corner_radius=10, border_width=0, hover=False,
                                        width=30, height=30, command=delete_message, image=dustbin_icon)
        button_delete_msg.grid(row=0, column=2, padx=(0, 5), pady=10, sticky="ne")

        try:
            row: int = 0
            for i in self.chat_blocks_list:
                i[0].grid_forget()
                i[0].grid(row=row, column=0, pady=7, padx=10, sticky="new")
                row += 1

            del row

        except Exception as e:
            print(e)