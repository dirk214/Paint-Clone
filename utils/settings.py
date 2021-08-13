import pygame

pygame.init()
pygame.font.init()

FPS = 240
WIDTH, HEIGHT = 600, 700
ROWS = COLS = 100
TOOLBAR_HEIGHT = HEIGHT - WIDTH
PIXEL_SIZE = WIDTH // COLS
DRAW_GRID_LINES = True

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BG_COLOR = WHITE


def get_font(size):
    return pygame.font.SysFont("timesnewroman", size)