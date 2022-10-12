from bullet import bullet
from random import randint
from math import pi
import pygame

class phases:
    def __init__(self):
        self.phaseName = "nothing"
        self.wallCounter = 0
        self.patienceCounter = 0
        self.fireWallSpacing = 70
        self.fireWallSpeed = 4
        self.minigunCounter = 0
        self.leucCounter = 0

    def reset(self):
        self.phaseName = "nothing"
        self.wallCounter = 0
        self.patienceCounter = 0
        self.fireWallSpacing = 70
        self.fireWallSpeed = 4
        self.minigunCounter = 0
        self.leucCounter = 0

    def setPhaseName(self, phaseName):
        self.phaseName = phaseName

    def getPhaseName(self):
        return self.phaseName

    def runPatience(self, entityList):
        pygame.time.set_timer(pygame.USEREVENT, 200)
        if self.patienceCounter < 10 and self.patienceCounter % 2 == 0:
            newBullet = bullet()
            newBullet.setPosDirSpdSize( randint(20, 940), 0, 3*pi/2, randint(4,6)/2, 25 )
            entityList.append(newBullet)
            newBullet2 = bullet()
            newBullet2.setPosDirSpdSize( randint(20, 940), 540, pi/2, randint(4,6)/2, 25 )
            entityList.append(newBullet2)
            newBullet3 = bullet()
            newBullet3.setPosDirSpdSize( 0, randint(20, 520), 0, randint(4,6)/2, 25 )
            entityList.append(newBullet3)
            newBullet4 = bullet()
            newBullet4.setPosDirSpdSize( 940, randint(20, 520), pi, randint(4,6)/2, 25 )
            entityList.append(newBullet4)
            self.patienceCounter +=1
        elif self.patienceCounter < 25:
            self.patienceCounter +=1
        if self.patienceCounter < 35 and self.patienceCounter % 2 == 0:
            newBullet = bullet()
            newBullet.setPosDirSpdSize( randint(20, 940), 0, 3*pi/2, randint(4,6)/2, 25 )
            entityList.append(newBullet)
            newBullet2 = bullet()
            newBullet2.setPosDirSpdSize( randint(20, 940), 540, pi/2, randint(4,6)/2, 25 )
            entityList.append(newBullet2)
            newBullet3 = bullet()
            newBullet3.setPosDirSpdSize( 0, randint(20, 520), 0, randint(4,6)/2, 25 )
            entityList.append(newBullet3)
            newBullet4 = bullet()
            newBullet4.setPosDirSpdSize( 940, randint(20, 520), pi, randint(4,6)/2, 25 )
            entityList.append(newBullet4)
            self.patienceCounter +=1
        elif self.patienceCounter < 50:
            self.patienceCounter +=1
        else:
            self.patienceCounter = 0
            self.phaseName = "firewalls"

    def runFirewall(self, entityList):
        pygame.time.set_timer(pygame.USEREVENT, 200)
        if self.wallCounter < 7:
            for i in range(12):
                newBullet = bullet()
                newBullet.setPosDirSpdSize(0, 10 + i*self.fireWallSpacing, 0, self.fireWallSpeed, 25)
                entityList.append(newBullet)
                newBullet1 = bullet()
                newBullet1.setPosDirSpdSize(960, 45 + i*self.fireWallSpacing, pi, self.fireWallSpeed, 25)
                entityList.append(newBullet1)
            self.wallCounter += 1
        elif self.wallCounter < 11:
            self.wallCounter +=1
        elif self.wallCounter < 18:
            for i in range(20):
                newBullet = bullet()
                newBullet.setPosDirSpdSize(0, 10 + i*self.fireWallSpacing, 0, self.fireWallSpeed, 25)
                entityList.append(newBullet)
                newBullet1 = bullet()
                newBullet1.setPosDirSpdSize(960, 45 + i*self.fireWallSpacing, pi, self.fireWallSpeed, 25)
                entityList.append(newBullet1)
            self.wallCounter +=1
        elif self.wallCounter < 30:
            self.wallCounter +=1
        elif self.wallCounter < 37:
            for i in range(20):
                newBullet = bullet()
                newBullet.setPosDirSpdSize(10 + i*self.fireWallSpacing, 0, 3*pi/2, self.fireWallSpeed, 25)
                entityList.append(newBullet)
                newBullet1 = bullet()
                newBullet1.setPosDirSpdSize(45 + i*self.fireWallSpacing, 540, pi/2, self.fireWallSpeed, 25)
                entityList.append(newBullet1)
            self.wallCounter +=1
        elif self.wallCounter < 41:
            self.wallCounter +=1
        elif self.wallCounter < 48:
            for i in range(20):
                newBullet = bullet()
                newBullet.setPosDirSpdSize(10 + i*self.fireWallSpacing, 0, 3*pi/2, self.fireWallSpeed, 25)
                entityList.append(newBullet)
                newBullet1 = bullet()
                newBullet1.setPosDirSpdSize(45 + i*self.fireWallSpacing, 540, pi/2, self.fireWallSpeed, 25)
                entityList.append(newBullet1)
            self.wallCounter +=1
        elif self.wallCounter < 50:
            self.wallCounter +=1
        else:
            self.wallCounter = 0
            self.phaseName = "slowminigun"


    def runSlowMinigun(self, entityList):

        pygame.time.set_timer(pygame.USEREVENT, 30)

        if self.minigunCounter < 100 :
            newBullet = bullet()
            newBullet.setPosDirSpdSize( 480, 0, pi + pi/100 + (pi/100)*self.minigunCounter, randint(4,8)/2, 25 )
            entityList.append(newBullet)
            self.minigunCounter +=1

        elif self.minigunCounter < 130:
            self.minigunCounter +=1

        elif self.minigunCounter < 230 :
            newBullet = bullet()
            newBullet.setPosDirSpdSize( 480, 540, (pi/100) + ((pi/100)*self.minigunCounter - 130), randint(4,8)/2, 25 )
            entityList.append(newBullet)
            self.minigunCounter +=1
        elif self.minigunCounter < 270:
            self.minigunCounter +=1
        else:
            self.minigunCounter = 0
            self.phaseName = "fastminigun"

    def runFastMinigun(self, entityList):

        pygame.time.set_timer(pygame.USEREVENT, 50)

        if self.minigunCounter < 20 :
            newBullet = bullet()
            newBullet.setPosDirSpdSize( 480, 0, pi + pi/20 + (pi/20)*self.minigunCounter, randint(4,8)/2, 25 )
            entityList.append(newBullet)
            self.minigunCounter +=1

        elif self.minigunCounter < 40:
            newBullet = bullet()
            newBullet.setPosDirSpdSize( 480, 0, - pi/20 - (pi/20)*(self.minigunCounter -20), randint(4,8)/2, 25 )
            entityList.append(newBullet)
            self.minigunCounter +=1

        elif self.minigunCounter < 60 :
            newBullet = bullet()
            newBullet.setPosDirSpdSize( 480, 0, pi + pi/20 + (pi/20)*(self.minigunCounter-40), randint(4,8)/2, 25 )
            entityList.append(newBullet)
            self.minigunCounter +=1

        elif self.minigunCounter < 80:
            newBullet = bullet()
            newBullet.setPosDirSpdSize( 480, 0, - pi/20 - (pi/20)*(self.minigunCounter -60), randint(4,8)/2, 25 )
            entityList.append(newBullet)
            self.minigunCounter +=1

        elif self.minigunCounter < 120:
            self.minigunCounter +=1
        else:
            self.minigunCounter = 0
            self.phaseName = "thirdcounter"

    def runThirdCounter(self, entityList):
        pygame.time.set_timer(pygame.USEREVENT, 800)
        if self.leucCounter < 10 :
            safespot = randint(8,20)
            for i in range(28):

                if not(i == safespot - 1 or i == safespot or i == safespot + 1):
                    newBullet = bullet()
                    newBullet.setPosDirSpdSize( 10 + 35*i, 0, 3*pi/2, 2.3, 25 )
                    entityList.append(newBullet)

            self.leucCounter +=1
        elif self.leucCounter < 12:
            self.leucCounter += 1
        else:
            self.leucCounter = 0
            self.phaseName = "patience"