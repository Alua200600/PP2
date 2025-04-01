import pygame
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game with Disappearing Food')
clock = pygame.time.Clock()

# Snake block size and initial speed
snake_block = 10
initial_speed = 5

# Fonts for displaying text
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def draw_score_level(score, level):
    """Display score and level."""
    score_text = score_font.render(f"Score: {score}  Level: {level}", True, yellow)
    dis.blit(score_text, [10, 10])

def draw_snake(snake_block, snake_list):
    #raw the snake
    for block in snake_list:
        pygame.draw.rect(dis, black, [block[0], block[1], snake_block, snake_block])

def message(msg, color):
    #Display a message on the screen
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def generate_food(snake_list):
    #Generate food in a position not occupied by the snake
    while True:
        food_size = random.choice([10, 20, 30])  # Random food size
        food_x = random.randrange(30, dis_width - food_size, 10)
        food_y = random.randrange(30, dis_height - food_size, 10)
        if [food_x, food_y] not in snake_list:
            return food_x, food_y, food_size, pygame.time.get_ticks()  # Add time of generation

def gameLoop():
    game_over = False
    game_close = False

    x1, y1 = dis_width // 2, dis_height // 2  # Initial snake position
    x1_change, y1_change = 0, 0

    snake_list = []
    snake_length = 1
    score = 0
    level = 1
    speed = initial_speed

    food_x, food_y, food_size, food_timer = generate_food(snake_list)
    food_lifetime = 10000 # Food disappears after 10 seconds 

    while not game_over:
        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            draw_score_level(score, level)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change, y1_change = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    x1_change, y1_change = snake_block, 0
                elif event.key == pygame.K_UP:
                    y1_change, x1_change = -snake_block, 0
                elif event.key == pygame.K_DOWN:
                    y1_change, x1_change = snake_block, 0

        # Check for wall collision
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Check if food should disappear
        if pygame.time.get_ticks() - food_timer > food_lifetime:
            food_x, food_y, food_size, food_timer = generate_food(snake_list)  # Generate new food

        pygame.draw.rect(dis, green, [food_x, food_y, food_size, food_size])  # Draw food

        # Update the snake
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for self-collision
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        draw_score_level(score, level)
        pygame.display.update()

        # If the snake eats the food
        if food_x <= x1 < food_x + food_size and food_y <= y1 < food_y + food_size:
            food_x, food_y, food_size, food_timer = generate_food(snake_list)  # Generate new food
            snake_length += food_size // 10  # Increase snake length based on food size
            score += food_size // 10

            # Increase level every 3 points
            if score % 3 == 0:
                level += 1
                speed += 2

        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()
