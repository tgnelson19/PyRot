from bullet import bullet
from random import randint
from math import pi

class phases:
    def __init__(self):
        self.phaseName = "nothing"
        self.wallCounter = 0
        self.patienceCounter = 0
        self.fireWallSpacing = 70
        self.fireWallSpeed = 4

    def reset(self):
        self.phaseName = "nothing"
        self.wallCounter = 0
        self.patienceCounter = 0
        self.fireWallSpacing = 70
        self.fireWallSpeed = 4

    def setPhaseName(self, phaseName):
        self.phaseName = phaseName

    def getPhaseName(self):
        return self.phaseName

    def runPatience(self, entityList):
        if self.patienceCounter < 10:
            newBullet = bullet()
            newBullet.setPosDirSpdSize( randint(20, 940), 0, 3*pi/2, randint(2,10)/2, randint(10, 40) )
            entityList.append(newBullet)
            newBullet2 = bullet()
            newBullet2.setPosDirSpdSize( randint(20, 940), 540, pi/2, randint(2,10)/2, randint(10, 40) )
            entityList.append(newBullet2)
            newBullet3 = bullet()
            newBullet3.setPosDirSpdSize( 0, randint(20, 520), 0, randint(2,10)/2, randint(10, 40) )
            entityList.append(newBullet3)
            newBullet4 = bullet()
            newBullet4.setPosDirSpdSize( 940, randint(20, 520), pi, randint(2,10)/2, randint(10, 40) )
            entityList.append(newBullet4)
            self.patienceCounter +=1
        elif self.patienceCounter < 30:
            self.patienceCounter +=1
        else:
            self.patienceCounter = 0
            self.phaseName = "firewalls"

    def runFirewall(self, entityList):
        if self.wallCounter < 7:
            for i in range(12):
                newBullet = bullet()
                newBullet.setPosDirSpdSize(0, 10 + i*self.fireWallSpacing, 0, self.fireWallSpeed, 25)
                entityList.append(newBullet)
                newBullet1 = bullet()
                newBullet1.setPosDirSpdSize(960, 35 + i*self.fireWallSpacing, pi, self.fireWallSpeed, 25)
                entityList.append(newBullet1)

            self.wallCounter += 1
        elif self.wallCounter < 16:
            self.wallCounter +=1
        elif self.wallCounter < 23:
            for i in range(20):
                newBullet = bullet()
                newBullet.setPosDirSpdSize(10 + i*self.fireWallSpacing, 0, 3*pi/2, self.fireWallSpeed, 25)
                entityList.append(newBullet)
                newBullet1 = bullet()
                newBullet1.setPosDirSpdSize(35 + i*self.fireWallSpacing, 540, pi/2, self.fireWallSpeed, 25)
                entityList.append(newBullet1)
            self.wallCounter +=1
        elif self.wallCounter < 31:
            self.wallCounter +=1
        else:
            self.wallCounter = 0
            self.phaseName = "patience"
            