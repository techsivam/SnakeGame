import pygame
import random

# Initialize Pygame
pygame.init()

# Set game dimensions
width = 500
height = 500

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set clock
clock = pygame.time.Clock()

# Create window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Create snake and apple
snake_size = 10
apple_size = 10
snake_x = width / 2
snake_y = height / 2
apple_x = round(random.randrange(0, width - apple_size) / 10.0) * 10.0
apple_y = round(random.randrange(0, height - apple_size) / 10.0) * 10.0
x_change = 0
y_change = 0
snake_list = []
snake_length = 1

# Create font
font_style = pygame.font.SysFont(None, 50)

# Create function to display score
def message(msg, color):
    message_text = font_style.render(msg, True, color)
    window.blit(message_text, [width / 6, height / 3])

# Create game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_size
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_size
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_size
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_size
                x_change = 0
                
    # Move snake
    snake_x += x_change
    snake_y += y_change
    
    # Check for boundaries
    if snake_x < 0 or snake_x > width - snake_size or snake_y < 0 or snake_y > height - snake_size:
        game_over = True
    
    # Add snake to list and limit length
    head = []
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)
    if len(snake_list) > snake_length:
        del snake_list[0]
    
    # Check for self-collision
    for segment in snake_list[:-1]:
        if segment == head:
            game_over = True
    
    # Draw snake and apple
    window.fill(black)
    pygame.draw.rect(window, red, [apple_x, apple_y, apple_size, apple_size])
    for segment in snake_list:
        pygame.draw.rect(window, white, [segment[0], segment[1], snake_size, snake_size])
    
    # Check for apple consumption and increase score
    if snake_x == apple_x and snake_y == apple_y:
        apple_x = round(random.randrange(0, width - apple_size) / 10.0) * 10.0
        apple_y = round(random.randrange(0, height - apple_size) / 10.0) * 10.0
        snake_length += 1
    
    # Update screen
    pygame.display.update()
    
    # Set FPS
    clock.tick(15)

# Quit Pygame
pygame.quit()

