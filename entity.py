from math import cos, sin, pi, sqrt
from bulletFunction import bulletFunction
import pygame

sH = 720
sW = 1280


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
        self.bFunction.setNameAndStuff("boss", 0,0)
        self.radius = 735
        self.canHitPlayer = True

    def getCHP(self):
        return self.canHitPlayer

    def setCHP(self, chp):
        self.canHitPlayer = chp
        
        

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
        self.bFunction.setNameAndStuff(name, xamp, yamp)


    def update(self):
        if (self.bFunction.getName() == "nothing"):
            self.posX +=  self.speed*cos(self.dir)
            self.posY -=  self.speed*sin(self.dir)
        elif (self.bFunction.getName() == "sinusoid"):
            self.posX += self.speed*cos(self.dir)  +  (self.bFunction.getAmp()*cos(self.bFunction.getTicker()))*sin(self.dir)
            self.posY -= self.speed*sin(self.dir)  -  (self.bFunction.getAmp()*cos(self.bFunction.getTicker()))*cos(self.dir)
            self.bFunction.upTicker(self.bFunction.getFrequency())
        elif(self.bFunction.getName()=="boss"):
            self.posX +=  self.speed*cos(self.dir)
            self.posY -=  self.speed*sin(self.dir)


        if (self.posX) < (-120) or (self.posX) > (1400) or self.posY < (-450) or self.posY > (1120):
            self.isAlive = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.hue, pygame.Rect(self.posX, self.posY, self.size, self.size))

    def contact(self, pX, pY):
        if abs(self.posX - pX) < self.size and abs(self.posY - pY) < self.size:
            return True