from PIL import Image
from src.utils.paths import *
from customtkinter import CTkImage



def _Load_Images(path, sizes: tuple[int, int] = None) -> CTkImage:
    """ LOAD IMAGES TO MEMORY FOR UI"""
    return CTkImage(Image.open((path)), size=sizes)



# icons vars
new_chat_icon: CTkImage = _Load_Images(image_new_chat, sizes=(22, 22))
send_message_icon: CTkImage = _Load_Images(image_send_message, sizes=(28, 28))
close_sidebar_icon: CTkImage = _Load_Images(image_close_sidebar, sizes=(17, 17))
user_icon: CTkImage = _Load_Images(image_user, sizes=(30, 30))
settings_icon: CTkImage = _Load_Images(image_settings, sizes=(20, 20))
potato_icon: CTkImage = _Load_Images(image_potato, sizes=(23, 23))
open_sidebar_icon: CTkImage = _Load_Images(image_open_sidebar, sizes=(17, 17))
send_queries_icon: CTkImage = _Load_Images(image_send_queries, sizes=(17, 17))
home_icon: CTkImage = _Load_Images(image_home, sizes=(20, 20))
dustbin_icon: CTkImage = _Load_Images(image_dustbin, sizes=(20, 20))
ai_icon: CTkImage = _Load_Images(image_ai, sizes=(20, 20))
cpu_icon: CTkImage = _Load_Images(image_cpu, sizes=(20, 20))
french_fries_icon: CTkImage = _Load_Images(image_french_fries, sizes=(35, 35))
user_settings_icon: CTkImage = _Load_Images(image_user_settings, sizes=(35, 35))
about_icon: CTkImage = _Load_Images(image_about, sizes=(35, 35))
help_icon: CTkImage = _Load_Images(image_help, sizes=(35, 35))




# images vars


# image test
test_image: CTkImage = _Load_Images(image_test, sizes=(256, 256))