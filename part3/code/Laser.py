import pygame, sys, random
from pygame.locals import *
import globalDefs
class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.image = pygame.transform.scale(pygame.image.load('./resources/laser.png'), (80,40))
        self.rect = self.image.get_rect()
        self.speed = 10

    def update(self):
        # print "i've been updated"
        self.rect.right += self.speed
        if(self.rect.right > globalDefs.WINDOWWIDTH):
            self.kill()
        # self.draw(surface)
