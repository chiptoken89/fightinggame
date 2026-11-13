import pygame
from constants import *
class Player():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x,y,30,50)
        self.speed = 3
        self.gravity = 15
        self.jumpspeed = 30
    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.rect)
        
    def move(self):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            #left
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            #right
            self.rect.x += self.speed
        if keys [pygame.K_SPACE]:

            #self.rect.y += self.jumpspeed
            pass
    def jump(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                while self.rect.y <= FLOOR_POSITION:
                    self.rect.y -= self.jumpspeed
                    self.rect.y += self.gravity
    
       
            
        