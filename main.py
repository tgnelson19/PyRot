from math import pi, floor
from random import randint
import pygame

from bullet import bullet
from entity import entity
from boss import boss
from bomb import bomb
from phases import phases
from textThing import textThing

# Aspect Ratio Setter

sH = 720
sW = 1280

def main():

    # Basic initializations for the game to run

    pygame.init()
    size = [sW, sH]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PyRot")
    done = False
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 200)

    # Creating the lists that hold all of the texts of the game

    testingTextThing = textThing(" ", 0,0,pygame.Color(0,0,0,))

    openingTextList = []
    score = textThing("0", sW - 60, 20, pygame.Color(255,255,255))
    start = textThing("MicroDodging", 100, sH/3, pygame.Color(0,0,0))
    openingTextList.append(start)
    instructions = textThing("Press Space Key To Play", 100, sH/3 + 50, pygame.Color(0,0,0))
    openingTextList.append(instructions)
    instructions2 = textThing("Use Arrow Keys To Change Difficulty", 100, sH/3 + 100, pygame.Color(0,0,0))
    openingTextList.append(instructions2)
    instructions3 = textThing("Press Escape To Close", 100, sH/3 + 150, pygame.Color(0,0,0))
    openingTextList.append(instructions3)
    instructions4 = textThing("Nothing", 900, sH/3, pygame.Color(0,0,0))
    openingTextList.append(instructions4)
    instructions5 = textThing("", 150, sH-100, pygame.Color(0,0,0))
    openingTextList.append(instructions5)

    # Game logic initializations (Can still be further reduced by a player and coin library, though I don't know
    # the exact directions the game is taking quite yet)

    trueSpeed = 5
    directionalSpeed = 5
    whatYaWantAsPlayerHp = 10
    coinDead = True
    playerDead = True
    phase = phases()

    # Main while loop that runs the entirety of the game

    while not done:

        if playerDead:

            #When the player dies, reset all of the phase logic as to not have the game repeat any past events

            phase.reset()
            entityList = []
            scoreInt = 0
            coinX = randint(200, sW-200)
            coinY = randint(100, sH-100)
            pX = sW/2
            pY = sH/2
            pSize = 25
            playerHealth = whatYaWantAsPlayerHp
            maxPlayerHealth = whatYaWantAsPlayerHp
            isUp = False
            isDown = False
            isLeft = False
            isRight = False
            bossi = boss()
            #entityList.append(bossi) # Still working on fixing the boss, he's hard to control at the moment
            phase.setPhaseName("nothing") # Default phase name to kickstart any difficulty the player chooses
            
            # Archaic text handling, but it gets the job done for the moment

            score.updateText("0")
            instructions4.updateText(phase.getDifficulty())
            for i in openingTextList:
                i.drawText(screen)

            # testingTextThing.drawANewText("Hi there", 100, 100, pygame.Color(0,0,0), screen) # A Test for potential fixes to future text rendering

            # Difficulty choice logic handling

            for event in pygame.event.get():
                if event.type == pygame.QUIT: done = True
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE:done = True
                    elif event.key == pygame.K_UP: phase.difficultyUp()
                    elif event.key == pygame.K_DOWN: phase.difficultyDown()
                    elif event.key == pygame.K_SPACE: playerDead = False

            # End of menu loop

            clock.tick(60)
            pygame.display.flip()
            screen.fill(pygame.Color(255,255,255))

        else: # Main game loop

            # Event handler

            for event in pygame.event.get():

                if event.type == pygame.USEREVENT: # Runs a new phase process every time the desired tickspeed has been met
                    phase.runPhase(entityList, bossi)

                if event.type == pygame.QUIT: done = True 

                if event.type == pygame.KEYDOWN: # Moves the player any 
                    if event.key == pygame.K_w or event.key == pygame.K_UP: isUp = True
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN: isDown = True
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT: isLeft = True
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT: isRight = True

                    if event.key == pygame.K_ESCAPE:
                        playerDead = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_UP: isUp = False
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN: isDown = False
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT: isLeft = False
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT: isRight = False

            if isUp & isLeft | isUp & isRight | isDown & isLeft | isDown & isRight: directionalSpeed = trueSpeed * 0.707
            else: directionalSpeed = trueSpeed # Prevents player speed from being too fast if going diagonally

            # Player movement logic

            if isUp: pY -= directionalSpeed
            if isDown: pY += directionalSpeed
            if isRight: pX += directionalSpeed
            if isLeft: pX -= directionalSpeed

            if pX > sW-pSize: pX = sW-pSize
            if pY > sH-pSize: pY = sH-pSize
            if pX < 0: pX = 0
            if pY < 0: pY = 0

            # Entity update logic

            phpcolor = floor(255*((maxPlayerHealth - playerHealth)/maxPlayerHealth)) # prevents negative colors

            for e in entityList:
                if e.contact(pX, pY) and e.getCHP(): # Player hit logic
                    e.setCHP(False)
                    playerHealth -= 1
                    if playerHealth == 0:
                        playerDead = True
                        instructions5.updateText("Last Score Was " + str(scoreInt) + " on difficulty " + phase.getDifficulty())
                e.draw(screen)
                e.update()
                if (e.isAlive == False):
                    entityList.remove(e)

            # Coin life logic
                
            if coinDead:
                coinX = randint(200, sW-200)
                coinY = randint(100, sH-100)
                coinDead = False

            if abs(pX - coinX) < 25:
                if abs(pY-coinY) < 25:
                    coinDead = True
                    scoreInt += 1
                    score.updateText(str(scoreInt))

            # Draws the rest to the screen and updates it

            pygame.draw.rect(screen, pygame.Color(255,255,0), pygame.Rect(coinX, coinY, 25, 25))    
            
            pygame.draw.rect(screen, pygame.Color(0,0,255), pygame.Rect(pX, pY, pSize, pSize))

            pygame.draw.rect(screen, pygame.Color(phpcolor, 255 - phpcolor, 0), pygame.Rect(pX - 5, pY + 30, floor(35 - 35* (maxPlayerHealth - playerHealth)/maxPlayerHealth), 6))

            score.drawText(screen)
                    
            clock.tick(60)
            pygame.display.flip()
            screen.fill(pygame.Color(0,0,0))
 
    pygame.quit()
 
if __name__ == "__main__":
    main()