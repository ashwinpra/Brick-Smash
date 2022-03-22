import pygame
from pygame.locals import *
from english_words import english_words_set
pygame.init()
screen = pygame.display.set_mode((500,700))
pygame.display.set_caption("Wordle V2")

fps = 60 
clock = pygame.time.Clock()

# make a UI window:
    # show an instructions page first 
    # add box for letter in real time as user enters letter
    # if word is invalid, display error
    # display green and yellow like wordle, also green and yellow for number of letters
    # once the user guesses the word, give them a congrats, share option (?) and choice to play again

run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()