import pygame
from pygame.locals import *
# The pygame.locals module contains some 280 constants used and defined by pygame
# now instead of using pygame.KEYDOWN/K_<key> we can directly use KEYDOWN/K_<key>
# we can get the key pressed by user and give approppriate output based on it 
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Game")


# colors are defined as a tuple like (R,G,B) (0-255)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
background = BLACK
key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE, K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
           
            # if event.key == K_r:
            #     background = red
            # elif event.key == K_g:
            #     background = green
            # elif event.key == K_b:
            #     background = blue
            # #instead of using so many if loops, we can make use of dict
            if event.key in key_dict:
                background = key_dict[event.key]
            elif event.key == K_ESCAPE:
                pygame.quit()

    screen.fill(background)
    pygame.display.update()


