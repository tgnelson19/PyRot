import pygame

sH = 720
sW = 1280

class textThing():
    
    def __init__(self, text, posX, posY, color):
        self.text = text
        self.font = pygame.font.Font('freeFont.otf', 32)
        self.posX = posX
        self.posY = posY
        self.color = color
        self.letters = self.font.render(text, True, color)
        self.rect = self.letters.get_rect()
        self.rect.topleft = (posX, posY)


    def getText(self):
        return self.text

    def setText(self, text):
        self.text = text

    def drawText(self, screen):
        screen.blit(self.letters, self.rect)

    def updateText(self, text):
        self.letters = self.font.render(text, True, self.color)
        self.rect = self.letters.get_rect()
        self.rect.topleft = (self.posX, self.posY)