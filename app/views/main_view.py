######################################################################################################################
################################################# MAIN_VIEW.PY #######################################################
######################################################################################################################
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
from core.settings import (
    BACKGROUND_COLOR,
    BUTTON_COLOR,
    BUTTON_FONT,
    BUTTON_HEIGHT,
    BUTTON_PADDING,
    BUTTON_STYLE,
    BUTTON_TEXT_COLOR,
    BUTTON_WIDTH,
    FONT_COLOR,
    ICON_CARDS,
    ICON_CARDS_HEIGHT,
    ICON_CARDS_WIDTH,
    ICON_GITHUB,
    ICON_HEIGHT,
    ICON_WIDTH,
    LABEL_FONT,
    LABEL_INSTALLATION_BACKGROUND,
    LABEL_INSTALLATION_HEIGHT,
    LABEL_INSTALLATION_WIDTH,
    TITLE,
    TITLE_COLOR,
    TITLE_FONT,
    TITLE_PADDING,
)


class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

    def display_main_view(self):
        # Ajoute une colonne de poids pour décaler les boutons vers la droite
        self.root.grid_columnconfigure(0, weight=1)

        # Label avec le nom de l'application
        app_name_label = tk.Label(
            self.root,
            text=TITLE,  # Remplacez par votre variable TITLE si nécessaire
            font=TITLE_FONT,
            bg=BACKGROUND_COLOR,
            fg=TITLE_COLOR,
            padx=TITLE_PADDING,
            pady=TITLE_PADDING,
            relief="raised",  # Ajouter un relief pour un effet 3D
            bd=2,  # Épaisseur de la bordure
        )
        app_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # Positionner à gauche

        # Bouton "Démarrer"
        button1 = tk.Button(
            self.root,
            text="Démarrer",
            command=self.controller.on_button_click_1,
            bg=BUTTON_COLOR,
            fg=BUTTON_TEXT_COLOR,
            font=BUTTON_FONT,
            relief=BUTTON_STYLE,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
        )
        button1.grid(row=0, column=1, padx=BUTTON_PADDING, pady=BUTTON_PADDING, sticky="e")

        # Bouton "Options"
        button2 = tk.Button(
            self.root,
            text="Options",
            command=self.controller.on_button_click_2,
            bg=BUTTON_COLOR,
            fg=BUTTON_TEXT_COLOR,
            font=BUTTON_FONT,
            relief=BUTTON_STYLE,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
        )
        button2.grid(row=0, column=2, padx=BUTTON_PADDING, pady=BUTTON_PADDING, sticky="e")

        # Bouton "Quitter"
        button3 = tk.Button(
            self.root,
            text="Quitter",
            command=self.controller.on_button_click_3,
            bg=BUTTON_COLOR,
            fg=BUTTON_TEXT_COLOR,
            font=BUTTON_FONT,
            relief=BUTTON_STYLE,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
        )
        button3.grid(row=0, column=3, padx=BUTTON_PADDING, pady=BUTTON_PADDING, sticky="e")

        # Bouton GitHub
        github_image = Image.open(str(ICON_GITHUB))  # Open the image using Pillow
        github_image = github_image.resize((ICON_WIDTH, ICON_HEIGHT))  # Resize if necessary
        github_photo = ImageTk.PhotoImage(github_image)  # Convert to PhotoImage for Tkinter

        github_button = tk.Button(
            self.root,
            image=github_photo,
            text="GitHub",
            compound="top",  # Texte à gauche de l'image
            command=lambda: webbrowser.open("https://github.com/Siwax74"),
            bg=BACKGROUND_COLOR,
            relief="flat",
        )
        github_button.image = github_photo  # Keep a reference to avoid garbage collection
        github_button.grid(row=1, column=2, padx=5, pady=5)

        # Image carte
        card_image = Image.open(str(ICON_CARDS))  # Open the image using Pillow
        card_image = card_image.resize((ICON_CARDS_WIDTH, ICON_CARDS_HEIGHT))  # Resize if necessary
        card_photo = ImageTk.PhotoImage(card_image)  # Convert to PhotoImage for Tkinter
        # Créer un label pour afficher l'image
        label = tk.Label(self.root, image=card_photo, bg=BACKGROUND_COLOR)
        label.image = card_photo  # Keep a reference to avoid garbage collection
        label.grid(row=2, column=0, padx=5, pady=5)

        # Section Installation
        installation_label = tk.Label(
            self.root,
            text="🎉 Bienvenue dans POKERBRUT ! 🃏\n\n"
            "Votre application dédiée à l'analyse des probabilités au poker. 💰\n\n"
            "**Fonctionnalités clés** :\n"
            "**Probabilités de Gain** : Découvrez vos chances de gagner une main en temps réel ! 📈\n"
            "**Statistiques des Flops** : Analysez les cartes communes et optimisez votre stratégie. ♠️♦️♣️♥️\n"
            "**Historique des Parties** : Suivez vos performances et améliorez-vous à chaque session. 📝\n\n"
            "Prêt à plonger dans le monde des probabilités ? Appuyez sur *Démarrer* et que la chance soit avec vous !",
            bg=LABEL_INSTALLATION_BACKGROUND,
            fg=FONT_COLOR,
            relief="solid",  # Ajouter un relief pour un effet 3D
            bd=2,  # Épaisseur de la bordure
            width=LABEL_INSTALLATION_WIDTH,
            height=LABEL_INSTALLATION_HEIGHT,
            wraplength=300,  # Utilisez wraplength ici
            font=LABEL_FONT,
            anchor="n",  # Alignement en haut
            pady=50,  # Padding vertical (haut et bas)
            padx=0,  # Padding horizontal (gauche et droite)
        )
        installation_label.place(x=795, y=100)
