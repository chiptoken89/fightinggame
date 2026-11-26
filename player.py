import pygame
from constants import *
class Player():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x,y,30,50)
        self.speed = 3
        self.gravity = 7
        self.jump_velocity_initial = 10
        self.jumpstatus = False
    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.rect)
        
    def update(self):
        
        keys = pygame.key.get_pressed()
        #LEFT AND RIGHT MOVEMENT
        if keys[pygame.K_a]: #left
    
            self.rect.x -= self.speed
        if keys[pygame.K_d]: #right
            
            self.rect.x += self.speed
        velocity = self.jump_velocity_initial
        #JUMPING
        
        if self.jumpstatus:
            while self.rect.y < FLOOR_POSITION:
                self.rect.y -= velocity
                #velocity -=self.gravity
            self.jumpstatus = False
    def handle_jump(self, event):
        #put in event loop 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.jumpstatus = True
            
                    
                    
                    
        # refer to asteroids game for method stuff, can probably 
        #fix whatever is going on now from that
            
        