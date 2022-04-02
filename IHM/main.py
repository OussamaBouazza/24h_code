import pygame
import sys
import requests
from 

class Grille:
    def __init__(self):
        self




class Jeu:
    def __init__(self):
        self.ecran=pygame.display.set_mode(1000,700)
        pygame.display.set_caption('Space Travellers')
        self.jeu_en_cours=True

    def fonction_principale(self):
        while self.jeu_en_cours:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()

if __name__ =='__main__':
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()


    