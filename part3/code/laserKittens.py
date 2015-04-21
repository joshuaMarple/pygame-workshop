import pygame, random, sys
from pygame.locals import *
import globalDefs
from bear import *
from player import Player
def startGame():
    pygame.init()
    mainClock = pygame.time.Clock()

    windowSurface = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    globalDefs.WINDOWWIDTH = pygame.display.Info().current_w
    globalDefs.WINDOWHEIGHT = pygame.display.Info().current_h
    globalDefs.background = pygame.transform.scale(pygame.image.load('./res/space.jpg').convert_alpha(), (globalDefs.WINDOWWIDTH, globalDefs.WINDOWHEIGHT))
    # globalDefs.background = pygame.transform.scale(background, (globalDefs.WINDOWWIDTH, globalDefs.WINDOWHEIGHT))
    pygame.display.set_caption('Kitten Lasers')
    pygame.mouse.set_visible(False)
    windowSurface.fill(globalDefs.BACKGROUNDCOLOR)
    windowSurface.blit(globalDefs.background, (-10,-10))
    font = pygame.font.Font("./res/manteka.ttf", 30)
    
    beary = bear()
    beary.center()
    player = Player()
    beary.summon()
    
    def terminate():
        pygame.quit()
        sys.exit()

    def waitKey():
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

    def clearScreen():
        windowSurface.fill(globalDefs.BACKGROUNDCOLOR)
        windowSurface.blit(globalDefs.background, (0,0))
        
    def redraw():
        global window
        windowSurface.fill(globalDefs.BACKGROUNDCOLOR)
        windowSurface.blit(globalDefs.background, (0,0))
        
        if (beary.isSummoned()):
            beary.chargeBear(windowSurface)
            windowSurface.blit(beary.BearPic, beary.bearRect)

            # beary.splazers(windowSurface, planets)

        windowSurface.blit(player.image, player.rect)
        
        player.update(windowSurface)
        player.rockets.update()
        
        pygame.display.update()

        mainClock.tick(globalDefs.FPS)

    def eventChecker(event):
        if event.type == QUIT:
            terminate()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                player.moveModder(True, False)
                beary.moveModder(True, False)
            if event.key == K_UP:
                player.moveModder(False, True)
                beary.moveModder(False, True)
            if event.key == K_SPACE:
                # kit.laserFire = True
                player.fireRockets()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                drawText('press enter to unpause', font, windowSurface, (globalDefs.WINDOWWIDTH /3), (globalDefs.WINDOWHEIGHT / 3))
                drawText('press esc again to exit', font, windowSurface, (globalDefs.WINDOWWIDTH /3), (globalDefs.WINDOWHEIGHT / 3) + 50)
                pygame.display.update()
                waitKey()
            if event.key == K_UP:
                player.moveModder(False, False)
                beary.moveModder(False, False)
            if event.key == K_DOWN:
                player.moveModder(False, False)
                beary.moveModder(False, False)


    windowSurface.fill(globalDefs.BACKGROUNDCOLOR)
    windowSurface.blit(globalDefs.background, (0,0))

    while True:
        for event in pygame.event.get():
            eventChecker(event)

        beary.update()

        # laserColDet(kit, beary)
        
        redraw()
        
