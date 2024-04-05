import pygame, os, random, math
import pygame.gfxdraw
pygame.init()
pygame.mixer.init()

width, height = 1600, 900

WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Top Down Last Stand")

clock = pygame.time.Clock()

red = (255, 0, 0)

player_bullets = []
enemies = []
bullet_speed = 15
enemy_speed = 1

ground = pygame.image.load(os.path.join('Assets', 'ground.png'))
player_image_orig = pygame.image.load(os.path.join('Assets', 'player.png'))
cursor_image = pygame.image.load(os.path.join('Assets', 'target.png'))
line_image_orig = pygame.image.load(os.path.join('Assets', 'line.png'))
bullet_image = pygame.image.load(os.path.join('Assets', 'bullet.png'))
player_shoot_image_orig = pygame.image.load(os.path.join('Assets', 'player_shoot.png'))
enemy_image = pygame.image.load(os.path.join('Assets', 'enemy.png'))

shot_sound = pygame.mixer.Sound(os.path.join('Sounds', 'shot.mp3'))
step_sound_1 = pygame.mixer.Sound(os.path.join('Sounds', 'step_1.mp3'))
step_sound_2 = pygame.mixer.Sound(os.path.join('Sounds', 'step_2.mp3'))


pygame.mouse.set_visible(False)
cursor_imgage_rect = cursor_image.get_rect()

class Bullet():
    def __init__(self, player_rect, player_angle, bullet_image_path):
        spawn_offset_x = 10  
        spawn_offset_y = 0   
        spawn_x = player_rect.centerx + spawn_offset_x * math.cos(math.radians(player_angle))
        spawn_y = player_rect.centery + spawn_offset_y * math.sin(math.radians(player_angle))
        self.rect = pygame.Rect(spawn_x, spawn_y, 10, 5)
        self.dx = math.cos(math.radians(player_angle)) * bullet_speed
        self.dy = math.sin(math.radians(player_angle)) * bullet_speed
        self.player_angle = player_angle
        self.bullet_image = pygame.image.load(os.path.join('Assets', 'bullet.png'))  
        self.bullet_image = pygame.transform.scale(self.bullet_image, (10, 5))

    def move(self):
        self.rect.x += int(self.dx)
        self.rect.y -= int(self.dy)
        if self.rect.x > width or self.rect.x < 0 or self.rect.y > height or self.rect.y < 0:
            del(player_bullets[0])

    def draw_bullet(self):
        rotated_bullet = pygame.transform.rotate(self.bullet_image, self.player_angle)
        rotated_bullet_rect = rotated_bullet.get_rect(center=self.rect.center)

        WIN.blit(rotated_bullet, rotated_bullet_rect.topleft)

class Enemy():
    def __init__(self, enemy_angle):
        self.spawn_x = random.randint(0, width)
        if self.spawn_x in [0, 1600]:
            self.pawn_y = random.randint(0, height)
        else:
            self.spawn_y = random.choice([0, 900])
        self.rect = enemy_image.get_rect()
        self.enemy_angle = enemy_angle
        self.enemy_image = pygame.image.load(os.path.join('Assets', 'enemy.png'))
        self.dx = math.cos(math.radians(enemy_angle)) * enemy_speed
        self.dy = math.sin(math.radians(enemy_angle)) * enemy_speed
        self.health = 6
    def spawn_enemy(self):
        rotated_enemy = pygame.transform.rotate(self.enemy_image, self.enemy_angle)
        rotated_enemy_rect = rotated_enemy.get_rect(center=self.rect.center)

        WIN.blit(rotated_enemy, rotated_enemy_rect)

    def move_enemy(self, player_x, player_y, wall_1, wall_2, wall_3, wall_4):
        # Calculate the angle between the enemy and the player
        dx = player_x - self.rect.x
        dy = player_y - self.rect.y
        self.enemy_angle = math.degrees(math.atan2(-dy, dx)) % 360

        # Rotate the enemy image
        rotated_enemy = pygame.transform.rotate(self.enemy_image, self.enemy_angle)
        rotated_enemy_rect = rotated_enemy.get_rect(center=self.rect.center)

        WIN.blit(rotated_enemy, rotated_enemy_rect)

        # Move the enemy
        if self.rect.x > player_x and not self.rect.colliderect(wall_1) and not self.rect.colliderect(wall_2) and not self.rect.colliderect(wall_3) and not self.rect.colliderect(wall_4):
            self.rect.x -= enemy_speed
        elif self.rect.x < player_y and not self.rect.colliderect(wall_1) and not self.rect.colliderect(wall_2) and not self.rect.colliderect(wall_3) and not self.rect.colliderect(wall_4):
            self.rect.x += enemy_speed
        if self.rect.y > player_y and not self.rect.colliderect(wall_1) and not self.rect.colliderect(wall_2) and not self.rect.colliderect(wall_3) and not self.rect.colliderect(wall_4):
            self.rect.y -= enemy_speed
        elif self.rect.y < player_y and not self.rect.colliderect(wall_1) and not self.rect.colliderect(wall_2) and not self.rect.colliderect(wall_3) and not self.rect.colliderect(wall_4):
            self.rect.y += enemy_speed


