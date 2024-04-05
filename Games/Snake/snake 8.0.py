import pygame

pygame.init()

width, height = 800, 600

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

score_font = pygame.font.SysFont('ubuntu', 25)

WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake 8.0")

snake_speed, snake_size = 15, 10

def draw_score(score):
    score_message = score_font.render(f"Score: {score}", True, green)
    WIN.blit(score_message, (0, 0))

def draw_snake(snake_pixels):
    for pixel in snake_pixels:
        
