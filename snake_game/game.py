import pygame as p
import random
import matplotlib.pyplot as plt

# Initialize pygame
p.init()

# Game window dimensions
width = 800
height = 600

# Colors
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)

# Set up display
screen = p.display.set_mode((width, height))
p.display.set_caption("Snake Game")

# Snake and food settings
snake_pos = [100, 50]
snake_body = [[100,50], [90,50], [80,50]]
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1,(height//10)) * 10]
food_spawn = True
direction = "RIGHT"
change_to = direction
score = 0

def game_over():
    p.quit()
    quit()

while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            game_over()
        elif event.type == p.KEYDOWN:
            if event.key == p.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == p.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == p.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == p.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    # Update direction
    if change_to == "UP":
        direction = "UP"
    elif change_to == "DOWN":
        direction = "DOWN"
    elif change_to == "LEFT":
        direction = "LEFT"
    elif change_to == "RIGHT":
        direction = "RIGHT"

    # Move snake position
    if direction == "UP":
        snake_pos[1] -= 10
    elif direction == "DOWN":
        snake_pos[1] += 10
    elif direction == "LEFT":
        snake_pos[0] -= 10
    elif direction == "RIGHT":
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) *10]
    food_spawn = True

    # Game over conditions
    if snake_pos[0] < 0 or snake_pos[0] > (width-10):
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > (height-10):
        game_over()
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    # Draw everything
    # def grid():
    #     for x in range(0, width, 10):
    #         p.draw.line(screen, (255, 255, 255), (x, 0), (x, height))
    #     for y in range(0, height, 10):
    #         p.draw.line(screen, (255,255,255), (0, y),(width, y))
    # screen.fill(black)
    # grid()
    for pos in snake_body:
        p.draw.rect(screen, green, p.Rect(pos[0], pos[1], 10, 10))
    p.draw.rect(screen, red, p.Rect(food_pos[0], food_pos[1], 10, 10))

    # Refresh game screen
    p.display.update()

    # Frame Per Second controller
    p.time.Clock().tick(10)
