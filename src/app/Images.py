from PIL import Image
from src.utils.paths import *
from customtkinter import CTkImage

def _Load_Images(path, sizes: tuple[int, int] = None):
    """ LOAD IMAGES TO MEMORY FOR UI"""
    return CTkImage(Image.open((path)), size=sizes)



# icons vars
new_chat_icon = _Load_Images(image_new_chat, sizes=(22, 22))
send_message_icon = _Load_Images(image_send_message, sizes=(28, 28))
close_sidebar_icon = _Load_Images(image_close_sidebar, sizes=(17, 17))
user_icon = _Load_Images(image_user, sizes=(30, 30))
settings_icon = _Load_Images(image_settings, sizes=(20, 20))
potato_icon = _Load_Images(image_potato, sizes=(23, 23))
open_sidebar_icon = _Load_Images(image_open_sidebar, sizes=(17, 17))
send_queries_icon = _Load_Images(image_send_queries, sizes=(17, 17))
home_icon = _Load_Images(image_home, sizes=(20, 20))



# images vars