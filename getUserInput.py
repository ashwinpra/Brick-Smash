import pygame 
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            print(event)

pygame.quit()