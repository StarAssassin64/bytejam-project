import pygame
from snake import *
from food import Food

# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 10

score = 0
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
game_active = True


def game_over():
    my_font = pygame.font.SysFont('Calisto MT', 50)
    game_over_surface = my_font.render('Game Over!', True, Black)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_size[0] / 2, screen_size[1] / 2)
    window.fill(Red)
    window.blit(game_over_surface, game_over_rect)
    pygame.display.update()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit(0)
    elif keys[pygame.K_r]:
        global game_active
        game_active = True
        snake.respawn()
        food.respawn()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
            exit(0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.steer(Direction.LEFT)
    elif keys[pygame.K_RIGHT]:
        snake.steer(Direction.RIGHT)
    elif keys[pygame.K_UP]:
        snake.steer(Direction.UP)
    elif keys[pygame.K_DOWN]:
        snake.steer(Direction.DOWN)

    if game_active:
        snake.move()
        snake.check_for_food(food)

        if snake.check_bounds() == True or snake.check_tail_collision() == True:
            game_active = False

        window.fill(Black)
        bgd_image = pygame.image.load("NokiaPhone.png")
        window.blit(bgd_image, (0, 0))
        snake.draw(pygame, window)
        food.draw(pygame, window)
        pygame.display.update()
    else:
        game_over()

    fps_controller.tick(difficulty)
