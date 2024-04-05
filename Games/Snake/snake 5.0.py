import pygame, random

pygame.init()

width, height = 640, 480

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake 5.0")

snake_size = 10
snake_speed = 15

lose_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)

clock = pygame.time.Clock()

def draw_score(score):
    score_message = score_font.render(f"Score: {score}", True, green)
    WIN.blit(score_message, [0, 0])

def draw_snake(snake_pixels, snake_size):
    for pixel in snake_pixels:
        pygame.draw.rect(WIN, green, [pixel[0], pixel[1], snake_size, snake_size])

def main():
    playing = True

    snake_pixels = []
    snake_length = 1

    x_speed, y_speed = 0, 0

    x, y = width / 2, height / 2

    food_x = round(random.randrange(0, width) / 10.0) * 10.0
    food_y = round(random.randrange(0, height)/ 10.0) * 10.0

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_d:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_w:
                    x_speed = 0 
                    y_speed = -snake_size
                if event.key == pygame.K_s:
                    x_speed = 0
                    y_speed = snake_size
        x += x_speed
        y += y_speed

        WIN.fill(black)

        pygame.draw.rect(WIN, red, [food_x, food_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del (snake_pixels[0])

        for pixel in snake_pixels[:-1]:
            if pixel == [x,y]:
                playing = False
        
        if x == food_x and y == food_y:
            snake_length += 1
            food_x = round(random.randrange(0, width) / 10.0) * 10.0
            food_y = round(random.randrange(0, height)/ 10.0) * 10.0 
        draw_score(snake_length - 1)
        draw_snake(snake_pixels, snake_size)

        pygame.display.update()
        clock.tick(snake_speed)

main()