def rotate(image, angle, pos):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center = pos)
    return rotated_image, rotated_rect


def main():
    player_x = width/2
    player_y = height/2 - 70
    playing = True
    player_image = player_image_orig.copy()
    player_shoot_image = player_shoot_image_orig.copy()
    wall_1 = pygame.Rect(670, 330, 280, 5)
    wall_2 = pygame.Rect(670, 545, 280, 5)
    wall_3 = pygame.Rect(680, 335, 5, 210)
    wall_4 = pygame.Rect(940, 335, 5, 210)
    step_channel = pygame.mixer.Channel(0)

    while playing:

        WIN.blit(ground, (0, 0))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - player_x, mouse_y - player_y
        player_angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        enemy_angle = (180/math.pi) * -math.atan2(player_x, player_y) * 10
        print(enemy_angle)
        player_image, player_rect = rotate(player_image_orig, player_angle, (player_x, player_y))
        player_shoot_image, player_rect = rotate(player_shoot_image_orig, player_angle, (player_x, player_y))
        WIN.blit(player_image, player_rect.topleft)
        WIN.blit(cursor_image, (mouse_x - 7.5, mouse_y - 7.5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if len(player_bullets) < 3:
                        shot_sound.play()
                        bullet = Bullet(player_rect, player_angle, bullet_image)
                        WIN.blit(player_shoot_image, player_rect.topleft)
                        player_bullets.append(bullet)
                        print(mouse_x, mouse_y)

        key_pressed  = pygame.key.get_pressed()
        if key_pressed[pygame.K_w] and not player_rect.colliderect(wall_1) and not player_rect.colliderect(wall_2) and not player_rect.colliderect(wall_3) and not player_rect.colliderect(wall_4):
            player_y -= player_speed
            if not step_channel.get_busy():  
                step_channel.play(step_sound_1)
        if key_pressed[pygame.K_s] and not player_rect.colliderect(wall_1) and not player_rect.colliderect(wall_2) and not player_rect.colliderect(wall_3) and not player_rect.colliderect(wall_4):
            player_y += player_speed
            if not step_channel.get_busy():  
                step_channel.play(step_sound_2)
        if key_pressed[pygame.K_a] and not player_rect.colliderect(wall_1) and not player_rect.colliderect(wall_2) and not player_rect.colliderect(wall_3) and not player_rect.colliderect(wall_4):
            player_x -= player_speed
            if not step_channel.get_busy(): 
                step_channel.play(step_sound_1)
        if key_pressed[pygame.K_d] and not player_rect.colliderect(wall_1) and not player_rect.colliderect(wall_2) and not player_rect.colliderect(wall_3) and not player_rect.colliderect(wall_4):
            player_x += player_speed
            if not step_channel.get_busy():  
                step_channel.play(step_sound_2)
        if key_pressed[pygame.K_LSHIFT]:
            player_speed = 2.75
        else: 
            player_speed = 1.75
        

        if player_rect.colliderect(wall_1):
            player_y += 1
        if player_rect.colliderect(wall_2):
            player_y -= 1
        if player_rect.colliderect(wall_3):
            player_x += 1
        if player_rect.colliderect(wall_4):
            player_x -= 1

        for bullet in player_bullets:
            bullet.move()
            bullet.draw_bullet()
        
        if len(enemies) < 1:
            enemy = Enemy(player_angle)
            enemies.append(enemy)
        for enemy in enemies:
            enemy.spawn_enemy()
            enemy.move_enemy(player_x, player_y, wall_1, wall_2, wall_3, wall_4)

        pygame.display.update()
        clock.tick(60)
        
    main()

main()
