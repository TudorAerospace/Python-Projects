import pygame
import os
import math
import random

pygame.font.init()
pygame.mixer.init()
pygame.init()

WIDTH, HEIGHT = 1500, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Ships Multiplayer 2.0")



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (139, 0, 0)
BLUE = (0, 0, 139)


blue_rotated = False
red_rotated = False
red_health = 10
blue_health = 10
power_up_collected = False
start_ticks = pygame.time.get_ticks()

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'hit.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'fire.mp3'))
GAME_OVER_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'game-over.mp3'))
DEBRIS_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'debris_hit.mp3'))
DEBRIS_HIT_2_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'debris_hit_2.mp3'))
POWER_UP_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'power_up_sound.mp3'))

WINNER_FONT = pygame.font.SysFont('Impact', 45)

BACKGROUND = pygame.image.load(os.path.join('Assets', 'space.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

a = 2
FPS = 60
VELOCITY_RED = 6
VELOCITY_BLUE = 6
BULLET_VEL = 25
MAX_BULLETS_RED = 3
MAX_BULLETS_BLUE = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 100, 85
WIN_TEXT_WIDTH, WIN_TEXT_HEIGHT = 500, 800
HEALTH_WIDTH, HEALTH_HEIGHT = 230, 40
BULLET_GRAPH_WIDTH, BULLET_GRAPH_HEIGHT = 200, 40
POWER_UP_WIDTH, POWER_UP_HEIGHT = 60, 30
power_up_picker = 0
MAX_BULLETS_DURATION = 300  # in frames
VELOCITY_DURATION = 300     # in frames
MAIN_TITLE_WIDTH, MAIN_TITLE_HEIGHT = 909, 89

# Initialize counters for the power-up durations
max_bullets_counter = 0
velocity_counter = 0

BLUE_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

BLUE_WINS_IMAGE = pygame.image.load(os.path.join('Assets', 'blue_wins.png'))
BLUE_WINS_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    BLUE_WINS_IMAGE, (WIN_TEXT_WIDTH, WIN_TEXT_HEIGHT)), 0)
RED_WINS_IMAGE = pygame.image.load(os.path.join('Assets', 'red_wins.png'))
RED_WINS_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    RED_WINS_IMAGE, (WIN_TEXT_WIDTH, WIN_TEXT_HEIGHT)), 0)

BLUE_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_blue.png'))
BLUE_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    BLUE_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
MAIN_TITLE_IMAGE = pygame.image.load(os.path.join('Assets', 'main_title.png'))

space_debris_image = pygame.image.load(os.path.join('Assets', f'space_debris_{a}.png'))
space_debris_image = pygame.transform.scale(space_debris_image, (150, 100))

def main_menu():
    global game_started
    game_started = False
    font = pygame.font.Font(None, 24)
    button_surface = pygame.Surface((150, 50))
    text = font.render("Start Game", True, (0, 0, 0))
    text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))
    button_rect = pygame.Rect(WIDTH/2 - 75, HEIGHT/2, 150, 50)
    while game_started == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    game_started = True
        if button_rect.collidepoint(pygame.mouse.get_pos()):
         pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)
            button_surface.blit(text, text_rect)
        WIN.blit(BACKGROUND, (0,0))
        WIN.blit(MAIN_TITLE_IMAGE, (WIDTH - MAIN_TITLE_WIDTH - 270, HEIGHT/2 - MAIN_TITLE_HEIGHT*4))
        WIN.blit(button_surface, (button_rect.x, button_rect.y))
        pygame.display.update()
    


