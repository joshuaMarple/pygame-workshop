import pygame, sys, random
from pygame.locals import *
from Laser import Laser
import globalDefs
class Player(pygame.sprite.Sprite):
    def __init__(self, image, direction, x_cord, y_cord):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.image = pygame.transform.scale(pygame.image.load(image), (70,70))
        self.rect = self.image.get_rect()
        self.rect.left = x_cord
        self.rect.top = y_cord
        self.playerMove = 15
        self.health = 100
        self.direction = direction
        self.moveUp = False
        self.moveDown = False
        self.lasers = pygame.sprite.Group()

    def fire_laser(self):
        newlaser = Laser()
        newlaser.rect.center = self.rect.center
        if self.direction == "right":
            newlaser.speed = -15
        self.lasers.add(newlaser)

    def update(self, windowSurface):
        for i in self.lasers:
            if i.rect.x > globalDefs.WINDOWWIDTH:
                i.kill()
                del i
        self.lasers.update()
        self.lasers.draw(windowSurface)
        self.move()
        if (self.health < 0):
            return "dead"
        
    def move_mod(self, moveUp, moveDown):
        self.moveUp = moveUp
        self.moveDown = moveDown
        
    def move(self):
        if self.moveUp and self.rect.top < globalDefs.WINDOWHEIGHT:
            self.rect.move_ip(0, self.playerMove)
        if self.moveDown and self.rect.bottom  > 0:
            self.rect.move_ip(0, -self.playerMove)
