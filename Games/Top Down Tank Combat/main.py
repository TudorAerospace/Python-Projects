import pygame, os, math

width, height = 1600, 900

pygame.init()
pygame.mixer.init()
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Top Down Tank Combat")

scale_down = 10
player_speed = 5

clock = pygame.time.Clock()

ground = pygame.image.load(os.path.join('Assets', 'ground.png'))
ground = pygame.transform.scale(ground, (width, height))
player_turret_orig = pygame.image.load(os.path.join('Assets', 'player_turret.png'))
player_turret_orig = pygame.transform.scale(player_turret_orig, (width//scale_down + 200, height//scale_down))

player_hull= pygame.image.load(os.path.join('Assets', 'player_hull.png'))  # Load the original image
player_hull = pygame.transform.scale(player_hull, (width//scale_down - 50, height//scale_down + 120))

def draw_player(player_x, player_y, player_hull, player_turret):
    WIN.blit(player_hull, (player_x, player_y))
    WIN.blit(player_turret, (player_x + player_hull.get_width()//2 - player_turret.get_width()//2 - 3, player_y + player_hull.get_height()//2 - player_turret.get_height()//2))  # Increase the y-offset
    

def main():
    player_x, player_y = 70, height / 2
    playing = True

    player_turret = player_turret_orig.copy()  # Copy the original turret image
    while playing:
        WIN.blit(ground, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w] and player_y > 10:
            player_y -= player_speed
        if key_pressed[pygame.K_s] and player_y < height - 220:
            player_y += player_speed

        mouse_x, mouse_y = pygame.mouse.get_pos()  # Get the mouse cursor position
        rel_x, rel_y = mouse_x - player_x, mouse_y - player_y  # Get the relative position of the mouse to the player
        turret_angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        player_turret = pygame.transform.rotate(player_turret_orig, turret_angle)  # Rotate the turret image
        draw_player(player_x, player_y, player_hull, player_turret)  # Use the x and y of hull_rect for drawing
        pygame.display.update()

        clock.tick(60)
    main()

main()
