from bullet import bullet
from random import randint
from boss import boss
from math import pi, sqrt, cos, sin, floor
import pygame

sH = 720
sW = 1280

class phases:
    def __init__(self):
        self.phaseName = "nothing"
        self.wallCounter = 0
        self.patienceCounter = 0
        self.fireWallSpacing = 70
        self.fireWallSpeed = 4
        self.minigunCounter = 0
        self.leucCounter = 0
        self.overallCounter = 0
        self.difficultyList = ["Easy", "Normal", "Hard", "Impossible", "Testing"]
        self.difficulty = "Easy"
        self.easyPhaseList = ["easyjoke", "feeble"]
        self.normalPhaseList = ["normaljoke", "slowminigun", "fastminigun", "thirdcounter"]
        self.hardPhaseList = ["hardjoke", "patience", "firewalls"]
        self.impossiblePhaseList = ["impossiblejoke", "leucsins"]
        self.testingPhaseList = ["rotatebeam"]
        self.bossi = boss()

    def reset(self):
        self.wallCounter = 0
        self.patienceCounter = 0
        self.fireWallSpacing = 70
        self.fireWallSpeed = 4
        self.minigunCounter = 0
        self.leucCounter = 0
        self.overallCounter = 0
        self.bossi = boss()

    def nextPhase(self):
        if(self.difficulty == "Easy"):
            if (self.phaseName == "nothing" or self.phaseName == self.easyPhaseList[len(self.easyPhaseList)-1]):
                self.phaseName = self.easyPhaseList[0]
            else:
                self.phaseName = self.easyPhaseList[self.easyPhaseList.index(self.phaseName)+1]
        elif(self.difficulty == "Normal"):
            if (self.phaseName == "nothing" or self.phaseName == self.normalPhaseList[len(self.normalPhaseList)-1]):
                self.phaseName = self.normalPhaseList[0]
            else:
                self.phaseName = self.normalPhaseList[self.normalPhaseList.index(self.phaseName)+1]
        elif(self.difficulty == "Hard"):
            if (self.phaseName == "nothing" or self.phaseName == self.hardPhaseList[len(self.hardPhaseList)-1]):
                self.phaseName = self.hardPhaseList[0]
            else:
                self.phaseName = self.hardPhaseList[self.hardPhaseList.index(self.phaseName)+1]
        elif(self.difficulty == "Impossible"):
            if (self.phaseName == "nothing" or self.phaseName == self.impossiblePhaseList[len(self.impossiblePhaseList)-1]):
                self.phaseName = self.impossiblePhaseList[0]
            else:
                self.phaseName = self.impossiblePhaseList[self.impossiblePhaseList.index(self.phaseName)+1]

        elif(self.difficulty == "Testing"):
            self.phaseName = self.testingPhaseList[0]

    def setBoss(self, boss):
        self.bossi = boss

    def setPhaseName(self, phaseName):
        self.phaseName = phaseName

    def getPhaseName(self):
        return self.phaseName

    def difficultyUp(self):
        if self.difficultyList.index(self.difficulty) != len(self.difficultyList) - 1:
            self.difficulty = self.difficultyList[self.difficultyList.index(self.difficulty)+1]
        else:
            self.difficulty = self.difficultyList[0]

    def difficultyDown(self):
        if self.difficultyList.index(self.difficulty) != 0:
            self.difficulty = self.difficultyList[self.difficultyList.index(self.difficulty)-1]
        else:
            self.difficulty = self.difficultyList[len(self.difficultyList)-1]

    def getDifficulty(self):
        return self.difficulty

    def runPhase(self, entityList):
        if (self.phaseName == "nothing"):
            self.nextPhase()
        elif(self.phaseName == "easyjoke"):
            self.runEasyJoke(entityList, self.bossi)
        elif(self.phaseName == "normaljoke"):
            self.runNormalJoke(entityList, self.bossi)
        elif(self.phaseName == "hardjoke"):
            self.runHardJoke(entityList, self.bossi)
        elif(self.phaseName == "impossiblejoke"):
            self.runImpossibleJoke(entityList, self.bossi)
        elif (self.phaseName == "patience"):
            self.runPatience(entityList, self.bossi)
        elif (self.phaseName == "firewalls"):
            self.runFirewall(entityList, self.bossi)
        elif (self.phaseName == "slowminigun"):
            self.runSlowMinigun(entityList, self.bossi)
        elif (self.phaseName == "fastminigun"):
            self.runFastMinigun(entityList, self.bossi)
        elif (self.phaseName == "thirdcounter"):
            self.runThirdCounter(entityList, self.bossi)
        elif (self.phaseName == "leucsins"):
            self.runLeucSins(entityList, self.bossi)
        elif (self.phaseName == "sinpain"):
            self.runSinPain(entityList, self.bossi)
        elif (self.phaseName == "feeble"):
            self.runFeeble(entityList, self.bossi)
        elif(self.phaseName == "rotatebeam"):
            self.runRotateBeam(entityList, self.bossi)

    def setNewTickSpeed(self, tSpeed): 
        pygame.time.set_timer(pygame.USEREVENT, tSpeed)

    def makeAStraightShooter(self, entityList, xStart, yStart, dir, speed, size):
        newBullet = bullet()
        newBullet.setPosDirSpdSize( xStart, yStart, dir, speed, size )
        entityList.append(newBullet)

    def makeASinusoid(self, entityList, xStart, yStart, dir, speed, size, amplitude, frequency):
        newBullet = bullet()
        newBullet.setPosDirSpdSize( xStart, yStart, dir, speed, size )
        newBullet.setBFunction("sinusoid", amplitude, frequency)
        entityList.append(newBullet)

    def runEasyJoke(self, entityList, bossi):

        self.setNewTickSpeed(200)

        array1 = [1,0,0,1,0,1,1,1,0,0,0,1,1,0,0,1,1,1,1]
        array2 = [1,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,1]
        array3 = [1,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,1]
        array4 = [0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,1,1,1,1]
        array5 = [0,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1]
        array6 = [0,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1]
        array7 = [0,1,1,0,0,0,1,1,1,0,1,0,0,1,0,1,1,1,1]

        allarrays = [array1,array2,array3,array4,array5,array6,array7]

        if self.overallCounter < len(array1):

            for i in range(7):
                if(allarrays[i][self.overallCounter]):
                    self.makeAStraightShooter(entityList, 0, 200 + 35*i, 0, 3.5, 25)

            self.overallCounter +=1
        else:
            self.overallCounter = 0
            self.nextPhase()


    def runNormalJoke(self, entityList, bossi):
        self.setNewTickSpeed(200)

        array1 = [0,0,0,1,0,0,1,1,0,0,1,0,0,1,0,0,1,1,1,0,0,1,1,0,0,1,0,0,1]
        array2 = [0,0,0,1,0,1,0,0,1,0,1,1,1,1,0,1,0,0,1,0,1,0,0,1,0,1,0,1,1]
        array3 = [0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,1,1]
        array4 = [0,0,0,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1]
        array5 = [0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,0,1,0,0,1,0,1,1,0,1]
        array6 = [0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1]
        array7 = [1,1,1,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,0,0,1,0,0,1]

        allarrays = [array1,array2,array3,array4,array5,array6,array7]

        if self.overallCounter < len(array1):

            for i in range(7):
                if(allarrays[i][self.overallCounter]):
                    self.makeAStraightShooter(entityList, 0, 200 + 35*i, 0, 3.5, 25)

            self.overallCounter +=1
        else:
            self.overallCounter = 0
            self.nextPhase()


    def runHardJoke(self, entityList, bossi):
        self.nextPhase()

    def runImpossibleJoke(self, entityList, bossi):
        self.nextPhase()

    def runFeeble(self, entityList, bossi):
        self.setNewTickSpeed(200)
        if self.overallCounter < 20:
            for i in range(3):
                self.makeAStraightShooter(entityList, 0, 30+200*i, 0, 5, 25)
            self.overallCounter += 1
        else:
            self.overallCounter = 0
            self.nextPhase()

    def runRotateBeam(self, entityList, bossi):
        self.setNewTickSpeed(100)
        angle = 2*pi*self.overallCounter/90
        radius = 735
        if self.overallCounter < 90:
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, 5, 1)
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, -5, 1)
            angle = angle + pi/2
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, 5, 1)
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, -5, 1)
            angle = angle + pi/2
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, 5, 1)
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, -5, 1)
            angle = angle + pi/2
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, 5, 1)
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, -5, 1)
            self.overallCounter +=1
        elif self.overallCounter < 180:
            angle = -2*pi*(self.overallCounter-90)/90
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, 5, 1)
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, -5, 1)
            angle = angle + pi/2
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, 5, 1)
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, -5, 1)
            angle = angle + pi/2
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, 5, 1)
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, -5, 1)
            angle = angle + pi/2
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, 5, 1)
            self.makeASinusoid(entityList, sW/2 + radius*cos(angle), sH/2 - radius*sin(angle), pi + angle, 25, 25, -5, 1)


            self.overallCounter +=1
        else:
            self.overallCounter = 0
            self.nextPhase()



    def runPatience(self, entityList, bossi):
        
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
            self.nextPhase()

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
            self.nextPhase()

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
            self.nextPhase()

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
            self.nextPhase()

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
            self.nextPhase()

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
            self.nextPhase()  

    def runSinPain(self, entityList, bossi):
        self.setNewTickSpeed(100)
        amp = 4
        freq = 0.075
        spd = 10
        if self.overallCounter < 50:
            #self.makeASinusoid(entityList, 0, pi/3, 0, spd, 25, amp, freq )
            #self.makeASinusoid(entityList, 0, 2*pi/3, 0, spd, 25, -amp, freq )
            #self.makeASinusoid(entityList, 0, pi/6, 0, spd * 1.5, 25, amp/2, freq )
            #self.makeASinusoid(entityList, 0, 5*pi/6, 0, spd * 1.5, 25, -amp/2, freq )

            self.makeASinusoid(entityList, 0, 25*self.overallCounter, 0, spd, 25, amp, freq )
            self.makeASinusoid(entityList, 0, 25*self.overallCounter, 0, spd, 25, -amp, freq )
            self.makeASinusoid(entityList, 0, 25*self.overallCounter, 0, spd * 1.5, 25, amp/2, freq )
            self.makeASinusoid(entityList, 0, 25*self.overallCounter, 0, spd * 1.5, 25, -amp/2, freq )
            self.overallCounter+=1
        else:
            self.overallCounter = 0
            self.nextPhase()
    