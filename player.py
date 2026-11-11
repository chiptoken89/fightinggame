import pygame
from constants import *
class Player():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x,y,30,50)
        self.speed = 3
        self.gravity = 10
    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.rect )
        
    def update(self):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            #left
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_d]:
            #right
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_s]:
            #crouch
            pass
        if keys[pygame.K_SPACE]:
            #jump
            pass
            
        