import pygame 
import time
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Game")

# colors are defined as a tuple like (R,G,B) (0-255)
yellow = (255,255,0)
screen.fill(yellow)
pygame.display.update()
time.sleep(10)
pygame.quit()
