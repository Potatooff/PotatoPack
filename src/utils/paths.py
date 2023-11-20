import os

src_path = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))

data_path = os.path.join(src_path, "data")

data_assets_path = os.path.join(data_path, "assets")

data_fonts_path = os.path.join(data_path, "fonts")



# Image paths
image_new_chat = os.path.join(data_assets_path, "new_chat.png")
image_send_message = os.path.join(data_assets_path, "send_message.png")
image_close_sidebar = os.path.join(data_assets_path, "close_sidebar.png")
image_user = os.path.join(data_assets_path, "user.png")
image_settings = os.path.join(data_assets_path, "settings.png")
image_potato = os.path.join(data_assets_path, "potato.png")
image_open_sidebar = os.path.join(data_assets_path, "open_sidebar.png")
image_send_queries = os.path.join(data_assets_path, "send_queries.png")
image_home = os.path.join(data_assets_path, "home.png")
image_waiting = os.path.join(data_assets_path, "waiting.png")


# Font paths
font_nunito = os.path.join(data_fonts_path, "Nunito-Regular.ttf")
font_pacifico = os.path.join(data_fonts_path, "Pacifico-Regular.ttf")
font_quicksand = os.path.join(data_fonts_path, "Quicksand-Regular.ttf")
font_roboto = os.path.join(data_fonts_path, "Roboto-Regular.ttf")
font_raleway = os.path.join(data_fonts_path, "Raleway-Medium.ttf")
font_montserrat = os.path.join(data_fonts_path, "Montserrat-Regular.ttf")
font_ArchitectsDaughter = os.path.join(data_fonts_path, "ArchitectsDaughter-Regular.ttf")
