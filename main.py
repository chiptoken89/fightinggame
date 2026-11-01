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
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(200, 200)
    i = 0 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                return
        screen.fill("blue")
        #for item in drawable:
        for item in drawable:
            item.draw(screen)
        updatable.update()
        i+=1
        print(i)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
