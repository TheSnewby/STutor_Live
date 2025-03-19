import pygame
import sys
import time

# TOWERS OF HANOI
# Produced by Claude & Gemini

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900  # Reduced to fit within 1920x1080 including window borders
BACKGROUND = (240, 240, 240)
TEXT_COLOR = (0, 0, 0)
ROD_COLOR = (139, 69, 19)  # Brown
DISC_COLORS = [
    (52, 152, 219),  # Blue
    (155, 89, 182),  # Purple
    (52, 73, 94),  # Dark Blue
    (22, 160, 133),  # Green
    (241, 196, 15),  # Yellow
    (230, 126, 34),  # Orange
    (231, 76, 60),  # Red
    (149, 165, 166)  # Gray
]

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower of Hanoi - Stack Visualization")
font = pygame.font.SysFont('Arial', 28)  # Further reduced font size
move_count = 0

def draw_rod(x, label):
    rod_width = 14
    rod_height = 400
    base_width = 260
    base_height = 25

    # Draw base
    pygame.draw.rect(screen, ROD_COLOR, (x - base_width // 2, SCREEN_HEIGHT - 180, base_width, base_height))

    # Draw rod
    pygame.draw.rect(screen, ROD_COLOR, (x - rod_width // 2, SCREEN_HEIGHT - 180 - rod_height, rod_width, rod_height))

    # Draw label
    label_text = font.render(label, True, TEXT_COLOR)
    screen.blit(label_text, (x - label_text.get_width() // 2, SCREEN_HEIGHT - 140))

def draw_disc(rod_x, disc_width, disc_height, disc_position, color):
    y = SCREEN_HEIGHT - 180 - (disc_position + 1) * disc_height
    pygame.draw.rect(screen, color, (rod_x - disc_width // 2, y, disc_width, disc_height), 0, 15)
    pygame.draw.rect(screen, (50, 50, 50), (rod_x - disc_width // 2, y, disc_width, disc_height), 2, 15)

def draw_towers(towers, n_discs):
    # Clear screen
    screen.fill(BACKGROUND)

    # Draw move counter
    move_text = font.render(f"Moves: {move_count}", True, TEXT_COLOR)
    screen.blit(move_text, (SCREEN_WIDTH - move_text.get_width() - 20, 20))

    # Draw title
    title = font.render("Tower of Hanoi - Stack Visualization", True, TEXT_COLOR)
    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 20))

    # Draw info
    info = font.render(f"Number of discs: {n_discs}", True, TEXT_COLOR)
    screen.blit(info, (20, 20))

    # Calculate dimensions
    rod_positions = [SCREEN_WIDTH // 4, SCREEN_WIDTH // 2, 3 * SCREEN_WIDTH // 4]
    max_disc_width = 240
    disc_height = 40

    # Draw rods
    for i, x in enumerate(rod_positions):
        draw_rod(x, chr(65 + i))  # A, B, C

    # Draw discs
    for rod_idx, rod in enumerate(towers):
        for disc_pos, disc_size in enumerate(rod):
            disc_width = max_disc_width - (n_discs - disc_size) * 25
            draw_disc(rod_positions[rod_idx], disc_width, disc_height, disc_pos, DISC_COLORS[disc_size % len(DISC_COLORS)])

def solve_tower_of_hanoi(n, source, auxiliary, target, towers, n_discs):
    global move_count

    if n == 1:
        # Move a single disc from source to target
        disc = towers[source].pop()
        towers[target].append(disc)
        move_count += 1

        # Visualize
        draw_towers(towers, n_discs)
        pygame.display.flip()
        time.sleep(0.5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        return

    # Move n-1 discs from source to auxiliary using target as intermediate
    solve_tower_of_hanoi(n - 1, source, target, auxiliary, towers, n_discs)

    # Move remaining disc from source to target
    disc = towers[source].pop()
    towers[target].append(disc)
    move_count += 1

    # Visualize
    draw_towers(towers, n_discs)
    pygame.display.flip()
    time.sleep(0.5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move n-1 discs from auxiliary to target using source as intermediate
    solve_tower_of_hanoi(n - 1, auxiliary, source, target, towers, n_discs)

def main():
    global move_count

    n_discs = 6  # Number of discs

    # Initialize towers
    towers = [list(range(n_discs, 0, -1)), [], []]  # [source, auxiliary, target]

    # Initial visualization
    draw_towers(towers, n_discs)
    pygame.display.flip()
    time.sleep(3)

    # Solve
    move_count = 0
    solve_tower_of_hanoi(n_discs, 0, 1, 2, towers, n_discs)

    # Wait for user to close window
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()