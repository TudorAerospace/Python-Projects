import pygame
import random

pygame.font.init()
pygame.mixer.init()
pygame.init()

WIDTH, HEIGHT = 640, 480
SNAKE_WIDTH, SNAKE_HEIGHT = 10, 10

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

FPS = 60
food_x = 200
food_y = 200
snake_body = []

def draw_window(snake, food):
    WIN.fill(BLACK)
    for part in snake_body:  # Draw each part of the snake body
        pygame.draw.rect(WIN, GREEN, part)
    pygame.draw.circle(WIN, RED, food.center, 5)
    pygame.display.update()



def handle_movement(up, down, left, right, snake):
    if up:
        snake.y -= 2
    elif down:
        snake.y += 2
    elif left:
        snake.x -= 2
    elif right:
        snake.x += 2


def handle_food(snake, food):
    global food_x, food_y, snake_length
    if snake.colliderect(food):
        print("Food!")
        snake_length += 1
        print(snake_length)
        food_x = random.randint(15, WIDTH - 15)
        food_y = random.randint(15, HEIGHT - 15)
        print(food_x, food_y)
        for i in range(6):
            snake_body.append(snake.copy())
        print(len(snake_body))
        return pygame.Rect(food_x, food_y, SNAKE_WIDTH, SNAKE_HEIGHT)
    return food




def main():
    up = False
    down = False
    left = False
    right = False
    snake = pygame.Rect(300, 300, SNAKE_WIDTH, SNAKE_HEIGHT)
    snake_body.append(snake.copy())
    global food_x, food_y, snake_length
    snake_length = 1
    playing = True
    clock = pygame.time.Clock()
    while playing:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            if down:
                pass
            else:
                up = True
                down = False
                left = False
                right = False
        if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            if up:
                pass
            else:
                up = False
                down = True
                left = False
                right = False
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            if right:
                pass
            else:
                up = False
                down = False
                left = True
                right = False
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            if left:
                pass
            else:
                up = False
                down = False
                left = False
                right = True
        if len(snake_body) > snake_length * 6:  # Remove the tail of the snake
            del snake_body[0]
        for i in range(len(snake_body) - 1, 0, -1):  # Move the body to follow the head
            snake_body[i] = snake_body[i - 1].copy()
        if snake_body:
            snake_body[0] = snake.copy()
        food_rect = pygame.Rect(food_x, food_y, SNAKE_WIDTH, SNAKE_HEIGHT)
        handle_movement(up, down, left, right, snake)
        draw_window(snake, food_rect)
        handle_food(snake, food_rect)


if __name__ == "__main__":
    main()