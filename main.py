import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    # initialising the game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0 # delta time

    # setting up groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # adding classes to respective groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # creating the player object
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, radius=PLAYER_RADIUS)

    asteroid_field = AsteroidField()

    # the main game loop
    game_loop = 0
    while game_loop == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for image in drawable:
            image.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(shot) == True:
                    asteroid.split()
                    shot.kill()
        for obj in asteroids:
            if obj.collision_check(player) == True:
                print("Game over!")
                sys.exit(0)
        pygame.display.flip()
        dt = fps.tick(60)
        dt = dt / 1000


if __name__ == "__main__":
    main()
