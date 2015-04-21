import pygame, sys, math, csv, time
from pygame.locals import *

""" Problems to solve:

Implement a maximum velocity for the cat- make sure that it can't go too fast. 

Implement a "wall" feature- the cat's velocity should go to 0 whenever it hits a wall (only negating y velocity if it hits the top or bottom,
and only negating x velocity if it hits the sides)

Bonus: the cat currently negates both up and down motion when either a up or a down key is released (and same for left/right).
Fix this so that the cat is still affected by the button currently pressed. 

"""

def game():
    
    pygame.init()
    
    FPS = 60 # frames per second setting
    fps_clock = pygame.time.Clock()
    screen_width = 700
    screen_height = 400
    DISPLAYSURF = pygame.display.set_mode([screen_width, screen_height])
    
    WINDOWWIDTH = pygame.display.Info().current_w
    WINDOWHEIGHT = pygame.display.Info().current_h

    pygame.display.set_caption('Simple Game')
    
    black = (0,0,0)
    
    def terminate():
        pygame.quit()
        sys.exit()
        
    def wait_key():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        terminate()
                    if event.key == K_RETURN:
                        return
                    
    while True: # the main game loop

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    wait_key()

                    
        DISPLAYSURF.fill(black)
                
        pygame.display.update()
        fps_clock.tick(FPS)
    
game()
