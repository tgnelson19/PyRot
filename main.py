from math import pi
from random import randint
import pygame

from bullet import bullet
from entity import entity
from boss import boss
from bomb import bomb
from phases import phases

sH = 720
sW = 1280

def main():
    pygame.init()
 
    size = [sW, sH]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("PyRot")
 
    font = pygame.font.Font('freeFont.otf', 32)

    score = font.render('0', True, pygame.Color(255,255,255))
    scoreRect = score.get_rect()
    scoreRect.center = (sW - 60, 20)

    start = font.render('MicroDodging', True, pygame.Color(0,0,0))
    startRect = start.get_rect()
    startRect.center = (280, sH/2)

    instructions = font.render('Press Any Key To Play', True, pygame.Color(0,0,0))
    instructionsRect = instructions.get_rect()
    instructionsRect.center = (280, sH/2 + 50)

    instructions2 = font.render('Press Escape To Close', True, pygame.Color(0,0,0))
    instructions2Rect = instructions2.get_rect()
    instructions2Rect.center = (280, sH/2 + 100)

    instructions3 = font.render('Use Arrow Keys To Change First Phase', True, pygame.Color(0,0,0))
    instructions3Rect = instructions3.get_rect()
    instructions3Rect.center = (280, sH/2 + 150)

    

    scoreInt = 0

    done = False
 
    clock = pygame.time.Clock()

    pygame.time.set_timer(pygame.USEREVENT, 200)

    entityList = []

    pX = sW/2
    pY = sH/2
    pSize = 25

    coinX = 0
    coinY = 0

    trueSpeed = 5
    directionalSpeed = 5

    isUp = False
    isDown = False
    isLeft = False
    isRight = False

    coinDead = True
    playerDead = True

    phase = phases()

    bossi = boss()

    phase.setPhaseName("leucsins")

    while not done:

        if playerDead:

            phase.reset

            scoreInt = 0

            isUp = False
            isDown = False
            isLeft = False
            isRight = False

            pX = sW/2
            pY = sH/2

            coinX = randint(200, sW-200)
            coinY = randint(100, sH-100)

            score = font.render(str(scoreInt), True, pygame.Color(255,255,255))

            entityList.clear()
            

            screen.fill(pygame.Color(255,255,255))
            screen.blit(start, startRect)
            screen.blit(instructions, instructionsRect)
            screen.blit(instructions2, instructions2Rect)

            instructions4 = font.render(phase.getPhaseName(), True, pygame.Color(0,0,0))
            instructions4Rect = instructions4.get_rect()
            instructions4Rect.center = (800, sH/2 + 100)
            screen.blit(instructions4, instructions4Rect)

            

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    done = True
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE:
                        done = True
                    elif event.key == pygame.K_UP: 
                        phase.phaseUp()
                    elif event.key == pygame.K_DOWN: 
                        phase.phaseDown()
                    else:
                        playerDead = False

            


            clock.tick(60)
            pygame.display.flip()

            

            

            

        else:

            for event in pygame.event.get():

                if event.type == pygame.USEREVENT:
                    
                    if (phase.getPhaseName() == "patience"):
                        phase.runPatience(entityList, bossi)
                    elif (phase.getPhaseName() == "firewalls"):
                        phase.runFirewall(entityList, bossi)
                    elif (phase.getPhaseName() == "slowminigun"):
                        phase.runSlowMinigun(entityList, bossi)
                    elif (phase.getPhaseName() == "fastminigun"):
                        phase.runFastMinigun(entityList, bossi)
                    elif (phase.getPhaseName() == "thirdcounter"):
                        phase.runThirdCounter(entityList, bossi)
                    elif (phase.getPhaseName() == "testing"):
                        phase.runTesting(entityList, bossi)
                    elif (phase.getPhaseName() == "testing1"):
                        phase.runTesting1(entityList, bossi)
                    elif (phase.getPhaseName() == "wigglies"):
                        phase.runTesting2(entityList, bossi)
                    elif (phase.getPhaseName() == "leucsins"):
                        phase.runLeucSins(entityList, bossi)

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
                    score = font.render(str(scoreInt), True, pygame.Color(255,255,255))

            pygame.draw.rect(screen, pygame.Color(255,255,0), pygame.Rect(coinX, coinY, 25, 25))    
            
            pygame.draw.rect(screen, pygame.Color(0,0,255), pygame.Rect(pX, pY, pSize, pSize))

            screen.blit(score, scoreRect)
                    
            clock.tick(60)
            pygame.display.flip()
            screen.fill(pygame.Color(0,0,0))
 
    pygame.quit()
 
if __name__ == "__main__":
    main()