from math import pi
from random import randint
import pygame

from bullet import bullet
from entity import entity
from boss import boss
from bomb import bomb
from phases import phases

def main():
    pygame.init()
 
    size = [960, 540]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("PyRot")
 
    font = pygame.font.Font('freeFont.otf', 32)

    score = font.render('0', True, pygame.Color(255,255,255))
    scoreRect = score.get_rect()
    scoreRect.center = (900, 20)

    start = font.render('MicroDodging', True, pygame.Color(0,0,0))
    startRect = score.get_rect()
    startRect.center = (280, 270)

    instructions = font.render('Press Any Key To Play', True, pygame.Color(0,0,0))
    instructionsRect = score.get_rect()
    instructionsRect.center = (280, 320)

    scoreInt = 0

    done = False
 
    clock = pygame.time.Clock()

    pygame.time.set_timer(pygame.USEREVENT, 200)

    entityList = []

    pX = 480
    pY = 270
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

    while not done:

        if playerDead:

            phase.reset()

            scoreInt = 0

            isUp = False
            isDown = False
            isLeft = False
            isRight = False

            pX = 480
            pY = 270

            coinX = randint(200, 720)
            coinY = randint(100, 400)

            score = font.render(str(scoreInt), True, pygame.Color(255,255,255))

            entityList.clear()
            

            screen.fill(pygame.Color(255,255,255))
            screen.blit(start, startRect)
            screen.blit(instructions, instructionsRect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: done = True
                if event.type == pygame.KEYDOWN: playerDead = False

            clock.tick(60)
            pygame.display.flip()

            phase.setPhaseName("patience")

        else:

            for event in pygame.event.get():

                if event.type == pygame.USEREVENT:
                    
                    
                    if (phase.getPhaseName() == "patience"):
                        
                        phase.runPatience(entityList)

                    elif (phase.getPhaseName() == "firewalls"):

                        phase.runFirewall(entityList)
                    
                    
                if event.type == pygame.QUIT: done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP: isUp = True
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN: isDown = True
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT: isLeft = True
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT: isRight = True

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

            if pX > 935: pX = 935
            if pY > 515: pY = 515
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
                coinX = randint(200, 760)
                coinY = randint(100, 440)
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