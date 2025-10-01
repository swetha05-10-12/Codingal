import pygame

pygame.init()
SCREEN_WIDTH , SCREEN_HEIGHT= 500 , 500

display_surface=pygame.display.set_mode(SCREEN_WIDTH,SCREEN_HEIGHT)
pygame.display.set_caption("Adding imga e and background image")

background_image= pygame.transfrom.scale(
    pygame.image.load('background.png').convert(),
    (SCREEN_WIDTH,SCREEN_HEIGHT)
)

penguin_image=pygame.transform.scale(
    pygame.image.load("hello penquin.png").convert_alpha(), (200),200)
penguin_rect=penquin_image.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2-30))

text =pygame.font.Font(None,36).render('Hello world')