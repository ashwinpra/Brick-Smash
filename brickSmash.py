import pygame
import random
from pygame.locals import *
from pygame.sprite import *
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Brick Smash')
small_font = pygame.font.Font(None, 30)
medium_font = pygame.font.Font(None, 45)
large_font = pygame.font.Font(None,75)
background = pygame.image.load("bgimg.jpeg")
background = pygame.transform.scale(background,(600,600))
WHITE = (255,255,255)
BLACK = (0,0,0)
DARKRED = (130, 8, 8)
RED = (255, 0, 0)
GREEN = (0,255,0)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
ORANGE = (255,106,0)
YELLOW = (255,255,0)
sprites = Group() #list of all sprites
bricks = Group() #list of all bricks 
lives = 3
score = 0 
click = False
running = True


def draw_text(font,text, color,x,y):
    global screen
    showText = font.render(text, 1, color)
    screen.blit(showText,(x,y))



def update_screen():
    global screen
    global sprites
    #screen.fill(BLACK)
    screen.blit(background,(0,0))
    pygame.draw.line(screen, WHITE, [0,38],[800,38],2)
    draw_text(small_font,f"Score: {score}",WHITE,20,10)
    draw_text(small_font,f"Lives: {lives}",WHITE,500,10)
    sprites.draw(screen)

def add_bricks(color,y):
    global sprites
    global bricks
    for i in range(6):
        brick = Brick(color,76.67,30)
        brick.rect.x = 20 + i* 96.67
        brick.rect.y = y
        sprites.add(brick)
        bricks.add(brick)

def new_game():
    global running
    global score
    global lives
    global bricks
    global sprites
    bricks.empty()
    sprites.empty()
    running = True
    lives = 3
    score = 0
    update_screen()
    

def game():
    new_game()
    global screen
    global lives
    global score
    global running
    global bricks
    global sprites
    bat = Bat(DARKBLUE,100,20)
    bat.rect.x, bat.rect.y=260,550
    sprites.add(bat)
    ball = Ball(WHITE,10,10)
    ball.rect.x,ball.rect.y=250,540
    sprites.add(ball)
    add_bricks(RED,60)
    add_bricks(ORANGE,110)
    add_bricks(YELLOW,160)

    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[K_d] or keys[K_RIGHT]:
            bat.move('right',7)
        elif keys[K_a] or keys[K_LEFT]:
            bat.move('left',7)

        # Checking collision of bat and ball
        if pygame.sprite.collide_mask(ball, bat):
            ball.bounce()
            

        # Checking collision of brick and ball
        collided_bricks = pygame.sprite.spritecollide(ball,bricks,False)
        for brick in collided_bricks:
            ball.bounce()
            score += 1
            brick.kill()
            if len(bricks)==0:
                draw_text(large_font,"GAME COMPLETED!",WHITE,60,300)
                draw_text(medium_font,f"Final Score = {score}",WHITE,185,350)
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False

        ball.collision()
        sprites.update()
        update_screen()
        pygame.display.flip()
        clock.tick(60)
    
def instructions():
    global screen
    global lives
    global score
    global running
    global click
    global bricks
    global sprites
    global background
    running = True
    while running:
        #screen.fill(BLACK)
        screen.blit(background, (0,0))
        draw_text(medium_font,"INSTRUCTIONS",WHITE,180,40)
        draw_text(small_font,"You have a bat which you can move to the left or right",WHITE,40,100)
        draw_text(small_font,"using the A/LEFT and D/RIGHT keys respectively.",WHITE,40,130)
        draw_text(small_font,"Using this, you have to hit the ball in order to smash",WHITE,40,180)
        draw_text(small_font,"the bricks. On smashing each brick, you get 1 point.",WHITE,40,210)
        draw_text(small_font,"If the ball hits the bottom wall, you lose a life, and",WHITE,40,260)
        draw_text(small_font,"if you lose all 3 lives, the game is over.",WHITE,40,290)
        draw_text(small_font,"The objective of the game is to smash all the bricks",WHITE,40,340)
        draw_text(small_font,"without losing all 3 of your lives.",WHITE,40,370)
        draw_text(medium_font,"Enjoy!",WHITE,245,420)

        mx, my = pygame.mouse.get_pos()
 
        button = pygame.Rect(190, 480, 200, 50)
        pygame.draw.rect(screen, LIGHTBLUE, button,4)
        draw_text(small_font,"Back to Main Menu",WHITE,195,495)

        
        if button.collidepoint((mx, my)):
            if click:
                main_menu()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.flip()
        clock.tick(60)

def exit():
    pygame.quit()

class Bat(Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect()

    # Note that rect.x gives the coordinate of the leftmost end
    def move(self,direction,pixels):
        if direction == 'right':
            self.rect.x+=pixels
            if self.rect.x>600:
                self.rect.x=-self.width #It wraps around
        else:
            self.rect.x-=pixels
            if self.rect.x+self.width<0:
                self.rect.x=700-self.width

class Ball(Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.velocity = [random.randint(3,6),random.randint(-6,6)]#x and y components of velocity
        
        while self.velocity[1]==0:
            self.velocity[1]=random.randint(-6,6) 
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x+=self.velocity[0]
        self.rect.y+=self.velocity[1]
    
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-6,6)

    def collision(self):
        global running
        global lives
        global score
        global screen
        # We will consider perfectly elastic collision with walls and 
        # randomly elastic with bat

        if self.rect.x>=590 or self.rect.x <=0:
            # x component reverses, y component remains same
            self.velocity[0] = -self.velocity[0]
        if self.rect.y>=590 :
            # y component reverses, x component remains same
            # in this case, decrease lives also
            self.velocity[1] = -self.velocity[1]
            lives-=1
            if lives==0:
                # Display game over message
                draw_text(large_font,"GAME OVER",WHITE,150,300)
                draw_text(medium_font,f"Final Score = {score}",WHITE,200,350)
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False

        if self.rect.y<=40:
            # y component reverses, x component remains same
            self.velocity[1] = -self.velocity[1]

class Brick(Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        pygame.draw.rect(self.image, BLACK, [0, 0, self.width, self.height],1)
        self.rect = self.image.get_rect()
    


def main_menu():
    pygame.init()
    global background
    global click
    global screen
    while True:
        screen.blit(background, (0, 0))
        draw_text(large_font,'Brick Smash',WHITE, 145, 40)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(200, 320, 200, 50)
        button_2 = pygame.Rect(200, 420, 200, 50)
        button_3 = pygame.Rect(200, 520, 200, 50)
        pygame.draw.rect(screen,LIGHTBLUE, button_1,4)
        pygame.draw.rect(screen,LIGHTBLUE, button_2,4)
        pygame.draw.rect(screen, LIGHTBLUE,button_3,4)
        draw_text(small_font,"Play Game",WHITE,250,335)
        draw_text(small_font,"Instructions",WHITE,240,435)
        draw_text(small_font,"Exit",WHITE,280,535)

        
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                instructions()
        if button_3.collidepoint((mx,my)):
            if click:
                exit()
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.flip()
        clock.tick(60)
 

if __name__ == "__main__":
    main_menu()