import pygame, random

pygame.init()

width, height = 640, 480

WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake 6.0")

red, green, black = (255, 0, 0), (0, 255, 0), (0, 0, 0)

clock = pygame.time.Clock()

snake_size, snake_speed = 10, 15

lose_font, score_font = pygame.font.SysFont('ubuntu', 30), pygame.font.SysFont('ubuntu', 25)

def draw_score(score):
    score_message = score_font.render(f"Score: {score}", False, green)
    WIN.blit(score_message, [0,0])

def draw_snake(snake_pixels, snake_size):
    for pixel in snake_pixels:
        pygame.draw.rect(WIN, green, [pixel[0], pixel[1], snake_size, snake_size])

def main():
    playing = True
    game_over = False

    x_speed, y_speed = 0, 0

    x, y = width / 2, height / 2

    food_x = round(random.randrange(0 + snake_size, width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0 + snake_size, height - snake_size) / 10.0) * 10.0

    snake_length = 1
    snake_pixels = []

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and not x_speed == snake_size:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_d and not x_speed == -snake_size:
                    x_speed = snake_size
                    y_speed = 0 
                if event.key == pygame.K_w and not y_speed == snake_size:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_s and not y_speed == -snake_size:
                    x_speed = 0
                    y_speed = snake_size
            if event.type == pygame.QUIT:
                pygame.quit()
        x += x_speed
        y += y_speed

        WIN.fill(black)

        pygame.draw.rect(WIN, red, [food_x, food_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del(snake_pixels[0])

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                playing = False
                game_over = True


        if x == food_x and y == food_y:
            snake_length += 1
            food_x = round(random.randrange(0 + snake_size, width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0 + snake_size, height - snake_size) / 10.0) * 10.0

        if x > width or x < 0 or y < 0 or y > height:
            game_over = True
            playing = False
        
        draw_score(snake_length - 1)
        draw_snake(snake_pixels, snake_size)

        clock.tick(snake_speed)

        pygame.display.update()
    while game_over:
        WIN.fill(black)
        lose_message = lose_font.render("Game Over!", False, green)
        WIN.blit(lose_message, (width/3, height / 3))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    playing = True
                    game_over = False
            if event.type == pygame.QUIT:
                pygame.quit()
    main()
main()