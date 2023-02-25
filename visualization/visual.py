import pygame
import time

# Define some colors
BACKGROUND_COLOR = (0, 0, 0)
TILE_COLOR = (0, 120, 255)
BORDER_COLOR = (255, 255, 255)
FONT_COLOR = (255, 255, 255)

# Set the width and height of each tile
TILE_WIDTH = 100
TILE_HEIGHT = 100

# Initialize Pygame
pygame.init()

# Set the size of the screen
size = (TILE_WIDTH * 3, TILE_HEIGHT * 3)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("8 Puzzle Solver")

# Load the font for displaying the numbers on the tiles
font = pygame.font.Font("visualization/fonts/Roboto-Bold.ttf", 60)
def main():
    # Define a function to draw the tiles on the screen
    def draw_tiles(tiles):
        for i in range(3):
            for j in range(3):
                value = tiles[j * 3 + i]
                rect = pygame.Rect(j * TILE_WIDTH, i * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
                pygame.draw.rect(screen, TILE_COLOR, rect)
                pygame.draw.rect(screen, BORDER_COLOR, rect, 2)
                if value != 0:
                    text = font.render(str(value), True, FONT_COLOR)
                    text_rect = text.get_rect(center=rect.center)
                    screen.blit(text, text_rect)

        # Add a glowing border effect to the tiles
        border_rect = pygame.Rect(0, 0, TILE_WIDTH * 3, TILE_HEIGHT * 3)
        border_surface = pygame.Surface((TILE_WIDTH * 3, TILE_HEIGHT * 3), pygame.SRCALPHA)
        pygame.draw.rect(border_surface, (255, 255, 255, 20), border_rect, 50, border_radius=20)
        screen.blit(border_surface, border_rect)

    # Load the node path from the text file
    with open("nodePath.txt") as file:
        node_path = file.readlines()

    # Convert the node path to a list of tile configurations
    tile_configs = []
    for line in node_path:
        tile_configs.append(list(map(int, line.strip().split())))

    # Loop through the tile configurations and draw them on the screen
    for tiles in tile_configs:
        screen.fill(BACKGROUND_COLOR)
        draw_tiles(tiles)
        pygame.display.update()
        time.sleep(1)  # Pause for 1 second before displaying the next tile configuration

    # Wait for the user to close the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

if __name__ == "__main__":
    main()

