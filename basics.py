import pygame as pg 
pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption("Test game")


class player(object):
    def __init__(self,x,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height






pg.quit()