from entity import entity
from bulletFunction import bulletFunction
from math import atan
import pygame

sH = 720
sW = 1280

class boss(entity):

    def __init__(self):
        self.posX = 250
        self.posY = 250
        self.hue = pygame.Color(0,255,0)
        self.dir = 0
        self.name = "boss"
        self.speed = 1
        self.size = 25
        self.isAlive = True
        self.trueSpeed = 2
        self.bFunction = bulletFunction()

    def goToCenter(self):
        self.speed = 1
        self.dir = -atan((self.posY - sH/2)/(self.posX - sW/2))
        if ((self.posY - sH/2)*(self.posX - sW/2)) <= 0:
            self.dir = atan((self.posY - sH/2)/(self.posX - sW/2))

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