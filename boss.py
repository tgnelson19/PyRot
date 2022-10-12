from entity import entity
from math import atan
import pygame

class boss(entity):

    def __init__(self):
        self.posX = 250
        self.posY = 250
        self.hue = pygame.Color(0,255,0)
        self.dir = 0
        self.name = "boss"
        self.speed = 2
        self.size = 25
        self.isAlive = True
        self.trueSpeed = 2

    def goToCenter(self):
        if (self.posX - 480) > self.trueSpeed and (self.posY - 270) > self.trueSpeed:
            self.speed = 2
            self.dir = atan((self.posY - 270)/(self.posX - 480))
            if ((self.posY - 270)*(self.posX - 480)) <= 0:
                self.dir = -atan((self.posY - 270)/(self.posX - 480))
        else:
            self.posX = 480
            self.poxY = 270
            self.dir = 0
            self.speed = 0

    def goToPos(self, x, y):
        if abs(self.posX - x) > self.trueSpeed or abs(self.posY - y + 25) > self.trueSpeed and not self.posX - x == 0:
            self.speed = 2
            self.dir = atan((self.posY - y + 25)/(self.posX - x))
            if (self.posY - y)*(self.posX - x) < 0:
                self.dir = atan((self.posY - y + 25)/(self.posX - x))
        else:
            self.posX = x
            self.poxY = y + 25
            self.dir = 0
            self.speed = 0