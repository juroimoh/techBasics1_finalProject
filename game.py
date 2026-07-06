import pygame as py, time, sys, csv, random
from pygame import mixer

py.init()
mixer.init()

    # screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 600
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption('Dangan')

font = py.font.SysFont("Arial", 28)

    # colors
BACKGROUND_COLOR = (16, 15, 22)
FONT_COLOR = (214, 255, 255)

    # setup
DEBUG = False

clock = py.time.Clock()

border_img = py.image.load("assets/gamebackground.png").convert_alpha()
player_img = py.image.load("assets/player.png").convert_alpha()
player_bullet_img = py.image.load("assets/player_bullet.png").convert_alpha()

player = py.Rect(290, 290, 14, 14)

BASE_SPEED = 300
player_speed = BASE_SPEED
player_x = player.x
player_y = player.y
player_width = 14

player_bullets = []
player_bulletsl = []
player_bulletsr = []
player_bullet_reload = 0.5
player_bullet_width = 6
player_bullet_height = 16
player_bullet_speed = 550

# mixer.music.load("assets/Ready.mp3")
mixer.music.load("assets/Skyrider.mp3")
mixer.music.set_volume(0.2)
mixer.music.play()

previous_time = time.time()

def draw_player():
    global player
    player = py.Rect(player.x, player.y, 14, 14)
    screen.blit(player_img, (player.x, player.y))

def draw_player_bullets():
    for b in player_bullets:
        py.Rect(b[0], b[1], 6, 16)
        screen.blit(player_bullet_img, (b[0], b[1]))
    for b in player_bulletsl:
        py.Rect(b[0], b[1], 6, 16)
        screen.blit(player_bullet_img, (b[0], b[1]))
    for b in player_bulletsr:
        py.Rect(b[0], b[1], 6, 16)
        screen.blit(player_bullet_img, (b[0], b[1]))

    # game loop
flag = True
while flag:
    # clock.tick(30)
    dt = time.time() - previous_time
    previous_time = time.time()

    for event in py.event.get():
        if event.type == py.QUIT:
            flag = False

    keys = py.key.get_pressed()
    if keys[py.K_LEFT] and player.left > 50:
        player_x -= player_speed * dt
        player.x = round(player_x)
        if player.left < 50:
            player.x = 50
    if keys[py.K_RIGHT] and player.right < 550:
        player_x += player_speed * dt
        player.x = round(player_x)
        if player.right > 550:
            player.x = 550 - player_width
    if keys[py.K_UP] and player.top > 50:
        player_y -= player_speed * dt
        player.y = round(player_y)
        if player.top < 50:
            player.y = 50
    if keys[py.K_DOWN] and player.bottom < 550:
        player_y += player_speed * dt
        player.y = round(player_y)
        if player.bottom > 550:
            player.y = 550 - player_width
    if keys[py.K_RIGHT] and keys[py.K_UP] or keys[py.K_RIGHT] and keys[py.K_DOWN] or keys[py.K_LEFT] and keys[py.K_UP] or keys[py.K_LEFT] and keys[py.K_DOWN]:
        player_speed = round(BASE_SPEED * 0.707)
    else:
        player_speed = BASE_SPEED
    if keys[py.K_SPACE] and player_bullet_reload <= 0:
        player_bullet_reload = 0.15
        player_bullet_x = player.x + player_width / 2 - player_bullet_width / 2
        player_bullet_y = player.y - 5
        player_bullets.append([player_bullet_x, player_bullet_y])
        player_bulletsl.append([player_bullet_x, player_bullet_y])
        player_bulletsr.append([player_bullet_x, player_bullet_y])

    if player_bullet_reload > -1:
        player_bullet_reload -= 1 * dt

    screen.fill(BACKGROUND_COLOR)

    for b in player_bullets:
        b[1] -= player_bullet_speed * dt
        if b[1] < 0:
            player_bullets.remove(b)
    for b in player_bulletsl:
        b[1] -= player_bullet_speed * dt
        b[0] -= player_bullet_speed / 10 * dt
        if b[1] < 0:
            player_bulletsl.remove(b)
    for b in player_bulletsr:
        b[1] -= player_bullet_speed * dt
        b[0] += player_bullet_speed / 10 * dt
        if b[1] < 0:
            player_bulletsr.remove(b)

    draw_player_bullets()
    draw_player()

    screen.blit(border_img, (0, 0)) # Keep this rendering last.

    # \/ debug \/
    if DEBUG:
        debug_text = font.render(f"debug:   x {player.x}   y {player.y}   |   {player_speed}, {len(player_bullets)}x3", True, FONT_COLOR)
        screen.blit(debug_text, (10, 10))

        debug_top = font.render(f"{player.top}", True, FONT_COLOR)
        screen.blit(debug_top, (660, 20))
        debug_right = font.render(f"{player.right}", True, FONT_COLOR)
        screen.blit(debug_right, (700, 60))
        debug_left = font.render(f"{player.left}", True, FONT_COLOR)
        screen.blit(debug_left, (620, 60))
        debug_bottom = font.render(f"{player.bottom}", True, FONT_COLOR)
        screen.blit(debug_bottom, (660, 100))
    # /\ end debug /\

    py.display.flip()

py.quit()
exit(0)
