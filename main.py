import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialise pygame
    pygame.init() 

    # Variables to keep track of time
    clock = pygame.time.Clock()
    dt = 0 # delta time (seconds). Time that has passed since the last frame was drawn.

    # New instance of GUI
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game Loop
    while True:
        log_state()
        for event in pygame.event.get():
            #Check if user has closed the window. Exit the game loop if they do.
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

        # Pause game until 1/60th of a second has passed, and update dt
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()