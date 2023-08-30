import pygame
import PySimpleGUI as sg

# Initialisation de Pygame
pygame.init()

# Paramètres de l'écran
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interface en 2D")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialisation de PySimpleGUI
sg.theme("DefaultNoMoreNagging")

# Création de la première fenêtre
layout = [[sg.Button("Login", key="-LOGIN-")]]
window1 = sg.Window("Première Surface", layout, finalize=True)

# Boucle principale
while True:
    event1, values1 = window1.read()

    if event1 == sg.WIN_CLOSED:
        break
    elif event1 == "-LOGIN-":
        window1.hide()

        # Création de la deuxième fenêtre
        layout2 = [
            [sg.Image(filename="", key="-IMAGE-"), sg.Button("OK", key="-OK-")]
        ]
        window2 = sg.Window("Deuxième Surface", layout2, finalize=True)

        # Boucle de la deuxième fenêtre
        while True:
            event2, values2 = window2.read()

            if event2 == sg.WIN_CLOSED:
                window2.close()
                window1.un_hide()
                break
            elif event2 == "-OK-":
                window2.close()

                # Création de la troisième fenêtre
                layout3 = [[sg.Text("Troisième Surface", text_color="white")]]
                window3 = sg.Window(
                    "Troisième Surface",
                    layout3,
                    finalize=True,
                    background_color=RED,
                )

                # Attente de la fermeture de la troisième fenêtre
                window3.read()
                window3.close()

                window1.un_hide()

# Fermeture de Pygame
pygame.quit()
