import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (252, 186, 3)

WIDTH = 20
HEIGHT = 20

MARGIN = 5

def display(grids):
    grid_width = len(grids[0][0])
    grid_height = len(grids[0])

    pygame.init()

    WINDOW_SIZE = [25 * grid_width, 25 * grid_height]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption("Array Backed Grid")

    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    for grid in grids:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        screen.fill(BLACK)

        for row in range(grid_height):
            for column in range(grid_width):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                elif grid[row][column] == 3:
                    color = RED
                elif grid[row][column] == 2:
                    color = YELLOW
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        clock.tick(3)
        pygame.display.flip()
    pygame.quit()