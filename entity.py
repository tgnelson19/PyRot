from math import cos, sin, pi
from bulletFunction import bulletFunction
import pygame


class entity:
    def __init__(self):
        self.isAlive = True
        self.posX = 0
        self.posY = 0
        self.speed = 0
        self.dir = 0
        self.size = 25
        self.hue = pygame.Color(255,255,255)
        self.name = "none"
        self.bFunction = bulletFunction()
        
        

    def setPos(self, x, y):
        self.posX = x
        self.posY = y

    def getPos(self):
        return self.pos

    def setDir(self, direc):
        self.dir = direc

    def getDir(self):
        return self.dir

    def setPosDirSpdSize(self, x, y, direc, speed, size):
        self.posX = x
        self.posY = y
        self.dir = direc
        self.speed = speed
        self.size = size

    def setBFunction(self, name, xamp, yamp):
        self.bFunction.setNameAndStuff(name, xamp, yamp, 0, 0)


    def update(self):
        if (self.bFunction.getName() == "nothing"):
            self.posX +=  self.speed*cos(self.dir)
            self.posY -=  self.speed*sin(self.dir)
        else:
            self.posX += self.speed*cos(self.dir)
            self.posY -= self.bFunction.getYAmp()*sin(self.bFunction.getTicker())
            self.bFunction.upTicker()


        if (self.posX) < (0 - self.size) or (self.posX) > (960 + self.size) or (self.posY) < (0 - self.size) or (self.posY) > (540 + self.size):
            self.isAlive = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.hue, pygame.Rect(self.posX, self.posY, self.size, self.size))

    def contact(self, pX, pY):
        if abs(self.posX - pX) < self.size*4/5 and abs(self.posY - pY) < self.size*4/5:
            return True