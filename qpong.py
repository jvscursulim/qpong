import pygame
from assets import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, FIELD_HEIGHT
from assets import CircuitGrid, ui

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("QPong")
clock = pygame.time.Clock()

def main():

    # initialize game
    circuit_grid = CircuitGrid(xpos=5, ypos=FIELD_HEIGHT)

    exit = False
    while not exit:
        # update game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)

        # draw game
        circuit_grid.draw(screen)
        ui.draw_statevector_grid(screen)
        pygame.display.flip()

        # set game framerate
        clock.tick(FPS)

if __name__ == "__main__":
    main()


