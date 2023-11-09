import pygame
from snake import *
from food import Food

pygame.init()
bounds = (480, 720)
screen_size = (480, 720)
window = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Snake")

block_size = 10
snake = Snake(block_size, bounds)
food = Food(block_size, bounds)
font = pygame.font.SysFont('Small Font Regular', 25)

run = True
while run:
    pygame.time.delay(100)

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
        pygame.time.delay(1000)
        snake.respawn()
        food.respawn()

    window.fill(0)
    bgd_image = pygame.image.load("NokiaPhone.png")
    window.blit(bgd_image, (0, 0))
    snake.draw(pygame, window)
    food.draw(pygame, window)
    pygame.display.update()
