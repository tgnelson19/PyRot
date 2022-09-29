import pygame

def main():
    pygame.init()
 
    # Set the height and width of the screen
    size = [960, 540]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("PyRot")
 
   
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                done = True
 
        
        
        clock.tick(60)
        pygame.display.flip()
 
    
    pygame.quit()
 
if __name__ == "__main__":
    main()