def draw_window(red, blue, red_bullets, blue_bullets, debris, power_up_location):
    global power_up
    WIN.blit(BACKGROUND, (0, 0))

    blue_health_image = pygame.image.load(os.path.join('Assets', f'health_{blue_health}.png'))
    blue_health_image = pygame.transform.scale(blue_health_image, (HEALTH_WIDTH, HEALTH_HEIGHT))
    WIN.blit(blue_health_image, (10, 10))

    red_health_image = pygame.image.load(os.path.join('Assets', f'health_{red_health}.png'))
    red_health_image = pygame.transform.scale(red_health_image, (HEALTH_WIDTH, HEALTH_HEIGHT))
    WIN.blit(red_health_image, (WIDTH - HEALTH_WIDTH - 10, 10))

    if MAX_BULLETS_BLUE == 3:
        blue_bullet_graph_image = pygame.image.load(os.path.join('Assets', f'bullets_{len(blue_bullets)}.png'))
        blue_bullet_graph_image = pygame.transform.scale(blue_bullet_graph_image, (BULLET_GRAPH_WIDTH, BULLET_GRAPH_HEIGHT))
        WIN.blit(blue_bullet_graph_image, (10, 60))
    elif MAX_BULLETS_BLUE == 4:
        blue_bullet_graph_image = pygame.image.load(os.path.join('Assets', f'bullets_up_{len(blue_bullets)}.png'))
        blue_bullet_graph_image = pygame.transform.scale(blue_bullet_graph_image, (BULLET_GRAPH_WIDTH, BULLET_GRAPH_HEIGHT))
        WIN.blit(blue_bullet_graph_image, (10, 60))

    if MAX_BULLETS_RED == 3:
        red_bullet_graph_image = pygame.image.load(os.path.join('Assets', f'bullets_{len(red_bullets)}.png'))
        red_bullet_graph_image = pygame.transform.scale(red_bullet_graph_image, (BULLET_GRAPH_WIDTH, BULLET_GRAPH_HEIGHT))
        WIN.blit(red_bullet_graph_image, (WIDTH - BULLET_GRAPH_WIDTH - 10, 60))
    elif MAX_BULLETS_RED == 4:
        red_bullet_graph_image = pygame.image.load(os.path.join('Assets', f'bullets_up_{len(red_bullets)}.png'))
        red_bullet_graph_image = pygame.transform.scale(red_bullet_graph_image, (BULLET_GRAPH_WIDTH, BULLET_GRAPH_HEIGHT))
        WIN.blit(red_bullet_graph_image, (WIDTH - BULLET_GRAPH_WIDTH - 10, 60))

    WIN.blit(BLUE_SPACESHIP, blue)
    WIN.blit(RED_SPACESHIP, red)
    if not power_up_collected:
        WIN.blit(power_up, power_up_location)

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in blue_bullets:
        pygame.draw.rect(WIN, BLUE, bullet)

    amplitude = 45
    frequency = 2
    speed = 0.04
    points = []
    for y in range(WIDTH):
        x = int(HEIGHT / 2 + amplitude * math.sin(
            frequency * ((float(y) / WIDTH) * (2 * math.pi) + (pygame.time.get_ticks() / 1000.0) * speed)))
        points.append((x, y))

    # Blit the image at a single point that moves along the wave
    y = int((pygame.time.get_ticks() / 1000.0) * speed * WIDTH) % WIDTH
    x = int(WIDTH / 2 + amplitude * math.sin(frequency * ((float(y) / WIDTH) * (2 * math.pi))))
    WIN.blit(space_debris_image, (x - 25, y))
    debris.x = x
    debris.y = y

    pygame.display.update()


def blue_handle_movement(keys_pressed, blue, debris):
    if keys_pressed[pygame.K_a] and blue.x - VELOCITY_BLUE > 0 and not debris.colliderect(blue):
        blue.x -= VELOCITY_BLUE
    if keys_pressed[pygame.K_d] and blue.x - VELOCITY_BLUE < WIDTH - SPACESHIP_WIDTH and not debris.colliderect(blue):
        blue.x += VELOCITY_BLUE
    if keys_pressed[pygame.K_w] and blue.y - VELOCITY_BLUE > 0 and not debris.colliderect(blue):
        blue.y -= VELOCITY_BLUE
    if keys_pressed[pygame.K_s] and blue.y + VELOCITY_BLUE + blue.height < HEIGHT - 15 and not debris.colliderect(blue):
        blue.y += VELOCITY_BLUE
    if debris.colliderect(blue):
        blue.x -= VELOCITY_BLUE


