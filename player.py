import pygame
from constants import *
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
        self.rect = pygame.Rect(x,y,30,50)
        self.speed = 3
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
            
        