import pygame

pygame.init()

ecran = pygame.display.set_mode((900, 700))
zeecran=pygame.image.load("ecran.png").convert_alpha()

continuer = True
#200,193
while continuer:
    ecran.blit(zeecran, (0,0 ))
  
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()

pygame.quit()
