from math import pi
from random import randint
import pygame

from bullet import bullet
from entity import entity
from boss import boss
from bomb import bomb
from phases import phases
from textThing import textThing

sH = 720
sW = 1280

def main():
    pygame.init()
 
    size = [sW, sH]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("PyRot")

    done = False

    openingTextList = []
    score = textThing("0", sW - 60, 20, pygame.Color(255,255,255))
    start = textThing("MicroDodging", 100, sH/3, pygame.Color(0,0,0))
    openingTextList.append(start)
    instructions = textThing("Press Space Key To Play", 100, sH/3 + 50, pygame.Color(0,0,0))
    openingTextList.append(instructions)
    instructions2 = textThing("Use Arrow Keys To Change First Phase", 100, sH/3 + 100, pygame.Color(0,0,0))
    openingTextList.append(instructions2)
    instructions3 = textThing("Press Escape To Close", 100, sH/3 + 150, pygame.Color(0,0,0))
    openingTextList.append(instructions3)
    instructions4 = textThing("Nothing", 900, sH/3, pygame.Color(0,0,0))
    openingTextList.append(instructions4)
    instructions5 = textThing("Last score was 0", 400, sH-100, pygame.Color(0,0,0))
    openingTextList.append(instructions5)

    clock = pygame.time.Clock()

    pygame.time.set_timer(pygame.USEREVENT, 200)

    trueSpeed = 5
    directionalSpeed = 5

    coinDead = True
    playerDead = True

    phase = phases()

    phase.setPhaseName("leucsins")

    while not done:

        if playerDead:

            phase.reset()

            entityList = []

            scoreInt = 0

            isUp = False
            isDown = False
            isLeft = False
            isRight = False

            bossi = boss()
            #entityList.append(bossi)

            phase.setBoss(bossi)

            pX = sW/2
            pY = sH/2
            pSize = 25

            coinX = randint(200, sW-200)
            coinY = randint(100, sH-100)

            score.updateText("0")
            instructions4.updateText(phase.getPhaseName())

            for i in openingTextList:
                i.drawText(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: done = True
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE:done = True
                    elif event.key == pygame.K_UP: phase.phaseUp()
                    elif event.key == pygame.K_DOWN: phase.phaseDown()
                    elif event.key == pygame.K_SPACE: playerDead = False

            clock.tick(60)
            pygame.display.flip()
            screen.fill(pygame.Color(255,255,255))

        else:

            for event in pygame.event.get():

                if event.type == pygame.USEREVENT:
                    phase.runPhase(entityList)

                if event.type == pygame.QUIT: done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP: isUp = True
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN: isDown = True
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT: isLeft = True
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT: isRight = True
                    if event.key == pygame.K_ESCAPE:
                        done = True
                    else:
                        playerDead = False

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_UP: isUp = False
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN: isDown = False
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT: isLeft = False
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT: isRight = False

            if isUp & isLeft | isUp & isRight | isDown & isLeft | isDown & isRight: directionalSpeed = trueSpeed * 0.707
            else: directionalSpeed = trueSpeed

            if isUp: pY -= directionalSpeed
            if isDown: pY += directionalSpeed
            if isRight: pX += directionalSpeed
            if isLeft: pX -= directionalSpeed

            if pX > sW-pSize: pX = sW-pSize
            if pY > sH-pSize: pY = sH-pSize
            if pX < 0: pX = 0
            if pY < 0: pY = 0

            for e in entityList:
                if e.contact(pX, pY):
                    playerDead = True
                    instructions5.updateText("Last Score Was " + str(scoreInt))
                e.update()
                if (e.isAlive == False):
                    entityList.remove(e)
                e.draw(screen)
                
            if coinDead:
                coinX = randint(200, sW-200)
                coinY = randint(100, sH-100)
                coinDead = False

            if abs(pX - coinX) < 25:
                if abs(pY-coinY) < 25:
                    coinDead = True
                    scoreInt += 1
                    score.updateText(str(scoreInt))

            pygame.draw.rect(screen, pygame.Color(255,255,0), pygame.Rect(coinX, coinY, 25, 25))    
            
            pygame.draw.rect(screen, pygame.Color(0,0,255), pygame.Rect(pX, pY, pSize, pSize))

            score.drawText(screen)
                    
            clock.tick(60)
            pygame.display.flip()
            screen.fill(pygame.Color(0,0,0))
 
    pygame.quit()
 
if __name__ == "__main__":
    main()