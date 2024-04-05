import pygame
import random

pygame.init()

# colors

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

width, height = 600, 400

WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake 3.0")

clock = pygame.time.Clock()

snake_speed = 15
snake_size = 10

lose_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 20)

def draw_score(score):
   text = score_font.render(f"Score: {score}", True, green)
   WIN.blit(text, [0,0])

def draw_snake(snake_size, snake_pixels):
   for pixel in snake_pixels:
      pygame.draw.rect(WIN, green, [pixel[0], pixel[1], snake_size, snake_size ])

def main():
    playing = True
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while playing:

        while game_close:
            WIN.fill(black)
            game_over_message = lose_font.render("Game over!", True, green)
            WIN.blit(game_over_message, [width / 3, height / 3])
            draw_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        playing = False
                        game_close = True
                        pygame.quit()
                    elif event.key == pygame.K_2:
                        main()
                    elif event.type == pygame.QUIT:
                        playing = False
                        game_close = True
                        pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not x_speed == snake_size or event.key == pygame.K_a and not x_speed == snake_size:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT and not x_speed == -snake_size or event.key == pygame.K_d and not x_speed == -snake_size:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP and not y_speed == snake_size or event.key == pygame.K_w and not y_speed == snake_size:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN and not y_speed == -snake_size or event.key == pygame.K_s and not y_speed == -snake_size:
                    x_speed = 0
                    y_speed = snake_size
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_speed
        y += y_speed

        WIN.fill(black)
        pygame.draw.rect(WIN, red, [food_x, food_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True
        draw_snake(snake_size, snake_pixels)
        draw_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()