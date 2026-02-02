import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

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

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add Player class to the updatable and drawable classes
    Player.containers = (updatable, drawable)

    # Instantiate a Player Object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Game Loop
    while True:
        log_state()
         #Check if user has closed the window. Exit the game loop if they do.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        # Update sprites
        updatable.update(dt)

        # Re-render drawable sprites
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # Pause game until 1/60th of a second has passed, and update dt
        dt = clock.tick(60)/1000

        

if __name__ == "__main__":
    main()