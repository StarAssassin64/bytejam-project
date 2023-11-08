import pygame, sys, time, random

# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 25

# Window size
frame_size_x = 480
frame_size_y = 720

# Error Checker
check_errors = pygame.init()
if check_errors[1] > 0:
    print(f'Error| {check_errors[1]} errors have occurred while initializing the game | Errors')
    sys.exit(2)

pygame.display.set_caption('Snake Byte')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
bgd_image = pygame.image.load("NokiaPhone.png")
game_window.blit(bgd_image, (0, 0))

# Colors (RGB)
# Green color hex - #3fd140
Black = pygame.Color(0, 0, 0, 204) # snake, text
Red = pygame.Color(255, 0, 0, 204) # food

# FPS
fps_controller = pygame.time.Clock()

# Imported game variables
snake_pos = [110, 320]
snake_body = [[110, 320], [110-10, 320], [110-(2*10), 320]]

food_pos = [random.randrange(86, 389), random.randrange(289, 505)]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0


# Game Over
def game_over():
    my_font = pygame.font.SysFont('Calisto MT', 50)
    game_over_surface = my_font.render('Game Over!', True, Black)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/2)
    game_window.fill(Red)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, Black, 'Calisto MT', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont('Calisto MT', 20)
    score_surface = score_font.render('Score : ' + str(score), True, Black)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (125, 490)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()


# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawning food on the screen
    if not food_spawn:
        food_pos = [random.randrange(86, 389), random.randrange(289, 505)]
    food_spawn = True

# GFX
    bgd_image = pygame.image.load("NokiaPhone.png")
    game_window.blit(bgd_image, (0, 0))
    for pos in snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(game_window, Black, pygame.Rect(pos[0], pos[1], 10, 10))

    # Snake food
    pygame.draw.rect(game_window, Red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    # Getting out of bounds
    if snake_pos[0] < 84 or snake_pos[0] > 391:
        game_over()
    if snake_pos[1] < 287 or snake_pos[1] > 507:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, Black, 'Calisto MT', 10)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(difficulty)

if __name__ == '__main__':
    pass
