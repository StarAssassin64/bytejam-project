import pygame
from snake import *
from food import Food

# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 15


pygame.init()
bounds = (480, 720)
screen_size = (480, 720)
window = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Snake")

fps_controller = pygame.time.Clock()

block_size = 10
snake = Snake(block_size, bounds)
food = Food(block_size, bounds)
font = pygame.font.SysFont('Small Font Regular', 25)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.steer(Direction.LEFT)
    elif keys[pygame.K_RIGHT]:
        snake.steer(Direction.RIGHT)
    elif keys[pygame.K_UP]:
        snake.steer(Direction.UP)
    elif keys[pygame.K_DOWN]:
        snake.steer(Direction.DOWN)

    snake.move()
    snake.check_for_food(food)

    if snake.check_bounds() == True or snake.check_tail_collision() == True:
        text = font.render('Game Over', True, (255, 255, 255))
        window.blit(text, (20, 120))
        pygame.display.update()
        snake.respawn()
        food.respawn()

    window.fill(0)
    bgd_image = pygame.image.load("NokiaPhone.png")
    window.blit(bgd_image, (0, 0))
    snake.draw(pygame, window)
    food.draw(pygame, window)
    pygame.display.update()
    fps_controller.tick(difficulty)
