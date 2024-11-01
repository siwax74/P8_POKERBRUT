from app.views.main_view import View
from core.settings import CURRENT_THEME, ICON_PATH, RESIZABLE, TITLE, WINDOW_HEIGHT, WINDOW_WIDTH


class FrameControllerInit:
    def __init__(self, root):
        self.root = root

    def init_param_main_view(self):
        # Configuration de la fenêtre principale
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title(TITLE)
        if ICON_PATH.exists():
            print("Icône trouvée :", ICON_PATH)
            self.root.iconbitmap(ICON_PATH)
        self.root.resizable(RESIZABLE, RESIZABLE)
        self.root.configure(bg=CURRENT_THEME["background"])
        return True


class FrameController:
    def __init__(self, frame_controller_init):
        self.root = frame_controller_init.root
        self.frame_controller_init = frame_controller_init
        self.view = View(self.root, self)

    def load_main_view(self):
        return self.view.display_main_view()

    def on_button_click_1(self):
        print("Bouton 1 cliqué!")

    def on_button_click_2(self):
        print("Bouton 2 cliqué!")

    def on_button_click_3(self):
        print("Bouton 3 cliqué!")
