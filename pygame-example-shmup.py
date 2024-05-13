# pygame-example-shmup.py

import pygame as pg

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 720
HEIGHT = 1000
SCREEN_SIZE = (WIDTH, HEIGHT)

SHIP = pg.image.load("./Images/pinkship.gif")
SHIP = pg.transform.scale(
    SHIP, (SHIP.get_width() // 7, SHIP.get_height() // 7)
        )  


BULLET = pg.image.load("./Images/pinkprojectile.gif")
BULLET = pg.transform.rotate(BULLET, 90)
BULLET = pg.transform.scale(
    BULLET, (BULLET.get_width() // 7, BULLET.get_height() // 7)
        )  

BULLET2 = pg.image.load("./Images/pinkbubble.webp")
BULLET2 = pg.transform.rotate(BULLET2, 90)
BULLET2 = pg.transform.scale(
    BULLET2, (BULLET2.get_width() // 7, BULLET2.get_height() // 7)
        )  

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = SHIP
        self.rect = self.image.get_rect()

    def update(self):
        """Follow the mouse"""
        self.rect.center = pg.mouse.get_pos()

        # Keep it at the bottom of the screen
        if self.rect.top < HEIGHT - 200:
            self.rect.top = HEIGHT - 200

class Bullet(pg.sprite.Sprite):
    def __init__(self, player_loc: list):
        """
        Params:
            player_loc: x,y coords of centerx and top
        """
        super().__init__()

        self.image = BULLET2

        self.rect = self.image.get_rect()

        # Spawn at the Player
        self.rect.centerx = player_loc[0]
        self.rect.bottom = player_loc[1]


# TODO: Enemies
#      - Move left to right to left


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    # Create the Player sprite object
    player = Player()

    all_sprites.add(player)

    pg.display.set_caption("Shoot 'Em Up")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                all_sprites.add(Bullet((player.rect.centerx, player.rect.top)))

        # --- Update the world state
        all_sprites.update()

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()
