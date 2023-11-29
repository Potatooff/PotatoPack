# Libraries Import
import customtkinter as c
from typing import Tuple, Optional
from random import randint as random_int

# Files Import
from src.app.components.shared import BG_COLOR
from src.app.components.viewer import Window_ImageViewer
from src.app.components.DefaultChat import Component_Welcome_Screen_Label
from src.app.Fonts import (font_ArchitectsDaughter_var,
                           font_nunito_var,
                           font_quicksand_var
                          )
from src.app.Images import (user_icon, 
                            dustbin_icon, 
                            cpu_icon,
                            image_test,
                            ai_icon, 
                            test_image,
                            test_image_width,
                            test_image_height,
                            Load_Images
                           )



from src.database.History import Database_ChatHistory

class Component_Chat_History(c.CTkFrame):

    def __init__(
            self, 
            master: any, 
            message_history,
            chatNAME: None | str,
            item_list: list[tuple[str | None, bool | None]] = [],
            **kwargs
    ) -> None:
        
        super().__init__(
            master,
            **kwargs
        )

        self.chat_history_file_path: str = message_history

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
        self.chat_blocks_list: list[tuple[Optional[c.CTkFrame], Optional[str]]] = []

        self.ImageViewer: Optional[Window_ImageViewer] = None

        # MAIN GRID LAYOUT
        self.main.grid_rowconfigure((0, 1), weight=0)
        self.main.grid_columnconfigure(0,weight=1)

        self.Load_messages(chat_name=chatNAME)


    def add_user_message(self, message: str) -> None:

        def delete_message() -> None:
            for i in self.chat_blocks_list:
                if i[0] == container:
                    i[0].destroy()
                    self.chat_blocks_list.remove(i)
                    Database_ChatHistory(self.chat_history_file_path).delete_user_query(chat_name=chatName)
                    break

            container.destroy()
            if self.chat_blocks_list == []:
                frame_title.grid_forget()
                self.bg.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
                self.bg_bool: bool = True

        if self.bg:
            frame_title: c.CTkFrame = c.CTkFrame(self, fg_color=BG_COLOR)
            frame_title.grid(row=0, column=0, padx=0, pady=0, sticky="new")


            # grid layout frame_title
            frame_title.grid_columnconfigure(0, weight=1)
            frame_title.grid_rowconfigure((0, 1), weight=1)

            information: c.CTkLabel = c.CTkLabel(frame_title, text="PotatoGPT model v1.0.0", font=(font_nunito_var, 16), fg_color=BG_COLOR, text_color="#CCCCCC")
            information.grid(row=0, column=0, padx=20, pady=(3, 0), sticky="nsew")


            seperator2: c.CTkButton = c.CTkButton(frame_title, fg_color="#CCCCCC", height=3, text="", corner_radius=40, hover=False, state="disabled",
                                     width=1400)
            seperator2.grid(row=1, column=0, padx=0, pady=(5, 5), sticky="sew")
            self.bg.grid_forget()
            self.bg_bool: bool = False

            # MAIN GRID LAYOUT
            self.main.grid_columnconfigure(0, weight=1)
            self.main.grid_rowconfigure(0, weight=0)  # Only one row at the top
        

        # add message to chat history
        chatName = Database_ChatHistory(self.chat_history_file_path).add_user_query(message)

        container: c.CTkFrame = c.CTkFrame(self.main, corner_radius=10, fg_color=BG_COLOR)
        container.grid(row=0, column=0, pady=12, padx=10, sticky="new")

        self.chat_blocks_list.append((container, "None"))

        # Container Grid Layout
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure((0, 2), weight=0)
        container.grid_columnconfigure(1, weight=1)

        # Image profile
        user_profile_image: c.CTkLabel = c.CTkLabel(container, image=user_icon, corner_radius=10, fg_color=BG_COLOR, text="", width=30)
        user_profile_image.grid(row=0, column=0, padx=(5, 0), pady=0, sticky="nw")


        # Message
        user_query: c.CTkLabel = c.CTkLabel(container, font=(font_nunito_var, 16), fg_color=BG_COLOR, text_color="#CCCCCC", text=message,
                                justify="left", anchor="w")
        user_query.grid(row=0, column=1, padx=(5, 5), pady=0, sticky="nsew")


        # Option
        button_delete_msg: c.CTkButton = c.CTkButton(container, text="", fg_color=BG_COLOR, corner_radius=10, border_width=0, hover=False,
                                        width=30, height=30, command=delete_message, image=dustbin_icon)
        button_delete_msg.grid(row=0, column=2, padx=(0, 5), pady=0, sticky="ne")



        try:
            row: int = 0
            for i in self.chat_blocks_list:
                i[0].grid_forget()
                i[0].grid(row=row, column=0, pady=7, padx=10, sticky="new")
                row += 1

            del row
            self.add_bot_message(chatname=chatName, message=message, image=test_image)

        except Exception as e:
            print(e)

        


    def add_bot_message(self, chatname: str, message: str, image: any = None) -> None:

        def open_image() -> None:
            if self.ImageViewer is None or not self.ImageViewer.winfo_exists():
                # TODO: modify this line lol
                self.ImageViewer: Window_ImageViewer = Window_ImageViewer(image2view=Load_Images(image_test, sizes=(test_image_width, test_image_height)), width_image=test_image_width, height_image=test_image_height)  # create window if its None or destroyed
            else:
                self.ImageViewer.focus()  # if window exists focus it


        def delete_message() -> None:
            for i in self.chat_blocks_list:
                if i[0] == container2:
                    i[0].destroy()
                    self.chat_blocks_list.remove(i)
                    Database_ChatHistory(self.chat_history_file_path).delete_chat_response(chat_name=chatname)
                    break

            container2.destroy()
            if self.chat_blocks_list == []:
                frame_title.grid_forget()
                self.bg.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
                self.bg_bool = True

        if self.bg:
            frame_title: c.CTkFrame = c.CTkFrame(self, fg_color=BG_COLOR)
            frame_title.grid(row=0, column=0, padx=0, pady=0, sticky="new")

            # grid layout frame_title
            frame_title.grid_columnconfigure(0, weight=1)
            frame_title.grid_rowconfigure((0, 1), weight=1)

            information: c.CTkLabel = c.CTkLabel(frame_title, text="PotatoGPT model v1.0.0", font=(font_quicksand_var, 16), fg_color=BG_COLOR, text_color="#CCCCCC")
            information.grid(row=0, column=0, padx=20, pady=(3, 0), sticky="nsew")


            seperator2: c.CTkButton = c.CTkButton(frame_title, fg_color="#CCCCCC", height=3, text="", corner_radius=40, hover=False, state="disabled",
                                     width=1400)
            seperator2.grid(row=1, column=0, padx=0, pady=(5, 5), sticky="sew")
            self.bg.grid_forget()
            self.bg_bool: bool = False

            # MAIN GRID LAYOUT
            self.main.grid_columnconfigure(0, weight=1)
            self.main.grid_rowconfigure(0, weight=0)  # Only one row at the top
        


        container2: c.CTkFrame = c.CTkFrame(self.main, fg_color="#444654")
        container2.grid(row=0, column=0, pady=12, padx=0, sticky="new")

        self.chat_blocks_list.append((container2, "none"))

        # Container Grid Layout
        container2.grid_rowconfigure(0, weight=1)
        container2.grid_columnconfigure((0, 2), weight=0)
        container2.grid_columnconfigure(1, weight=1)

        # Image profile
        bot_profile_image: c.CTkLabel = c.CTkLabel(container2, image=cpu_icon, corner_radius=10, fg_color="#444654", text="", width=30)
        bot_profile_image.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nw")


        # Message
        if not image:
            bot_answer: c.CTkLabel = c.CTkLabel(container2, font=(font_nunito_var, 16), fg_color="#444654", text_color="#CCCCCC", text=message,
                                    justify="left", anchor="w")
            bot_answer.grid(row=0, column=1, padx=(8, 5), pady=10, sticky="nsew")

            # add message to chat history
            Database_ChatHistory(self.chat_history_file_path).add_chatbot_response(chat_name=chatname, chatbot_response=message)

        else:

            # add message to chat history
            Database_ChatHistory(self.chat_history_file_path).add_chatbot_response(chat_name=chatname, chatbot_response=[message, image_test])


            container2.grid_rowconfigure((0, 1), weight=1)

            bot_answer: c.CTkLabel = c.CTkLabel(container2, font=(font_nunito_var, 16), fg_color="#444654", text_color="#CCCCCC", text=message,
                                    justify="left", anchor="w")
            bot_answer.grid(row=0, column=1, padx=(8, 5), pady=(0, 0), sticky="nsew")

            bot_image: c.CTkButton = c.CTkButton(container2, image=image, corner_radius=10, fg_color="#444654", text="", compound="left", anchor="w",
                                    command=open_image, hover=False)
            bot_image.grid(row=1, column=1, padx=(8, 5), pady=(5, 10), sticky="nsew")



        # Option
        button_delete_msg: c.CTkButton = c.CTkButton(container2, text="", fg_color="#444654", corner_radius=10, border_width=0, hover=False,
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
            
    def Load_messages(self, chat_name: str) -> None:
        try:
            chat_history = Database_ChatHistory(self.chat_history_file_path).get_all_message_in_list()
            for i in chat_history:
                try:
                    if i["user_query"] != "":
                        self.Load_user_message(i["user_query"], chatName=chat_name)
                    
                    try:
                        if i["chatbot_response"][1]:
                            foo_image = Load_Images(i["chatbot_response"][1], sizes=(256, 256))
                            self.Load_bot_message(chatname=chat_name, message=i["chatbot_response"][0],
                                                 image=foo_image)
                    except Exception as e:
                        print(e)
                        if i["chatbot_response"][0]:
                            self.Load_bot_message(chatname=chat_name, message=i["chatbot_response"][0])

                except Exception as e:
                     print(e)
        except Exception as e:
            print(e)



    def Load_user_message(self, message: str, chatName) -> None:

        def delete_message() -> None:
            for i in self.chat_blocks_list:
                if i[0] == container:
                    i[0].destroy()
                    self.chat_blocks_list.remove(i)
                    Database_ChatHistory(self.chat_history_file_path).delete_user_query(chat_name=chatName)
                    break

            container.destroy()
            if self.chat_blocks_list == []:
                frame_title.grid_forget()
                self.bg.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
                self.bg_bool: bool = True

        if self.bg:
            frame_title: c.CTkFrame = c.CTkFrame(self, fg_color=BG_COLOR)
            frame_title.grid(row=0, column=0, padx=0, pady=0, sticky="new")


            # grid layout frame_title
            frame_title.grid_columnconfigure(0, weight=1)
            frame_title.grid_rowconfigure((0, 1), weight=1)

            information: c.CTkLabel = c.CTkLabel(frame_title, text="PotatoGPT model v1.0.0", font=(font_nunito_var, 16), fg_color=BG_COLOR, text_color="#CCCCCC")
            information.grid(row=0, column=0, padx=20, pady=(3, 0), sticky="nsew")


            seperator2: c.CTkButton = c.CTkButton(frame_title, fg_color="#CCCCCC", height=3, text="", corner_radius=40, hover=False, state="disabled",
                                     width=1400)
            seperator2.grid(row=1, column=0, padx=0, pady=(5, 5), sticky="sew")
            self.bg.grid_forget()
            self.bg_bool: bool = False

            # MAIN GRID LAYOUT
            self.main.grid_columnconfigure(0, weight=1)
            self.main.grid_rowconfigure(0, weight=0)  # Only one row at the top
        

        container: c.CTkFrame = c.CTkFrame(self.main, corner_radius=10, fg_color=BG_COLOR)
        container.grid(row=0, column=0, pady=12, padx=10, sticky="new")

        self.chat_blocks_list.append((container, "None"))

        # Container Grid Layout
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure((0, 2), weight=0)
        container.grid_columnconfigure(1, weight=1)

        # Image profile
        user_profile_image: c.CTkLabel = c.CTkLabel(container, image=user_icon, corner_radius=10, fg_color=BG_COLOR, text="", width=30)
        user_profile_image.grid(row=0, column=0, padx=(5, 0), pady=0, sticky="nw")


        # Message
        user_query: c.CTkLabel = c.CTkLabel(container, font=(font_nunito_var, 16), fg_color=BG_COLOR, text_color="#CCCCCC", text=message,
                                justify="left", anchor="w")
        user_query.grid(row=0, column=1, padx=(5, 5), pady=0, sticky="nsew")


        # Option
        button_delete_msg: c.CTkButton = c.CTkButton(container, text="", fg_color=BG_COLOR, corner_radius=10, border_width=0, hover=False,
                                        width=30, height=30, command=delete_message, image=dustbin_icon)
        button_delete_msg.grid(row=0, column=2, padx=(0, 5), pady=0, sticky="ne")



        try:
            row: int = 0
            for i in self.chat_blocks_list:
                i[0].grid_forget()
                i[0].grid(row=row, column=0, pady=7, padx=10, sticky="new")
                row += 1

            del row

        except Exception as e:
            print(e)


    def Load_bot_message(self, chatname: str, message: str, image: any = None) -> None:

        def open_image() -> None:
            if self.ImageViewer is None or not self.ImageViewer.winfo_exists():
                # TODO: modify this line lol
                self.ImageViewer: Window_ImageViewer = Window_ImageViewer(image2view=Load_Images(image_test, sizes=(test_image_width, test_image_height)), width_image=test_image_width, height_image=test_image_height)  # create window if its None or destroyed
            else:
                self.ImageViewer.focus()  # if window exists focus it


        def delete_message() -> None:
            for i in self.chat_blocks_list:
                if i[0] == container2:
                    i[0].destroy()
                    self.chat_blocks_list.remove(i)
                    Database_ChatHistory(self.chat_history_file_path).delete_chat_response(chat_name=chatname)
                    break

            container2.destroy()
            if self.chat_blocks_list == []:
                frame_title.grid_forget()
                self.bg.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
                self.bg_bool = True

        if self.bg:
            frame_title: c.CTkFrame = c.CTkFrame(self, fg_color=BG_COLOR)
            frame_title.grid(row=0, column=0, padx=0, pady=0, sticky="new")

            # grid layout frame_title
            frame_title.grid_columnconfigure(0, weight=1)
            frame_title.grid_rowconfigure((0, 1), weight=1)

            information: c.CTkLabel = c.CTkLabel(frame_title, text="PotatoGPT model v1.0.0", font=(font_quicksand_var, 16), fg_color=BG_COLOR, text_color="#CCCCCC")
            information.grid(row=0, column=0, padx=20, pady=(3, 0), sticky="nsew")


            seperator2: c.CTkButton = c.CTkButton(frame_title, fg_color="#CCCCCC", height=3, text="", corner_radius=40, hover=False, state="disabled",
                                     width=1400)
            seperator2.grid(row=1, column=0, padx=0, pady=(5, 5), sticky="sew")
            self.bg.grid_forget()
            self.bg_bool: bool = False

            # MAIN GRID LAYOUT
            self.main.grid_columnconfigure(0, weight=1)
            self.main.grid_rowconfigure(0, weight=0)  # Only one row at the top
        


        container2: c.CTkFrame = c.CTkFrame(self.main, fg_color="#444654")
        container2.grid(row=0, column=0, pady=12, padx=0, sticky="new")

        self.chat_blocks_list.append((container2, "none"))

        # Container Grid Layout
        container2.grid_rowconfigure(0, weight=1)
        container2.grid_columnconfigure((0, 2), weight=0)
        container2.grid_columnconfigure(1, weight=1)

        # Image profile
        bot_profile_image: c.CTkLabel = c.CTkLabel(container2, image=cpu_icon, corner_radius=10, fg_color="#444654", text="", width=30)
        bot_profile_image.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nw")


        # Message
        if not image:
            bot_answer: c.CTkLabel = c.CTkLabel(container2, font=(font_nunito_var, 16), fg_color="#444654", text_color="#CCCCCC", text=message,
                                    justify="left", anchor="w")
            bot_answer.grid(row=0, column=1, padx=(8, 5), pady=10, sticky="nsew")


        else:

            container2.grid_rowconfigure((0, 1), weight=1)

            bot_answer: c.CTkLabel = c.CTkLabel(container2, font=(font_nunito_var, 16), fg_color="#444654", text_color="#CCCCCC", text=message,
                                    justify="left", anchor="w")
            bot_answer.grid(row=0, column=1, padx=(8, 5), pady=(0, 0), sticky="nsew")

            bot_image: c.CTkButton = c.CTkButton(container2, image=image, corner_radius=10, fg_color="#444654", text="", compound="left", anchor="w",
                                    command=open_image, hover=False)
            bot_image.grid(row=1, column=1, padx=(8, 5), pady=(5, 10), sticky="nsew")



        # Option
        button_delete_msg: c.CTkButton = c.CTkButton(container2, text="", fg_color="#444654", corner_radius=10, border_width=0, hover=False,
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