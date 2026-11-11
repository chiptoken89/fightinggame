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
    player = Player(200, 200)
    i = 0 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                return
        screen.fill("blue")
        player.draw(screen)
        player.update()
        i+=1
        print(i)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
