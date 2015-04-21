import pygame, random, sys
from pygame.locals import *

def startGame():
    
    pygame.init()
    mainClock = pygame.time.Clock()

    TEXTCOLOR = (0,0,0)
    BACKGROUNDCOLOR = (255,255,255)
    FPS = 60
    windowSurface = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    # windowSurface = pygame.display.set_mode((1000,700))
    WINDOWWIDTH = pygame.display.Info().current_w
    WINDOWHEIGHT = pygame.display.Info().current_h
    # planet = pygame.image.load('./res/okayplanet.png').convert_alpha()
    background = pygame.transform.scale(pygame.image.load('./res/space.png').convert_alpha(), (WINDOWWIDTH, WINDOWHEIGHT))
            
    pygame.display.set_caption('Space Destructor')
    pygame.mouse.set_visible(False)
    windowSurface.fill(globalDefs.BACKGROUNDCOLOR)
    windowSurface.blit(globalDefs.background, (0,0))
    font = pygame.font.Font("./res/manteka.ttf", 30)

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
        textobj = font.render(text, 1, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x,y)
        surface.blit(textobj, textrect)

    def clearScreen():
        windowSurface.fill(BACKGROUNDCOLOR)
        windowSurface.blit(background, (0,0))

    def redraw(kit, bear, planets):
        global window
        windowSurface.fill(BACKGROUNDCOLOR)
        windowSurface.blit(background, (0,0))
        
        #draw text
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Earth Health: %s' % (EarthHealth), font, windowSurface, 10, 48)
        drawText('spaceCat Health: %s' % (kit.health), font, windowSurface, 10, 96)
        # drawText('spaceBear Health: %s' % (bear.health), font, windowSurface, 10, 144)
        # for p in planets:
            # windowSurface.blit(p['surface'], p['rect'])
        planets.update();
        planets.draw(windowSurface)
        kit.chargeKitty(windowSurface)
        windowSurface.blit(kit.kittyPic, kit.kitRect)
        kit.splazers(windowSurface, planets)

        if (beary.isSummoned()):
            beary.chargeBear(windowSurface)
            windowSurface.blit(beary.BearPic, beary.bearRect)

            beary.splazers(windowSurface, planets)

        windowSurface.blit(corg.image, corg.rect)
        corg.update(kit.kitRect, windowSurface, planets)
        # corg.rockets.update(windowSurface)
        pygame.display.update()

        earthHealthIncrementer()
        mainClock.tick(FPS)

    def earthHealthIncrementer():
        earthHealthCounter +=1
        if (earthHealthCounter > 100 & EarthHealth < 100):
            EarthHealth += 1
            earthHealthCounter = 0

    def earthChecker():
        if EarthHealth <= 0:
            EarthHealth = 100
            earthDead()

    def eventChecker(event, kit):
        if event.type == QUIT:
            terminate()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                kit.moveModder(True, False)
                beary.moveModder(True, False)
            if event.key == K_UP:
                kit.moveModder(False, True)
                beary.moveModder(False, True)

            if event.key == K_LCTRL:
                corg.fireRockets()
            if event.key == K_SPACE:
                kit.laserFire = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                drawText('press enter to unpause', font, windowSurface, (WINDOWWIDTH /3), (WINDOWHEIGHT / 3))
                drawText('press esc again to exit', font, windowSurface, (WINDOWWIDTH /3), (WINDOWHEIGHT / 3) + 50)
                pygame.display.update()
                waitKey()
            if event.key == K_UP:
                kit.moveModder(False, False)
                beary.moveModder(False, False)
            if event.key == K_DOWN:
                kit.moveModder(False, False)
                beary.moveModder(False, False)
            if event.key == K_SPACE:
                kit.laserFire = False

    def scoreChecker():
        if (score > 1):
            if (score % 100 == 0):
                score += 1
                beary.summon()
                kit.health = 100
                beary.health = 100
                for i in planets[:]:
                    planets.remove(i)

    def laserColDet(kit, beary):
        if kit.laserRect.colliderect(beary.bearRect) & kit.laserFire == True & beary.isSummoned() == True:
            beary.health -= kit.kitCharge/100.
        if beary.laserRect.colliderect(kit.kitRect) & beary.laserFire == True:
            kit.health -= beary.bearCharge/100.

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(background, (0,0))
    
    kit = kitty()
    kit.center()
    beary = bear()
    beary.center()
    corg = Corgi()
    kitOptions = {"dead", kitDead}
    while True:
        for event in pygame.event.get():
            eventChecker(event, kit)

        if (kit.update() == "dead"):
            kitDead()

        # beary.update()

        # redraw(kit, beary, planets)
