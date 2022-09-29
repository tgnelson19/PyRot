from random import randint
import pygame

def main():
    pygame.init()
 
    size = [960, 540]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("PyRot")
 
   
    done = False
 
    clock = pygame.time.Clock()

    pygame.time.set_timer(pygame.USEREVENT, 2000)

    TBPosX = randint(20, 940)

    bulletedXList = []

    bulletedYList = []

    pX = 480
    pY = 270

    trueSpeed = 5
    directionalSpeed = 5

    isUp = False
    isDown = False
    isLeft = False
    isRight = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: isUp = True
                if event.key == pygame.K_s: isDown = True
                if event.key == pygame.K_a: isLeft = True
                if event.key == pygame.K_d: isRight = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w: isUp = False
                if event.key == pygame.K_s: isDown = False
                if event.key == pygame.K_a: isLeft = False
                if event.key == pygame.K_d: isRight = False

            if event == pygame.USEREVENT:
                print('Making a new bullet')
                bulletedXList.append(randint(20, 940))
                bulletedYList.append(0)

        if isUp & isLeft | isUp & isRight | isDown & isLeft | isDown & isRight: directionalSpeed = trueSpeed * 0.707
        else: directionalSpeed = trueSpeed

        if isUp: pY -= directionalSpeed
        if isDown: pY += directionalSpeed
        if isRight: pX += directionalSpeed
        if isLeft: pX -= directionalSpeed




        
        
        
        
        
        for b in bulletedYList:
            b += 3
            pygame.draw.rect(screen, pygame.Color(255,0,0), pygame.Rect(bulletedXList(bulletedYList.index(b)), b, 25, 25))
            if b > 540:
                bulletedXList.remove(bulletedYList.index(b))
                bulletedYList.remove(b)
        
        
        
        pygame.draw.rect(screen, pygame.Color(0,0,255), pygame.Rect(pX, pY, 25, 25))
                
        clock.tick(60)
        pygame.display.flip()
        screen.fill(pygame.Color(0,0,0))
 
    
    pygame.quit()
 
if __name__ == "__main__":
    main()