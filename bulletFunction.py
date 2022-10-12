import pygame

class bulletFunction():

    def __init__(self):
        self.name = "nothing"
        self.xAmp = 0
        self.yAmp = 0
        self.xDer = 0
        self.yDer = 0
        self.ticker = 0

    def setNameAndStuff(self, name, xamp, yamp, xder, yder):
        self.name = name
        self.xAmp = xamp
        self.yAmp = yamp
        self.xDer = xder
        self.yDer = yder



    def getName(self):
        return self.name

    def getXAmp(self):
        return self.xAmp

    def getYAmp(self):
        return self.yAmp

    def getXDer(self):
        return self.xDer

    def getYDer(self):
        return self.yDer

    def getTicker(self):
        return self.ticker

    def upTicker(self):
        self.ticker = self.ticker + 0.1