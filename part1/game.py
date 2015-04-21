import pygame, sys, math, csv, time
from pygame.locals import *

""" Problems to solve:

Make the background white

Make the title bar match the current time
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
