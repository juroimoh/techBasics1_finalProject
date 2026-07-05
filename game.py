import pygame as py, time, sys, csv, random
from pygame import mixer

py.init()
mixer.init()

    # screen setup
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption('UNNAMED')

font = py.font.SysFont("Arial", 28)

    # colors
BACKGROUND_COLOR = (16, 15, 22)
FONT_COLOR = (214, 255, 255)

    # setup
clock = py.time.Clock()

border_img = py.image.load("assets/gamebackground.png").convert_alpha()
player_img = py.image.load("assets/player.png").convert_alpha()

player = py.Rect(290, 290, 14, 14)

player_speed = 400
player_x = player.x
player_y = player.y
player_width = 14

mixer.music.load("assets/Ready.mp3")
mixer.music.set_volume(0.6)
mixer.music.play()

previous_time = time.time()

    # game loop
flag = True
while flag:
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
        player_speed = 283
    else:
        player_speed = 400

    screen.fill(BACKGROUND_COLOR)
    screen.blit(border_img, (0, 0))

    # \/ debug \/
    debug_text = font.render(f"debug:   x {player.x}   y {player.y}   |   {player_speed}", True, FONT_COLOR)
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

    player = py.Rect(player.x, player.y, 14, 14)
    screen.blit(player_img, (player.x, player.y))

    py.display.flip()

py.quit()
exit(0)
