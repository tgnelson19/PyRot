from entity import entity
from bulletFunction import bulletFunction
import pygame
from math import sqrt

sH = 720
sW = 1280

class bullet(entity):

    def __init__(self):
        self.isAlive = True
        self.posX = 0
        self.posY = 0
        self.dir = 0
        self.name = "bullet"
        self.hue= pygame.Color(255,0,0)
        self.speed = 0
        self.size = 25
        self.bFunction = bulletFunction()
        self.radius = sqrt(sW^2 + sH^2)
        self.canHitPlayer = True

    