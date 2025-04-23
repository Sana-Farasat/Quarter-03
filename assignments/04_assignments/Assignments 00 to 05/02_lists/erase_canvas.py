import pygame

"""
Grid: Ek organized structure ya layout jisme rows aur columns hote hain.

Cell: Grid ka ek individual unit ya part hota hai, jo ek small rectangle ya square hota hai.
"""
pygame.init()  # To start pygame

# For making canvas screen
CANVA_WIDTH = 400
CANVA_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

BLUE = (0, 0, 255)  # Cells will be blue
WHITE = (255, 255, 255)  # Background will be white
PINK = (255, 182, 193)  # Eraser will be pink

# To display canvas screen
screen = pygame.display.set_mode((CANVA_WIDTH, CANVA_HEIGHT))

# To show prompt on window
pygame.display.set_caption("Enter effect in pygame")

# Initialize empty grid
grid = []

# Now we will run loop so that we could know how many rows and columns would be on it
for row in range(0, CANVA_HEIGHT, CELL_SIZE):
    for col in range(0, CANVA_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)  # Fixed row and column values
        grid.append(rect)

# Now making eraser
eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)

# Create clock object for controlling frame rate
clock = pygame.time.Clock()

# We don't know when our program execution would be stopped, so we will use while loop
running = True
while running:
    # Fill screen with white background
    screen.fill(WHITE)

    # Draw grid cells
    for rect in grid:
        pygame.draw.rect(screen, BLUE, rect)

    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Move the eraser to the mouse position (centered)
    eraser.topleft = (mouse_x - ERASER_SIZE // 2, mouse_y - ERASER_SIZE // 2)

    # Initialize new grid and remove cells that the eraser overlaps with
    new_grid = []
    for rect in grid:
        if not eraser.colliderect(rect):
            new_grid.append(rect)
    grid = new_grid

    # Draw the eraser on the screen
    pygame.draw.rect(screen, PINK, eraser)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the screen
    pygame.display.flip()

    # Control the frame rate to 60 frames per second
    clock.tick(60)

pygame.quit()
