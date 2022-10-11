from entity import entity
import pygame

class bullet(entity):

    def __init__(self):
        self.isAlive = True
        self.posX = 0
        self.posY = 0
        self.dir = "none"
        self.name = "bullet"
        self.hue= pygame.Color(255,0,0)
        self.speed = 0
        self.size = 25

    