from entity import entity
from math import atan
import pygame

class boss(entity):

    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.hue = pygame.Color(0,255,0)
        self.dir = 0
        self.name = "boss"
        self.speed = 2

    def isAtCenter(self):
        if self.posX - 480 > self.speed and self.posY - 270 > self.speed:
            self.dir = atan((self.posY - 270)/(self.posX - 480))
            if (self.posY - 270)*(self.posX - 480) < 0:
                self.dir = -atan((self.posY - 270)/(self.posX - 480))
        else:
            self.posX = 480
            self.poxY = 270
            return True