def red_handle_movement(keys_pressed, red, debris):
    if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY_RED > 0 and not debris.colliderect(red):
        red.x -= VELOCITY_RED
    if keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY_RED + red.width < WIDTH and not debris.colliderect(red):
        red.x += VELOCITY_RED
    if keys_pressed[pygame.K_UP] and red.y - VELOCITY_RED > 0 and not debris.colliderect(red):
        red.y -= VELOCITY_RED
    if keys_pressed[pygame.K_DOWN] and red.y + VELOCITY_RED + red.height < HEIGHT - 15 and not debris.colliderect(red):
        red.y += VELOCITY_RED
    if debris.colliderect(red):
        red.x += VELOCITY_RED


def handle_bullets(blue_bullets, red_bullets, blue, red, debris):
    global blue_rotated, red_rotated
    if not blue_rotated:
        for bullet in blue_bullets:
            bullet.x += BULLET_VEL
            if red.colliderect(bullet):
                pygame.event.post(pygame.event.Event(RED_HIT))
                blue_bullets.remove(bullet)
            elif bullet.x > WIDTH:
                blue_bullets.remove(bullet)
            if debris.colliderect(bullet):
                blue_bullets.remove(bullet)
                DEBRIS_HIT_SOUND.play()
    elif blue_rotated:
        for bullet in blue_bullets:
            bullet.x -= BULLET_VEL
            if red.colliderect(bullet):
                pygame.event.post(pygame.event.Event(RED_HIT))
                blue_bullets.remove(bullet)
            elif bullet.x < 0:
                blue_bullets.remove(bullet)
            if debris.colliderect(bullet):
                blue_bullets.remove(bullet)
                DEBRIS_HIT_SOUND.play()
    if not red_rotated:
        for bullet in red_bullets:
            bullet.x -= BULLET_VEL
            if blue.colliderect(bullet):
                pygame.event.post(pygame.event.Event(BLUE_HIT))
                red_bullets.remove(bullet)
            elif bullet.x < 0:
                red_bullets.remove(bullet)
            if debris.colliderect(bullet):
                red_bullets.remove(bullet)
                DEBRIS_HIT_2_SOUND.play()
    elif red_rotated:
        for bullet in red_bullets:
            bullet.x += BULLET_VEL
            if blue.colliderect(bullet):
                pygame.event.post(pygame.event.Event(BLUE_HIT))
                red_bullets.remove(bullet)
            elif bullet.x > WIDTH:
                red_bullets.remove(bullet)
            if debris.colliderect(bullet):
                red_bullets.remove(bullet)
                DEBRIS_HIT_2_SOUND.play()


def handle_power_ups(red, blue, power_up_location):
    global power_up, blue_health, red_health, power_up_collected, power_up_picker, VELOCITY_BLUE, VELOCITY_RED, MAX_BULLETS_RED, MAX_BULLETS_BLUE, max_bullets_counter, velocity_counter
    power_up = pygame.image.load(os.path.join('Assets', f'power_up_{power_up_picker}.png'))
    power_up = pygame.transform.scale(power_up, (POWER_UP_WIDTH, POWER_UP_HEIGHT))
    if power_up_location.colliderect(blue):
        POWER_UP_SOUND.play()
        if power_up_picker == 0:
            if blue_health == 9:
                blue_health += 1
                power_up_collected = True
            elif blue_health <= 8:
                blue_health += 2
                power_up_collected = True
            elif blue_health == 10:
                power_up_collected = True
        elif power_up_picker == 1:
            MAX_BULLETS_BLUE = 4
            max_bullets_counter = MAX_BULLETS_DURATION  # Start the counter
            power_up_collected = True
        elif power_up_picker == 2:
            VELOCITY_BLUE = 10
            velocity_counter = VELOCITY_DURATION  # Start the counter
            power_up_collected = True
    elif power_up_location.colliderect(red):
        POWER_UP_SOUND.play()
        if power_up_picker == 0:
            if red_health == 9:
                red_health += 1
                power_up_collected = True
            elif red_health <= 8:
                red_health += 2
                power_up_collected = True
            elif red_health == 10:
                power_up_collected = True
        elif power_up_picker == 1:
            MAX_BULLETS_RED = 4
            max_bullets_counter = MAX_BULLETS_DURATION  # Start the counter
            power_up_collected = True
        elif power_up_picker == 2:
            VELOCITY_RED = 10
            velocity_counter = VELOCITY_DURATION  # Start the counter
            power_up_collected = True
    if max_bullets_counter > 0:
        max_bullets_counter -= 1
        if max_bullets_counter == 0:
            MAX_BULLETS_BLUE = 3
            MAX_BULLETS_RED = 3

    if velocity_counter > 0:
        velocity_counter -= 1
        if velocity_counter == 0:
            VELOCITY_BLUE = 6
            VELOCITY_RED = 6


