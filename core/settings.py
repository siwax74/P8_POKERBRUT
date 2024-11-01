######################################################################################################################
################################################# SETTINGS.PY ########################################################
######################################################################################################################

from pathlib import Path

# BASE_DIR définit le répertoire racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

# Paramètres de l'interface
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 853
BACKGROUND_COLOR = "#00083f"
BACKGROUND_IMAGE = BASE_DIR / "medias/images/background.jpg"
FONT_COLOR = "#ffffff"
BUTTON_WIDTH = 15
BUTTON_HEIGHT = 2
BUTTON_COLOR = "#4CAF50"
BUTTON_TEXT_COLOR = "#FFFFFF"
LABEL_COLOR = "#333333"
ENTRY_COLOR = "#FFFFFF"
ENTRY_TEXT_COLOR = "#000000"
HIGHLIGHT_COLOR = "#007BFF"

# Section installation
LABEL_INSTALLATION_TEXT = "Ceci est le text de l'installation, qui sera affiché dans la fenêtre de l'installation"
LABEL_INSTALLATION_BACKGROUND = "#00083f"
LABEL_INSTALLATION_WIDTH = 50
LABEL_INSTALLATION_HEIGHT = 30


# Medias
IMAGE_NAV_1 = BASE_DIR / "medias/images/image1.jpg"
IMAGE_NAV_2 = BASE_DIR / "medias/images/image2.png"
IMAGE_NAV_3 = BASE_DIR / "medias/images/image3.jpg"
ICON_GITHUB = BASE_DIR / "medias/icons/github.png"
ICON_CARDS = BASE_DIR / "medias/icons/cartes.png"
ICON_CARDS_WIDTH = 512
ICON_CARDS_HEIGHT = 512
ICON_WIDTH = 50
ICON_HEIGHT = 50

# Polices
FONT = ("Arial", 12)
BUTTON_FONT = ("Arial", 12, "bold")
LABEL_FONT = ("Arial", 12)
TITLE_FONT = ("Arial", 16, "bold")

# Marges et espacements
PADDING = 10
BUTTON_PADDING = 5
LABEL_PADDING = 5

# Styles de widgets
BUTTON_STYLE = "flat"
ENTRY_STYLE = "normal"
LABEL_STYLE = "normal"

# Comportement de la fenêtre
RESIZABLE = False
TITLE = "POKERBRUT"
TITLE_COLOR = "#4a4a4a"  # Couleur du texte du titre
TITLE_FONT = ("Helvetica", 24, "bold")  # Police, taille et style du titre
TITLE_PADDING = 20  # Espacement autour du titre
ICON_PATH = BASE_DIR / "medias" / "icons" / "icon_exe.ico"

# Autres paramètres
DEFAULT_CURSOR = "arrow"
TOOLTIP_DELAY = 500  # Millisecondes
STATUSBAR_HEIGHT = 20

# Chemins des ressources
IMAGES_DIR = BASE_DIR / "medias" / "images"
SOUNDS_DIR = BASE_DIR / "medias" / "sounds"

# Configuration des messages
ERROR_COLOR = "#FF0000"
SUCCESS_COLOR = "#00FF00"
WARNING_COLOR = "#FFA500"

# Configuration de la grille
GRID_COLUMNS = 12
GRID_ROWS = 8

# Animation
ANIMATION_SPEED = 200  # Millisecondes

# Thèmes
DARK_THEME = {
    "background": "#00083f",  # Couleur de fond
    "fg": "#FFFFFF",  # Couleur du texte
    "title_bg": "#0078d7",
}

LIGHT_THEME = {
    "background": "#FFFFFF",  # Couleur de fond
    "fg": "#FFFFFF",  # Couleur du texte
}

# Configuration par défaut
CURRENT_THEME = DARK_THEME

# Paramètres de debug
DEBUG = True
LOG_LEVEL = "INFO"

######################################################################################################################
