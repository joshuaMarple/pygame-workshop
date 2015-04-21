import pygame, random, sys
from pygame.locals import *
import globalDefs
# from bear import *
from player import Player
def startGame():
    pygame.init()
    mainClock = pygame.time.Clock()

    window_surface = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    globalDefs.WINDOWWIDTH = pygame.display.Info().current_w
    globalDefs.WINDOWHEIGHT = pygame.display.Info().current_h
    globalDefs.background = pygame.transform.scale(pygame.image.load('./resources/space.jpg').convert_alpha(), (globalDefs.WINDOWWIDTH, globalDefs.WINDOWHEIGHT))
    pygame.display.set_caption('Space Destroyer')
    pygame.mouse.set_visible(False)
    window_surface.fill(globalDefs.BACKGROUNDCOLOR)
    window_surface.blit(globalDefs.background, (-10,-10))
    font = pygame.font.Font("./resources/manteka.ttf", 30)
    
    player = Player()
        
    
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

    def drawText(text, font, surface, x, y):
        textobj = font.render(text, 1, globalDefs.TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x,y)
        surface.blit(textobj, textrect)

    def clear_screen():
        window_surface.fill(globalDefs.BACKGROUNDCOLOR)
        window_surface.blit(globalDefs.background, (0,0))
        
    def redraw():
        global window
        window_surface.fill(globalDefs.BACKGROUNDCOLOR)
        window_surface.blit(globalDefs.background, (0,0))

        window_surface.blit(player.image, player.rect)
        
        player.update(window_surface)
        
        pygame.display.update()

        mainClock.tick(globalDefs.FPS)

    def event_checker(event):
        if event.type == QUIT:
            terminate()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                player.move_mod(True, False)
            if event.key == K_UP:
                player.move_mod(False, True)
            if event.key == K_SPACE:
                player.fire_laser()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                drawText('press enter to unpause', font, window_surface, (globalDefs.WINDOWWIDTH /3), (globalDefs.WINDOWHEIGHT / 3))
                drawText('press esc again to exit', font, window_surface, (globalDefs.WINDOWWIDTH /3), (globalDefs.WINDOWHEIGHT / 3) + 50)
                pygame.display.update()
                wait_key()
            if event.key == K_UP:
                player.move_mod(False, False)
            if event.key == K_DOWN:
                player.move_mod(False, False)


    window_surface.fill(globalDefs.BACKGROUNDCOLOR)
    window_surface.blit(globalDefs.background, (0,0))

    while True:
        for event in pygame.event.get():
            event_checker(event)
        
        redraw()
        
