import pygame # type: ignore
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = (800, 600)  # Window size: 800 pixels wide, 600 pixels tall
CELL_SIZE = 20            # Each cell is 20x20 pixels
GRID_WIDTH = WINDOW_SIZE[0] // CELL_SIZE  # Number of cells horizontally
GRID_HEIGHT = WINDOW_SIZE[1] // CELL_SIZE  # Number of cells vertically
ERASER_SIZE = 30          # Size of the eraser

# Colors
BLUE = (0, 0, 255)       # RGB color for blue
WHITE = (255, 255, 255)  # RGB color for white
BLACK = (0, 0, 0)        # RGB color for black

# Create the window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Canvas Eraser")

# Create the grid - a 2D list where each cell is initially blue
grid = [[BLUE for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Main game loop
running = True
while running:
    # Handle events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get mouse position and state
    mouse_pos = pygame.mouse.get_pos()  # Get current mouse position
    mouse_pressed = pygame.mouse.get_pressed()[0]  # Check if left mouse button is pressed
    
    # If mouse is pressed, erase cells under the eraser
    if mouse_pressed:
        # Calculate which grid cells the eraser covers
        start_x = max(0, (mouse_pos[0] - ERASER_SIZE//2) // CELL_SIZE)
        end_x = min(GRID_WIDTH, (mouse_pos[0] + ERASER_SIZE//2) // CELL_SIZE + 1)
        start_y = max(0, (mouse_pos[1] - ERASER_SIZE//2) // CELL_SIZE)
        end_y = min(GRID_HEIGHT, (mouse_pos[1] + ERASER_SIZE//2) // CELL_SIZE + 1)
        
        # Set all cells under the eraser to white
        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                grid[y][x] = WHITE
    
    # Draw the grid
    screen.fill(BLACK)  # Fill the screen with black background
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            # Draw each cell as a rectangle
            pygame.draw.rect(screen, grid[y][x], 
                           (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Draw the eraser (white outline rectangle that follows the mouse)
    eraser_rect = pygame.Rect(mouse_pos[0] - ERASER_SIZE//2, 
                            mouse_pos[1] - ERASER_SIZE//2, 
                            ERASER_SIZE, ERASER_SIZE)
    pygame.draw.rect(screen, WHITE, eraser_rect, 2)  # Draw eraser outline
    
    # Update the display
    pygame.display.flip()

# Clean up and quit
pygame.quit()
sys.exit()
