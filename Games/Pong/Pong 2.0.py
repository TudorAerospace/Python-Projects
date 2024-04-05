import pygame, random

pygame.init()

width, height =  800, 580

WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong 2.0")

clock = pygame.time.Clock()
#colours

score_font = pygame.font.SysFont('ubuntu', 60)

white = (200, 200, 200)
red = (255, 200, 200)
green = (200, 255, 200)
blue = (200, 200, 255)
black = (0, 0, 0)

ball_speed = 12
ball_size = 25
num = 0

paddle_width, paddle_height = 20, 100
paddle_speed = 15

def draw_window():
    WIN.fill(black)
    global up_wall, down_wall
    pygame.draw.rect(WIN, white, [0, 0, width, 20])
    up_wall = pygame.Rect((0, 0), (width, 20))
    pygame.draw.rect(WIN, white, [0, height - 20, width, 20])
    down_wall = pygame.Rect((0, height - 20), (width, 20))
    for i in range(28):
        if i % 2 == 1:
            pygame.draw.rect(WIN, white, [width/2 - 10, i * 20, 20, 20])
        else:
            pass


def draw_score(score_left, score_right):
    score_message_left = score_font.render(str(score_left), True, white)
    score_message_right = score_font.render(str(score_right), True, white)
    WIN.blit(score_message_right, (width/2 - 60, 20))
    WIN.blit(score_message_left, (width/2 + 25, 20))

def draw_player(player_x, player_y):
    global player
    player = pygame.Rect((player_x, player_y), (paddle_width, paddle_height))
    pygame.draw.rect(WIN, blue, [player_x, player_y, paddle_width, paddle_height])

def draw_bot(bot_x, bot_y):
    global bot
    bot = pygame.Rect((bot_x, bot_y), (paddle_width, paddle_height))
    pygame.draw.rect(WIN, green, [bot_x, bot_y, paddle_width, paddle_height])

def draw_ball(ball_x, ball_y):
    global ball
    ball = pygame.Rect((ball_x, ball_y), (ball_size, ball_size))
    pygame.draw.rect(WIN, red, [ball_x, ball_y, ball_size, ball_size] )
    
def ai(bot_y, ball_y, num2):
    if bot_y > 20 or bot_y < height - 2 - paddle_height:
        if num2 < 5000:
            if bot_y + paddle_height/2 > ball_y:
                bot_y -= paddle_speed/2
            elif bot_y + paddle_height/2 < ball_y:
                bot_y += paddle_speed/2
        elif num2 > 5000:
            if bot_y + paddle_height/2 > ball_y:
                bot_y -= paddle_speed/2.5
            elif bot_y + paddle_height/2 < ball_y:
                bot_y += paddle_speed/2.5


                    
    return bot_y
def main():
    stuck_time = 0
    playing = True
    num2 = 1
    player_x, player_y = width - 50 - paddle_width, height/2 - paddle_height/2
    bot_x, bot_y = 50, height/2 - paddle_height/2
    ball_x, ball_y = width/2 - ball_size/2, height/2 - ball_size/2
    ball_x_speed, ball_y_speed = ball_speed, 0
    score_left, score_right = 0, 0
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_o] and player_y > 20:
            player_y -= paddle_speed
        if key_pressed[pygame.K_k] and player_y < height - 2 - paddle_height:
            player_y += paddle_speed
        if key_pressed[pygame.K_e] and bot_y > 20:
            bot_y -= paddle_speed
        if key_pressed[pygame.K_d] and bot_y < height - 2 - paddle_height:
            bot_y += paddle_speed
        draw_window()
        draw_score(score_left, score_right)
        draw_player(player_x, player_y)
        draw_bot(bot_x, bot_y)
        draw_ball(ball_x, ball_y)
        bot_y = ai(bot_y, ball_y, num2)
        pygame.display.update()
        ball_x += ball_x_speed
        ball_y += ball_y_speed
        if ball_x < 100 or ball_x > width - 100:
            if stuck_time == 0:  # Start the timer if it's not already started
                stuck_time = pygame.time.get_ticks()
            else:
                # Calculate the time difference
                time_diff = pygame.time.get_ticks() - stuck_time
                if time_diff > 3000 and ball_x < 100: 
                    ball_x += 100
                    stuck_time = 0  # Reset the timer
                elif time_diff > 1000 and ball_x > width - 100:
                    ball_x -= 100
                    stuck_time = 0  # Reset the timer
        else:
            stuck_time = 0
        if ball.colliderect(player) or ball.colliderect(bot):
            print(ball_y_speed)
            if ball_x_speed > 0:
                num2 = random.randint(0, 10000)
                ball_x -= 35
                num = random.randint(0, 1)
                if num == 0: 
                    ball_y_speed = random.randint(1, 10)
                elif num == 1:
                    ball_y_speed = random.randint(-10, 0)
            else:
                num2 = random.randint(0, 10000)
                ball_x += 35
                num = random.randint(0, 1)
                if num == 0: 
                    ball_y_speed = random.randint(1, 10)
                elif num == 1:
                    ball_y_speed = random.randint(-10, 0)
            ball_x_speed = -ball_x_speed
            ball_y_speed = -ball_y_speed
            print(ball_y_speed)
        if ball.colliderect(up_wall) or ball.colliderect(down_wall):
            ball_y_speed = -ball_y_speed
            if ball_y < height/2:
                ball_y += 20
            else:
                ball_y -= 20
        if ball_x < 0:
            num2 = random.randint(0, 10000)
            score_left += 1
            ball_x = width/2 - ball_size/2
            ball_y = height/2 - ball_size/2
            ball_y_speed = 0
            player_x, player_y = width - 50 - paddle_width, height/2 - paddle_height/2
            bot_x, bot_y = 50, height/2 - paddle_height/2

        elif ball_x > width:
            num2 = random.randint(0, 10000)
            score_right += 1
            ball_x = width/2 - ball_size/2
            ball_y = height/2 - ball_size/2
            ball_y_speed = 0
            player_x, player_y = width - 50 - paddle_width, height/2 - paddle_height/2
            bot_x, bot_y = 50, height/2 - paddle_height/2

        
        clock.tick(60)

main()