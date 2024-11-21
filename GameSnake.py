import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 400, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake com IA")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
snake = [(5, 5)]
direction = (0, 1)
food = (random.randint(0, WIDTH // CELL_SIZE - 1), random.randint(0, HEIGHT // CELL_SIZE - 1))

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def is_safe_move(new_head, snake):
    return (
        0 <= new_head[0] < WIDTH // CELL_SIZE and 
        0 <= new_head[1] < HEIGHT // CELL_SIZE and
        new_head not in snake
    )

def get_ai_direction(snake, food):
    head = snake[0]
    possible_moves = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    if food[0] > head[0]:
        move = (1, 0)
    elif food[0] < head[0]:
        move = (-1, 0)
    elif food[1] > head[1]:
        move = (0, 1)
    else:
        move = (0, -1)

    new_head = (head[0] + move[0], head[1] + move[1])
    if is_safe_move(new_head, snake):
        return move

    for move in possible_moves:
        new_head = (head[0] + move[0], head[1] + move[1])
        if is_safe_move(new_head, snake):
            return move
        
        return(0, 0)
    
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    direction = get_ai_direction(snake, food)

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    if snake[0] == food:
        food = (random.randint(0, WIDTH // CELL_SIZE - 1), random.randint(0, HEIGHT // CELL_SIZE - 1))
    else:
        snake.pop()

    if not is_safe_move(new_head, snake[1:]):
        running = False

    draw_food(food)
    draw_snake(snake)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()

    