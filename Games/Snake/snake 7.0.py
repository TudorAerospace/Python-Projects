import pygame, random

pygame.init()

width, height = 640, 480

WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake 7.0")

red, green, black = (255, 0, 0), (0, 255, 0), (0, 0, 0)

snake_speed, snake_size = 15, 10

clock = pygame.time.Clock()

score_font, lose_font = pygame.font.SysFont('ubuntu', 20), pygame.font.SysFont('ubuntu', 30)

def draw_score(score):
    score_message = score_font.render(f"Score: {score}", True, green)
    WIN.blit(score_message, (0, 0))
        
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(WIN, green, [pixel[0], pixel[1], snake_size, snake_size])

def main():
    playing = True

    snake_pixels = []
    snake_length = 1

    x, y = width / 2, height / 2
    x_speed, y_speed = 0, 0

    food_x = round(random.randrange(0 + snake_size, width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0 + snake_size, height - snake_size) / 10.0) * 10.0

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and not x_speed == snake_size:
                    x_speed = -snake_size
                    y_speed =   0
                if event.key == pygame.K_d and not x_speed == -snake_size:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_w and not y_speed == snake_size:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_s and not y_speed == -snake_size:
                    x_speed = 0
                    y_speed = snake_size
        x += x_speed
        y += y_speed

        WIN.fill(black)

        snake_pixels.append([x, y])

        pygame.draw.circle(WIN, red, (food_x + snake_size / 2, food_y + snake_size / 2), 5)

        if len(snake_pixels) > snake_length:
            del(snake_pixels[0])

        if x > width or x < 0 or y > height or y < 0:
            game_over = True
            playing = False
        
        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                playing = False
                game_over = True

        if x == food_x and y == food_y:
            snake_length += 1
            food_x = round(random.randrange(0 + snake_size, width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0 + snake_size, height - snake_size) / 10.0) * 10.0

        draw_score(snake_length - 1)
        draw_snake(snake_size, snake_pixels)

        pygame.display.update()
        clock.tick(snake_speed)
    while game_over:
        WIN.fill(black)
        lose_message = lose_font.render("Game Over!", True, green)
        WIN.blit(lose_message, (width / 3, height / 3))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    playing = True
                    game_over = False
    if playing == True:
        main()
                    

main()

