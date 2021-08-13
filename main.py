from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Clone")


def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))

        for j in range(COLS + 1):
            pygame.draw.line(win, BLACK, (j * PIXEL_SIZE, 0), (j * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw(win, grid, buttonss):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for buttons in buttonss:
        buttons.draw(win)

    pygame.display.update()


def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttonss = [
    Buttons(10, button_y, 50, 50, BLACK),
    Buttons(70, button_y, 50, 50, RED),
    Buttons(130, button_y, 50, 50, BLUE),
    Buttons(190, button_y, 50, 50, GREEN),
    Buttons(250, button_y, 50, 50, YELLOW),
    Buttons(310, button_y, 50, 50, PURPLE),
    Buttons(370, button_y, 50, 50, CYAN),
    Buttons(440, button_y, 50, 50, WHITE, "Erase"),
    Buttons(510, button_y, 50, 50, WHITE, "Clear")
]

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for buttons in buttonss:
                    if not buttons.clicked(pos):
                        continue

                    drawing_color = buttons.color
                    if buttons.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK

    draw(WIN, grid, buttonss)

pygame.quit()
