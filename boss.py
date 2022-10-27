from entity import entity
from bulletFunction import bulletFunction
from math import atan
import pygame

sH = 720
sW = 1280

class boss(entity):

    def __init__(self):
        self.posX = 200
        self.posY = 200
        self.hue = pygame.Color(0,255,0)
        self.dir = 0
        self.name = "boss"
        self.speed = 10
        self.size = 25
        self.isAlive = True
        self.trueSpeed = 5
        self.bFunction = bulletFunction()

    def goToCenter(self):
        self.speed = 1
        self.dir = -atan((self.posY - sH/2)/(self.posX - sW/2))
        if ((self.posY - sH/2)*(self.posX - sW/2)) <= 0:
            self.dir = atan((self.posY - sH/2)/(self.posX - sW/2))

    def isAtPos(self, x, y):
        if abs(self.posX - x) > 10 or abs(self.posY - y) > 10 and not self.posX == x:
            return False
        else:
            return True

    def goToPos(self, x, y):
        if self.isAtPos(x, y):
            self.posX = x
            self.poxY = y
            self.dir = 0
            self.speed = -2
        else:
            self.speed = 10
            if (self.posY - y)*(self.posX - x) < 0:
                self.dir = atan((self.posY - y + 25)/(self.posX - x))
            else:
                self.dir = atan((self.posY - y + 25)/(self.posX - x))