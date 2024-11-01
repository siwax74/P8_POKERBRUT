######################################################################################################################
##################################################### MAIN.PY ########################################################
######################################################################################################################
import tkinter as tk
from app.controllers.main_controllers import MainController


def start_app():
    """Initialisation du controller app/controllers/main_controller.py"""

    root = tk.Tk()
    app = MainController(root)
    app.run()


if __name__ == "__main__":
    app_start = start_app()
