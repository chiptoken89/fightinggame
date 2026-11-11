import pygame
from constants import *

class RectShape(pygame.sprite.Sprite):
    def __init__(self, x, y):
        
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
        self.rect = pygame.Rect(x,y,30,50)
    def draw(self, screen):
        pass
    def update(self):
        pass
        