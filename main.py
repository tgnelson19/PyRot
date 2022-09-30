from random import randint
import pygame

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

    pygame.time.set_timer(pygame.USEREVENT, 500)

    TbulletedXList = []
    TbulletedYList = []

    RbulletedXList = []
    RbulletedYList = []

    LbulletedXList = []
    LbulletedYList = []
    
    BbulletedXList = []
    BbulletedYList = []

    pX = 480
    pY = 270

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



    while not done:

        if playerDead:
            scoreInt = 0

            isUp = False
            isDown = False
            isLeft = False
            isRight = False

            pX = 480
            pY = 270

            coinX = randint(40, 920)
            coinY = randint(40, 500)

            score = font.render(str(scoreInt), True, pygame.Color(255,255,255))

            TbulletedXList.clear()
            TbulletedYList.clear()
            RbulletedXList.clear()
            RbulletedYList.clear()
            LbulletedXList.clear()
            LbulletedYList.clear()
            BbulletedXList.clear()
            BbulletedYList.clear()

            screen.fill(pygame.Color(255,255,255))
            screen.blit(start, startRect)
            screen.blit(instructions, instructionsRect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: done = True
                if event.type == pygame.KEYDOWN: playerDead = False

            clock.tick(60)
            pygame.display.flip()
        else:

            for event in pygame.event.get():

                if event.type == pygame.USEREVENT:
                    TbulletedXList.append(randint(20, 940))
                    TbulletedYList.append(-25)

                    BbulletedXList.append(randint(20, 940))
                    BbulletedYList.append(540)

                    LbulletedXList.append(-25)
                    LbulletedYList.append(randint(20, 520))

                    RbulletedXList.append(960)
                    RbulletedYList.append(randint(20, 520))

                

                
                    
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


            
            
            
            
            
            for b in TbulletedYList:
                
                pygame.draw.rect(screen, pygame.Color(255,0,0), pygame.Rect(TbulletedXList[TbulletedYList.index(b)], b, 25, 25))
                if b > 540:
                    TbulletedXList.remove(TbulletedXList[TbulletedYList.index(b)])
                    TbulletedYList.remove(b)
                else:
                    TbulletedYList[TbulletedYList.index(b)] = b + 2

            for b in BbulletedYList:
                
                pygame.draw.rect(screen, pygame.Color(255,0,0), pygame.Rect(BbulletedXList[BbulletedYList.index(b)], b, 25, 25))
                if b < -25:
                    BbulletedXList.remove(BbulletedXList[BbulletedYList.index(b)])
                    BbulletedYList.remove(b)
                else:
                    BbulletedYList[BbulletedYList.index(b)] = b - 2

            for b in RbulletedXList:
                
                pygame.draw.rect(screen, pygame.Color(255,0,0), pygame.Rect(b, RbulletedYList[RbulletedXList.index(b)], 25, 25))
                if b < -25:
                    RbulletedYList.remove(RbulletedYList[RbulletedXList.index(b)])
                    RbulletedXList.remove(b)
                else:
                    RbulletedXList[RbulletedXList.index(b)] = b - 2

            for b in LbulletedXList:
                
                pygame.draw.rect(screen, pygame.Color(255,0,0), pygame.Rect(b, LbulletedYList[LbulletedXList.index(b)], 25, 25))
                if b > 960:
                    LbulletedYList.remove(LbulletedYList[LbulletedXList.index(b)])
                    LbulletedXList.remove(b)
                else:
                    LbulletedXList[LbulletedXList.index(b)] = b + 2


            if coinDead:
                coinX = randint(40, 920)
                coinY = randint(40, 500)
                coinDead = False

            for b in BbulletedXList:
                if abs(b - pX) < 25:
                    if abs(BbulletedYList[BbulletedXList.index(b)] - pY) < 25:
                        playerDead = True

            for b in TbulletedXList:
                if abs(b - pX) < 25:
                    if abs(TbulletedYList[TbulletedXList.index(b)] - pY) < 25:
                        playerDead = True

            for b in RbulletedXList:
                if abs(b - pX) < 25:
                    if abs(RbulletedYList[RbulletedXList.index(b)] - pY) < 25:
                        playerDead = True

            for b in LbulletedXList:
                if abs(b - pX) < 25:
                    if abs(LbulletedYList[LbulletedXList.index(b)] - pY) < 25:
                        playerDead = True


            if abs(pX - coinX) < 25:
                if abs(pY-coinY) < 25:
                    coinDead = True
                    scoreInt += 1
                    score = font.render(str(scoreInt), True, pygame.Color(255,255,255))

            

            pygame.draw.rect(screen, pygame.Color(255,255,0), pygame.Rect(coinX, coinY, 25, 25))    
            
            pygame.draw.rect(screen, pygame.Color(0,0,255), pygame.Rect(pX, pY, 25, 25))

            screen.blit(score, scoreRect)
                    
            clock.tick(60)
            pygame.display.flip()
            screen.fill(pygame.Color(0,0,0))
 
    
    pygame.quit()
 
if __name__ == "__main__":
    main()