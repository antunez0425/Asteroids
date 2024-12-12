import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    Player.containers = updatable, drawable
    Asteroid.containers = updatable, drawable, asteroid
    AsteroidField.containers = updatable

    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color('black'))


        for u in updatable:
            u.update(dt)
        for d in drawable:
            d.draw(screen)
        for a in asteroid:
            if a.collides_with(player1):
                print ("Game over!")
                return


        pygame.display.flip()
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()