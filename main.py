import pygame
from constants import *
from player import Player
import sys
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(200, 500)
    running = True
    while running:
        for event in pygame.event.get(): 
            player.handle_jump(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False
        screen.fill("blue")
        player.draw(screen)
        player.update()
        
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()
if __name__ == "__main__":
    main()
