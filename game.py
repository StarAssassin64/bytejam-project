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

# Colors (RGB)
# Green color hex - #3fd140
Black = pygame.Color(0, 0, 0, 204) # snake, text
Red = pygame.Color(255, 0, 0, 204) # food

# FPS
fps_controller = pygame.time.Clock()






if __name__ == '__main__':
    pass
