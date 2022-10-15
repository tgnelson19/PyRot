from tkinter import E
from bullet import bullet
from random import randint
from boss import boss
from math import pi
from math import floor
import pygame

sH = 720
sW = 1280

class phases:
    def __init__(self):
        self.phaseName = "patience"
        self.wallCounter = 0
        self.patienceCounter = 0
        self.fireWallSpacing = 70
        self.fireWallSpeed = 4
        self.minigunCounter = 0
        self.leucCounter = 0
        self.overallCounter = 0
        self.phaseList = ["patience", "firewalls", "slowminigun", "fastminigun", "thirdcounter", "leucsins"]

    def reset(self):
        self.wallCounter = 0
        self.patienceCounter = 0
        self.fireWallSpacing = 70
        self.fireWallSpeed = 4
        self.minigunCounter = 0
        self.leucCounter = 0
        self.overallCounter = 0
        self.phaseList = ["patience", "firewalls", "slowminigun", "fastminigun", "thirdcounter", "leucsins"]

    def setPhaseName(self, phaseName):
        self.phaseName = phaseName

    def getPhaseName(self):
        return self.phaseName

    def phaseUp(self):
        if self.phaseList.index(self.phaseName) != len(self.phaseList) - 1:
            self.phaseName = self.phaseList[self.phaseList.index(self.phaseName)+1]
        else:
            self.phaseName = self.phaseList[0]

    def phaseDown(self):
        if self.phaseList.index(self.phaseName) != 0:
            self.phaseName = self.phaseList[self.phaseList.index(self.phaseName)-1]
        else:
            self.phaseName = self.phaseList[len(self.phaseList)-1]

    def runPatience(self, entityList, bossi):
        bossi.goToCenter()
        pygame.time.set_timer(pygame.USEREVENT, 200)
        if self.patienceCounter < 40 and self.patienceCounter % 2 == 0:
            newBullet = bullet()
            newBullet.setPosDirSpdSize( randint(20, sW - 20), 0, 3*pi/2, randint(4,6)/2, 25 )
            entityList.append(newBullet)
            newBullet2 = bullet()
            newBullet2.setPosDirSpdSize( randint(20, sW - 20), sH, pi/2, randint(4,6)/2, 25 )
            entityList.append(newBullet2)
            newBullet3 = bullet()
            newBullet3.setPosDirSpdSize( 0, randint(20, sH - 20), 0, randint(4,6)/2, 25 )
            entityList.append(newBullet3)
            newBullet4 = bullet()
            newBullet4.setPosDirSpdSize( sW - 20, randint(20, sH - 20), pi, randint(4,6)/2, 25 )
            entityList.append(newBullet4)
            self.patienceCounter +=1
        elif self.patienceCounter < 55:
            self.patienceCounter +=1
        if self.patienceCounter < 95 and self.patienceCounter % 2 == 0:
            newBullet = bullet()
            newBullet.setPosDirSpdSize( randint(20, sW - 20), 0, 3*pi/2, randint(4,6)/2, 25 )
            entityList.append(newBullet)
            newBullet2 = bullet()
            newBullet2.setPosDirSpdSize( randint(20, sW - 20), sH, pi/2, randint(4,6)/2, 25 )
            entityList.append(newBullet2)
            newBullet3 = bullet()
            newBullet3.setPosDirSpdSize( 0, randint(20, sH - 20), 0, randint(4,6)/2, 25 )
            entityList.append(newBullet3)
            newBullet4 = bullet()
            newBullet4.setPosDirSpdSize( sW - 20, randint(20, sH - 20), pi, randint(4,6)/2, 25 )
            entityList.append(newBullet4)
            self.patienceCounter +=1
        elif self.patienceCounter < 110:
            self.patienceCounter +=1
        else:
            self.patienceCounter = 0
            self.phaseName = "firewalls"

    def runFirewall(self, entityList, bossi):
        bossi.goToCenter()
        pygame.time.set_timer(pygame.USEREVENT, 200)
        if self.wallCounter < 7:
            for i in range(24):
                newBullet = bullet()
                newBullet.setPosDirSpdSize(0, 10 + i*self.fireWallSpacing, 0, self.fireWallSpeed, 25)
                entityList.append(newBullet)
                newBullet1 = bullet()
                newBullet1.setPosDirSpdSize(sW, 45 + i*self.fireWallSpacing, pi, self.fireWallSpeed, 25)
                entityList.append(newBullet1)
            self.wallCounter += 1
        elif self.wallCounter < 11:
            self.wallCounter +=1
        elif self.wallCounter < 18:
            for i in range(24):
                newBullet = bullet()
                newBullet.setPosDirSpdSize(0, 10 + i*self.fireWallSpacing, 0, self.fireWallSpeed, 25)
                entityList.append(newBullet)
                newBullet1 = bullet()
                newBullet1.setPosDirSpdSize(sW, 45 + i*self.fireWallSpacing, pi, self.fireWallSpeed, 25)
                entityList.append(newBullet1)
            self.wallCounter +=1
        elif self.wallCounter < 30:
            self.wallCounter +=1
        elif self.wallCounter < 37:
            for i in range(24):
                newBullet = bullet()
                newBullet.setPosDirSpdSize(10 + i*self.fireWallSpacing, 0, 3*pi/2, self.fireWallSpeed, 25)
                entityList.append(newBullet)
                newBullet1 = bullet()
                newBullet1.setPosDirSpdSize(45 + i*self.fireWallSpacing, sH, pi/2, self.fireWallSpeed, 25)
                entityList.append(newBullet1)
            self.wallCounter +=1
        elif self.wallCounter < 41:
            self.wallCounter +=1
        elif self.wallCounter < 48:
            for i in range(24):
                newBullet = bullet()
                newBullet.setPosDirSpdSize(10 + i*self.fireWallSpacing, 0, 3*pi/2, self.fireWallSpeed, 25)
                entityList.append(newBullet)
                newBullet1 = bullet()
                newBullet1.setPosDirSpdSize(45 + i*self.fireWallSpacing, sH, pi/2, self.fireWallSpeed, 25)
                entityList.append(newBullet1)
            self.wallCounter +=1
        elif self.wallCounter < 50:
            self.wallCounter +=1
        else:
            self.wallCounter = 0
            self.phaseName = "slowminigun"


    def runSlowMinigun(self, entityList, bossi):
        
        pygame.time.set_timer(pygame.USEREVENT, 30)

        if self.minigunCounter < 100 :
            bossi.goToPos(sW/2,0)
            newBullet = bullet()
            newBullet.setPosDirSpdSize( sW/2, 0, pi + pi/100 + (pi/100)*self.minigunCounter, randint(4,8)/2, 25 )
            entityList.append(newBullet)
            self.minigunCounter +=1

        elif self.minigunCounter < 130:
            self.minigunCounter +=1

        elif self.minigunCounter < 230 :
            bossi.goToPos(sW/2,sH)
            newBullet = bullet()
            newBullet.setPosDirSpdSize( sW/2, sH, (pi/100) + ((pi/100)*self.minigunCounter - 130), randint(4,8)/2, 25 )
            entityList.append(newBullet)
            self.minigunCounter +=1
        elif self.minigunCounter < 270:
            self.minigunCounter +=1
        else:
            self.minigunCounter = 0
            self.phaseName = "fastminigun"

    def runFastMinigun(self, entityList, bossi):

        pygame.time.set_timer(pygame.USEREVENT, 50)

        if self.minigunCounter < 20 :
            bossi.goToPos(sW/2,0)
            newBullet = bullet()
            newBullet.setPosDirSpdSize( sW/2, 0, pi + pi/20 + (pi/20)*self.minigunCounter, randint(4,8)/2, 25 )
            entityList.append(newBullet)
            self.minigunCounter +=1

        elif self.minigunCounter < 40:
            newBullet = bullet()
            newBullet.setPosDirSpdSize( sW/2, 0, - pi/20 - (pi/20)*(self.minigunCounter -20), randint(4,8)/2, 25 )
            entityList.append(newBullet)
            self.minigunCounter +=1

        elif self.minigunCounter < 60 :
            newBullet = bullet()
            newBullet.setPosDirSpdSize( sW/2, 0, pi + pi/20 + (pi/20)*(self.minigunCounter-40), randint(4,8)/2, 25 )
            entityList.append(newBullet)
            self.minigunCounter +=1

        elif self.minigunCounter < 80:
            newBullet = bullet()
            newBullet.setPosDirSpdSize( sW/2, 0, - pi/20 - (pi/20)*(self.minigunCounter -60), randint(4,8)/2, 25 )
            entityList.append(newBullet)
            self.minigunCounter +=1

        elif self.minigunCounter < 120:
            self.minigunCounter +=1
        else:
            self.minigunCounter = 0
            self.phaseName = "thirdcounter"

    def runThirdCounter(self, entityList, bossi):
        bossi.goToCenter()
        pygame.time.set_timer(pygame.USEREVENT, 800)
        if self.leucCounter < 10 :
            safespot = randint(floor(sW/94),floor(sW/53))
            for i in range(55):

                if not(i == safespot - 1 or i == safespot or i == safespot + 1):
                    newBullet = bullet()
                    newBullet.setPosDirSpdSize( 10 + 35*i, 0, 3*pi/2, 2.3, 25 )
                    entityList.append(newBullet)

            self.leucCounter +=1
        elif self.leucCounter < 12:
            self.leucCounter += 1
        else:
            self.leucCounter = 0
            self.phaseName = "leucsins"

    def runTesting(self, entityList, bossi):
        pygame.time.set_timer(pygame.USEREVENT, 300)
        if self.overallCounter < 20:
            newBullet = bullet()
            newBullet.setPosDirSpdSize( 0, 40 + self.overallCounter* 20, 0, 3, 25 )
            newBullet.setBFunction("sinusoid", 0,5)
            entityList.append(newBullet)
            newBullet1 = bullet()
            newBullet1.setPosDirSpdSize( 0, 40 + self.overallCounter* 20, 0, 3, 25 )
            newBullet1.setBFunction("sinusoid", 0, -5)
            entityList.append(newBullet1)
            self.overallCounter += 1
        elif self.overallCounter < 40:
            newBullet = bullet()
            newBullet.setPosDirSpdSize( 0, 440 - (self.overallCounter - 20)* 20, 0, 3, 25 )
            newBullet.setBFunction("sinusoid", 0,5)
            entityList.append(newBullet)
            newBullet1 = bullet()
            newBullet1.setPosDirSpdSize( 0, 440 - (self.overallCounter - 20)* 20, 0, 3, 25 )
            newBullet1.setBFunction("sinusoid", -5, -5)
            entityList.append(newBullet1)
            self.overallCounter += 1
            if self.overallCounter == 39:
                self.overallCounter = 0
            
    def makeAStraightShooter(self, entityList, xStart, yStart, dir, speed, size):
        newBullet = bullet()
        newBullet.setPosDirSpdSize( xStart, yStart, dir, speed, size )
        entityList.append(newBullet)

    def setNewTickSpeed(self, tSpeed): 
        pygame.time.set_timer(pygame.USEREVENT, tSpeed)

    def makeASinusoid(self, entityList, xStart, yStart, dir, speed, size, amplitude, frequency):
        newBullet = bullet()
        newBullet.setPosDirSpdSize( xStart, yStart, dir, speed, size )
        newBullet.setBFunction("sinusoid", amplitude, frequency)
        entityList.append(newBullet)

    def runTesting1(self, entityList, bossi):
        self.setNewTickSpeed(400)
        if self.overallCounter < 20:
            self.makeAStraightShooter(entityList, 0, 280, 0, 3, 25)
            self.overallCounter += 1
        else:
            self.overallCounter = 0

    def runTesting2(self, entityList, bossi):
        self.setNewTickSpeed(200)
        if self.overallCounter < 20:
            self.makeASinusoid(entityList, sW/2, 0, -pi/20 - (self.overallCounter*pi)/20, 3, 25, 4, 0.1)
            self.overallCounter+=1
        elif self.overallCounter < 40:
            self.makeASinusoid(entityList, sW/2, 0, pi + pi/20  + ((self.overallCounter-20)*pi)/20, 3, 25, 4, 0.1)
            self.overallCounter +=1
        else:
            self.overallCounter = 0

    def runLeucSins(self, entityList, bossi):
        self.setNewTickSpeed(300)
        amp = 6
        freq = 0.075
        spd = 6
        if self.overallCounter < 20:
            self.makeASinusoid(entityList, sW/2, 0, -pi/20 - (self.overallCounter*pi)/20, spd, 25, amp, freq )
            self.makeASinusoid(entityList, sW/2, 0, -pi/20 - (self.overallCounter*pi)/20, spd, 25, -amp, freq )
            #self.makeASinusoid(entityList, sW/2, 0, -pi/20 - (self.overallCounter*pi)/20, spd * 1.5, 25, amp/2, freq )
            #self.makeASinusoid(entityList, sW/2, 0, -pi/20 - (self.overallCounter*pi)/20, spd * 1.5, 25, -amp/2, freq )
            self.overallCounter+=1
        elif self.overallCounter < 40:
            self.makeASinusoid(entityList, sW/2, 0, pi + pi/20  + ((self.overallCounter-20)*pi)/20, spd, 25, amp, freq )
            self.makeASinusoid(entityList, sW/2, 0, pi + pi/20  + ((self.overallCounter-20)*pi)/20, spd, 25, -amp, freq )
            #self.makeASinusoid(entityList, sW/2, 0, pi + pi/20  + ((self.overallCounter-20)*pi)/20, spd * 1.5, 25, amp/2, freq )
            #self.makeASinusoid(entityList, sW/2, 0, pi + pi/20  + ((self.overallCounter-20)*pi)/20, spd * 1.5, 25, -amp/2, freq )
            self.overallCounter +=1
        else:
            self.overallCounter = 0
            self.phaseName = "patience"
        
    