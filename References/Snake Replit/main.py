import pygame
from snake import *
from food import Food


Black = [0, 0, 0]
Red = [255, 0, 0]
# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
baseDifficulty = 10
difficulty = baseDifficulty

score = 0
pygame.init()
bounds = (480, 720)
screen_size = (480, 720)
window = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Snake Byte")
snake_icon = pygame.image.load("snake_icon.png")
pygame.display.set_icon(snake_icon)

# Initializes inits and loads sounds onto game
pygame.init()
pygame.mixer.init(44100,-16,1, 1024)
pygame.mixer.set_num_channels(5)

snake_move = pygame.mixer.Sound('../../sounds/snake_move.wav')
pickup_food = pygame.mixer.Sound('../../sounds/pickup_fruit_alt.wav')
snake_death = pygame.mixer.Sound('../../sounds/snake_die.wav')
music = pygame.mixer.Sound('../../sounds/snakebite.mp3')
gameover_amb = pygame.mixer.Sound('../../sounds/gameover_ambience.mp3')


fps_controller = pygame.time.Clock()

block_size = 10
snake = Snake(block_size, bounds)
food = Food(block_size, bounds)
font = pygame.font.SysFont('PixelOperator', 32)
font_small = pygame.font.SysFont('PixelOperator', 18)
font_smaller = pygame.font.SysFont('PixelOperator', 15)
game_active = True
snake_direction = 'RIGHT'
pygame.mixer.Channel(1).play(music, 1)


def game_over():
    global game_active, score, difficulty
    snake_gameover = pygame.image.load('snake_die.png')
    game_over_surface = font.render('Game Over!', True, Black)
    game_over_surface_2 = font_small.render(f'Score: {score}', True, Black)
    game_over_surface_3 = font_small.render('Press R to restart..', True, Black)

    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_size[0] / 2, screen_size[1] / 2)

    game_over_rect_2 = game_over_surface_2.get_rect()
    game_over_rect_2.midtop = (screen_size[0] / 2, screen_size[1] / 2 + 30)

    game_over_rect_3 = game_over_surface_3.get_rect()
    game_over_rect_3.midtop = (screen_size[0] / 2, screen_size[1] / 2 + 50)

    snake_gameover_rect = snake_gameover.get_rect()
    snake_gameover_rect.midtop = (screen_size[0] / 2, screen_size[1] / 2 + 100)

    window.fill(Black)
    window.blit(desk, (0, 0))
    window.blit(bgd_image, (0, 0))
    window.blit(game_over_surface, game_over_rect)
    window.blit(game_over_surface_2, game_over_rect_2)
    window.blit(game_over_surface_3, game_over_rect_3)
    window.blit(snake_gameover, snake_gameover_rect)
    pygame.display.update()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit(0)
    elif keys[pygame.K_r]:
        difficulty = baseDifficulty
        game_active = True
        pygame.mixer.Channel(1).play(music, 1)
        snake.respawn()
        food.respawn()
        score = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.steer(Direction.LEFT)
        if game_active:
            if snake_direction != 'LEFT' and snake_direction != 'RIGHT':
                pygame.mixer.Channel(2).play(snake_move)
            else:
                pass
        snake_direction = 'LEFT'
    elif keys[pygame.K_RIGHT]:
        snake.steer(Direction.RIGHT)
        if game_active:
            if snake_direction != 'LEFT' and snake_direction != 'RIGHT':
                pygame.mixer.Channel(2).play(snake_move)
            else:
                pass
        snake_direction = 'RIGHT'
    elif keys[pygame.K_UP]:
        snake.steer(Direction.UP)
        if game_active:
            if snake_direction != 'UP' and snake_direction != 'DOWN':
                pygame.mixer.Channel(2).play(snake_move)
            else:
                pass
        snake_direction = 'UP'
    elif keys[pygame.K_DOWN]:
        snake.steer(Direction.DOWN)
        if game_active:
            if snake_direction != 'UP' and snake_direction != 'DOWN':
                pygame.mixer.Channel(2).play(snake_move)
            else:
                pass
        snake_direction = 'DOWN'

    if game_active:
        snake.move()
        score, difficulty = snake.check_for_food(food, score, difficulty)

        if snake.check_bounds() == True or snake.check_tail_collision() == True:
            pygame.mixer.Channel(2).play(snake_death)
            pygame.mixer.Channel(1).play(gameover_amb, 1)
            game_active = False

        window.fill(Black)
        desk = pygame.image.load("Desk.png")
        window.blit(desk, (0, 0))
        bgd_image = pygame.image.load("NokiaPhone.png")
        window.blit(bgd_image, (0, 0))
        score_disp = font_smaller.render(f'Score: {score}', True, Black)
        score_rect = score_disp.get_rect()
        score_rect.midtop = (125, 490)
        window.blit(score_disp, score_rect)
        snake.draw(pygame, window)
        food.draw(pygame, window)
        pygame.display.update()
    else:
        game_over()

    fps_controller.tick(difficulty)
