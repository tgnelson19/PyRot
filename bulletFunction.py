import pygame

class bulletFunction():

    def __init__(self):
        self.name = "nothing"
        self.amplitude = 0
        self.frequency = 1
        self.ticker = 0

    def setNameAndStuff(self, name, amp, freq):
        self.name = name
        self.amplitude = amp
        self.frequency = freq

    def getName(self):
        return self.name

    def getAmp(self):
        return self.amplitude

    def getFrequency(self):
        return self.frequency

    def getTicker(self):
        return self.ticker

    def upTicker(self, frequency):
        self.ticker = self.ticker + frequency