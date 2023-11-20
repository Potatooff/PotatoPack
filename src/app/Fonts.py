from customtkinter import FontManager
from src.utils.paths import *


# Load Fonts
for font in [font_nunito, font_pacifico, font_quicksand, font_roboto, font_raleway, font_montserrat, font_ArchitectsDaughter]:
    FontManager.load_font(font)

# App use font variables to use fonts file
font_nunito_var = "Nunito"
font_pacifico_var = "Pacifico"
font_quicksand_var = "Quicksand"
font_roboto_var = "Roboto"
font_raleway_var = "Raleway Medium"
font_montserrat_var = "Montserrat"
font_ArchitectsDaughter_var = "Architects Daughter"