import pygame, sys, math, csv, time
from pygame.locals import *

""" Problems to solve:

Implement a maximum velocity for the cat- make sure that it can't go too fast. 

Implement a "wall" feature- the cat's velocity should go to 0 whenever it hits a wall (only negating y velocity if it hits the top or bottom,
and only negating x velocity if it hits the sides)

Bonus: the cat currently negates both up and down motion when either a up or a down key is released (and same for left/right).
Fix this so that the cat is still affected by the button currently pressed. 

"""

class player(pygame.sprite.Sprite):
    def __init__(self, name, image, xpos, ypos, width, height):
        self.name = name
        self.health = health
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        # self.image.fill(RED)
        self.rect.x = xpos
        self.rect.y = ypos
        self.actions = actions
        self.fight_menu = fightMenu(self, self.actions)
        self.fight_menu.hide()
        pygame.sprite.Sprite.__init__(self)
        
    def damage(self, pain):
        self.health -= pain
        if self.health < 0:
            self.fight_menu.hide()
            # del self.fight_menu
            self.kill()

    def attack(self):
        return 10 # for now
        
    def update(self, surface):
        self.fight_menu.update()
        surface.blit(self.image, self.rect)
        
    def click(self):
        # global selected_player
        # selected_player = self
        # print(selected_player)
        self.fight_menu.show()

    def unselect(self):
        self.fight_menu.hide()

def game():
    
    player_x_vel = 0.0
    player_y_vel = 0.0

    pygame.init()
    
    FPS = 60 # frames per second setting
    fps_clock = pygame.time.Clock()
    
    DISPLAYSURF = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    
    WINDOWWIDTH = pygame.display.Info().current_w
    WINDOWHEIGHT = pygame.display.Info().current_h

    pygame.display.set_caption('Simple Game')
    
    black = (0,0,0)
    player_img = pygame.image.load('cat.png')
    player_x = 0.0
    player_y = 0.0
    speed = 0.5
    
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

    cur_vel_flags = {"x_vel": 0, "y_vel": 0}
                    
    while True: # the main game loop
        DISPLAYSURF.fill(black)
        DISPLAYSURF.blit(player_img, (player_x, player_y))
        player_x += player_x_vel
        player_y += player_y_vel

        player_x_vel += speed*cur_vel_flags["x_vel"]
        player_y_vel += speed*cur_vel_flags["y_vel"]
        
        if(player_x_vel > 0): 
            player_x_vel -= .02 # a constant friction effect
        if(player_x_vel < 0):
            player_x_vel += .02
        if(player_y_vel > 0):
            player_y_vel -= .02
        if(player_y_vel < 0):
            player_y_vel += .02

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    cur_vel_flags["y_vel"] = 1
                if event.key == K_UP:
                    cur_vel_flags["y_vel"] = -1 
                if event.key == K_LEFT:
                    cur_vel_flags["x_vel"] = -1
                if event.key == K_RIGHT:
                    cur_vel_flags["x_vel"] = 1
                        
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    wait_key()
                if event.key == K_UP or event.key == K_DOWN:
                    cur_vel_flags["y_vel"] = 0
                if event.key == K_LEFT or event.key == K_RIGHT:
                    cur_vel_flags["x_vel"] = 0
                
        pygame.display.update()
        fps_clock.tick(FPS)
    
game()
