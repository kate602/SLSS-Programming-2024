# pygame-exercise-snowscape.py

import random
import pygame as pg

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
BLUE_1 = (0, 30, 100)
WIDTH = 1280
HEIGHT = 720
TITLE = "it snowing!!"

NUM_SNOW = 100

# snow image sizes
SNOW_IMAGE = pg.image.load("./images/whitesnowflake.png")
SNOW_IMAGES = [
    pg.transform.scale(SNOW_IMAGE, (7, 7)),
    pg.transform.scale(SNOW_IMAGE, (12, 12)),
    pg.transform.scale(SNOW_IMAGE, (10, 10))
]


class Snow(pg.sprite.Sprite):
    def __init__(self, width: int):
        """
        Params:
            width: width of snow in px
        """
        super().__init__()

        # image -> visual representation
        # self.image = pg.image.load("./images/whitesnowflake.png")

        #randomizes snowflake size (distance)
        # additionalWidth = random.choice([5, 10, 15])
        self.image = random.choice(SNOW_IMAGES)

        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, WIDTH + 1)
        self.rect.centery = 0
        self.vel_y = random.choice([2, 3, 4, 5, 6])

    def update(self):
        self.rect.y += self.vel_y

def main():
    pg.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pg.display.set_mode(size)
    pg.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pg.time.Clock()
    last_snow = 0

    # Create a snow sprites group
    snow_sprites = pg.sprite.Group()

    # Create more snow:
    for _ in range(10):
            snow_sprites.add(Snow(5))

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # ----- LOGIC
        snow_sprites.update()

        # kill sprite if not on screen
        for sprite in snow_sprites:
            if sprite.rect.y > HEIGHT+20:
                sprite.kill()
            #if sprite.rect.y > HEIGHT - 20:
            #    sprite.vel_y = 0

        # add a new snow if _ millseconds elapses
        if pg.time.get_ticks() - last_snow > 100:
            # set last_snow to current tick
            last_snow = pg.time.get_ticks()

            # add a snow
            for _ in range(10):
                 snow_sprites.add(Snow(5))
        
        print(len(snow_sprites))

        # ----- RENDER
        screen.fill(BLUE_1)

        # Draw all the sprite groups
        snow_sprites.draw(screen)

        # ----- UPDATE DISPLAY
        pg.display.flip()
        clock.tick(60)

    pg.quit()

def random_coords():
    x, y = (random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
    return x, y
if __name__ == "__main__":
    main()