def rotate_ships(blue, red):
    global BLUE_SPACESHIP, blue_rotated, RED_SPACESHIP, red_rotated
    if blue.x > red.x and not blue_rotated:
        BLUE_SPACESHIP = pygame.transform.rotate(BLUE_SPACESHIP, 180)
        blue_rotated = True
    if blue.x < red.x and blue_rotated:
        BLUE_SPACESHIP = pygame.transform.rotate(BLUE_SPACESHIP, 180)
        blue_rotated = False
    if red.x < blue.x and not red_rotated:
        RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 180)
        red_rotated = True
    if red.x > blue.x and red_rotated:
        RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 180)
        red_rotated = False


def draw_winner(red_shots, blue_shots, red_hits, blue_hits, red_score, blue_score):
    pygame.mixer.stop()
    GAME_OVER_SOUND.play()
    red_accuracy = 0
    blue_accuracy = 0
    global power_up_collected, winner_text
    power_up_collected = False
    blue_health_image = pygame.image.load(os.path.join('Assets', f'health_{blue_health}.png'))
    blue_health_image = pygame.transform.rotate(
        pygame.transform.scale(blue_health_image, (HEALTH_WIDTH, HEALTH_HEIGHT)), 0)
    WIN.blit(blue_health_image, (10, 10))

    if red_shots != 0:
        red_accuracy = red_hits/red_shots
    if blue_shots != 0:
        blue_accuracy = blue_hits/blue_shots
    red_score = int(red_score*red_accuracy)
    blue_score = int(blue_score*blue_accuracy)

    print(red_accuracy, blue_accuracy)
    print(red_score, blue_score)

    red_health_image = pygame.image.load(os.path.join('Assets', f'health_{red_health}.png'))
    red_health_image = pygame.transform.rotate(pygame.transform.scale(red_health_image, (HEALTH_WIDTH, HEALTH_HEIGHT)),
                                               0)
    WIN.blit(red_health_image, (WIDTH - HEALTH_WIDTH - 10, 10))
    if winner_text == "Blue Wins!":
        WIN.blit(BLUE_WINS_IMAGE,
                 (WIDTH // 2 - BLUE_WINS_IMAGE.get_width() / 2, HEIGHT / 2 - BLUE_WINS_IMAGE.get_height() / 2))
        text_surface = WINNER_FONT.render(str(blue_score), False, (0, 0, 129))
        WIN.blit(text_surface, (700, 167))
        text_surface = WINNER_FONT.render(str(blue_shots), False, (0, 0, 129))
        WIN.blit(text_surface, (790, 247))
        text_surface = WINNER_FONT.render(str(blue_hits), False, (0, 0, 129))
        WIN.blit(text_surface, (780, 327))
        text_surface = WINNER_FONT.render(str(blue_shots - blue_hits), False, (0, 0, 129))
        WIN.blit(text_surface, (850, 405))
        blue_accuracy = str(blue_accuracy*100 )[:4] + "%"
        text_surface = WINNER_FONT.render(blue_accuracy, False, (0, 0, 129))
        WIN.blit(text_surface, (822, 486))
    elif winner_text == "Red Wins!":
        WIN.blit(RED_WINS_IMAGE,(WIDTH // 2 - RED_WINS_IMAGE.get_width() / 2, HEIGHT / 2 - RED_WINS_IMAGE.get_height() / 2))
        text_surface = WINNER_FONT.render(str(red_score), False, (129, 0, 0))
        WIN.blit(text_surface, (700, 167))
        text_surface = WINNER_FONT.render(str(red_shots), False, (129, 0, 0))
        WIN.blit(text_surface, (790, 247))
        text_surface = WINNER_FONT.render(str(red_hits), False, (129, 0, 0))
        WIN.blit(text_surface, (780, 327))
        text_surface = WINNER_FONT.render(str(red_shots - red_hits), False, (129, 0, 0))
        WIN.blit(text_surface, (850, 405))
        red_accuracy = str(red_accuracy*100 )[:4] + "%"
        text_surface = WINNER_FONT.render(red_accuracy, False, (129, 0, 0))
        WIN.blit(text_surface, (822, 486))

    pygame.display.update()
    pygame.time.delay(5000)
    red_accuracy = 0
    blue_accuracy = 0
    winner_text = ""


def main():
    # Initialize game variables
    red = pygame.Rect(1100, 500, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    blue = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    debris = pygame.Rect(WIDTH / 2, 0, 150, 100)
    power_up_location = pygame.Rect(WIDTH//2, HEIGHT//2, POWER_UP_WIDTH, POWER_UP_HEIGHT)
    red_score = 0
    blue_score = 0
    red_shots = 0
    blue_shots = 0
    red_hits = 0
    blue_hits = 0

    red_bullets = []
    blue_bullets = []

    global red_health, blue_health, power_up_collected, start_ticks, power_up_picker, winner_text

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(blue_bullets) < MAX_BULLETS_BLUE:
                    bullet = pygame.Rect(blue.x + blue.width, blue.y + blue.height // 2 - 2, 45, 5)
                    blue_bullets.append(bullet)
                    blue_shots += 1
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS_RED:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 45, 5)
                    red_bullets.append(bullet)
                    red_shots += 1
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                blue_hits += 1
                blue_score += 50
                red_score += 20
                BULLET_HIT_SOUND.play()

            if event.type == BLUE_HIT:
                blue_health -= 1
                red_hits += 1
                red_score += 50
                blue_score += 20
                BULLET_HIT_SOUND.play()

        if power_up_collected:
            power_up_location = power_up_location = pygame.Rect(2000, 2000, POWER_UP_WIDTH, POWER_UP_HEIGHT)
        if power_up_collected and pygame.time.get_ticks() - start_ticks >= 15000:
            power_up_location = pygame.Rect(random.randint(WIDTH//2 - WIDTH//6, WIDTH//2 + WIDTH//6),
                                            random.randint(0, HEIGHT - POWER_UP_HEIGHT), POWER_UP_WIDTH,
                                            POWER_UP_HEIGHT)
            power_up_picker = random.randint(0, 2)
            power_up_collected = False
            start_ticks = pygame.time.get_ticks()
        winner_text = ""
        if red_health <= 0:
            winner_text = "Blue Wins!"
        if blue_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(red_shots, blue_shots, red_hits, blue_hits, red_score, blue_score)
            # Reset game variables
            red = pygame.Rect(1100, 500, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
            blue = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
            debris = pygame.Rect(WIDTH / 2, 0, 150, 100)
            power_up_location = pygame.Rect(WIDTH//2, HEIGHT//2, POWER_UP_WIDTH, POWER_UP_HEIGHT)
            red_bullets = []
            blue_bullets = []
            red_health = 10
            blue_health = 10
            power_up_collected = False
            start_ticks = pygame.time.get_ticks()
            red_score = 0
            blue_score = 0
            red_shots = 0
            blue_shots = 0
            red_hits = 0
            blue_hits = 0
            winner_text = ""

        print(red_bullets, blue_bullets)
        keys_pressed = pygame.key.get_pressed()
        blue_handle_movement(keys_pressed, blue, debris)
        red_handle_movement(keys_pressed, red, debris)
        rotate_ships(blue, red)
        handle_power_ups(red, blue, power_up_location)
        handle_bullets(blue_bullets, red_bullets, blue, red, debris)
        draw_window(red, blue, red_bullets, blue_bullets, debris, power_up_location)
    main()


if __name__ == "__main__":
    main_menu()
    if game_started == True:
        main()
