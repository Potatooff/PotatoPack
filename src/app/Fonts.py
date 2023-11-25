from customtkinter import FontManager
from src.utils.paths import *


# Load Fonts
for font in [font_nunito, font_pacifico, font_quicksand, font_roboto, font_raleway, font_montserrat, font_ArchitectsDaughter]:
    FontManager.load_font(font)

# App use font variables to use fonts file
font_nunito_var: str = "Nunito"
font_pacifico_var: str = "Pacifico"
font_quicksand_var: str = "Quicksand"
font_roboto_var: str = "Roboto"
font_raleway_var: str = "Raleway Medium"
font_montserrat_var: str = "Montserrat"
font_ArchitectsDaughter_var: str = "Architects Daughter"