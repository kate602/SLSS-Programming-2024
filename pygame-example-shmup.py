# pygame-example-shmup.py
import random
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

ENEMYSHIP = pg.image.load("./Images/ufo.png")
ENEMYSHIP = pg.transform.scale(
    ENEMYSHIP, (ENEMYSHIP.get_width() // 2, ENEMYSHIP.get_height() // 2)
        )  

BULLET1 = pg.image.load("./Images/pinkprojectile.gif")
BULLET1 = pg.transform.rotate(BULLET1, 90)
BULLET1 = pg.transform.scale(
    BULLET1, (BULLET1.get_width() // 7, BULLET1.get_height() // 7)
        )  

BULLET2 = pg.image.load("./Images/pinkbubble.webp")
BULLET2 = pg.transform.rotate(BULLET2, 90)
BULLET2 = pg.transform.scale(
    BULLET2, (BULLET2.get_width() // 12, BULLET2.get_height() // 12)
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

        # Spawn at PLAYER
        self.rect.centerx = player_loc[0]
        self.rect.bottom = player_loc[1]


        self.vel_y = -4

    def update(self):
        self.rect.y += self.vel_y

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = ENEMYSHIP
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = HEIGHT - 1000

        self.vel_x = random.choice((-6, -3, 3, 6))

    def update(self):
        self.rect.x += self.vel_x

        if self.rect.left < 0:
            self.rect.left = 0
            self.vel_x = -self.vel_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.vel_x = -self.vel_x

def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()
    score = 0
    font = pg.font.SysFont("Futura", 24)

    # Sprite groups
    all_sprites = pg.sprite.Group()
    bullet_sprites = pg.sprite.Group()
    enemy_sprites = pg.sprite.Group()

    # Create the Player sprite object
    player = Player()
    all_sprites.add(player)

    pg.display.set_caption("Shoot 'Em UPPPPPPPP")
  
    # create enemy sprite objects
    for _ in range(4):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                bullet = Bullet((player.rect.centerx, player.rect.top))
                all_sprites.add(bullet)
                bullet_sprites.add(bullet)
        # --- Update the world state
        all_sprites.update()

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)

        score_image = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_image, (5, 5))

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps

        # delete bullet once off screen
        for sprite in bullet_sprites:
            if sprite.rect.y > HEIGHT-100:
                sprite.kill()

        # increase score once bullet hits enemy
        for bullet in bullet_sprites:
            enemies_hit = pg.sprite.spritecollide(bullet, enemy_sprites, True)

            for enemies in enemies_hit:
              score += 1
              bullet.kill()


def main():
    start()


if __name__ == "__main__":
    main()
