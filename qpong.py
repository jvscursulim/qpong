import pygame
from assets import WINDOW_WIDTH, WINDOW_HEIGHT, FPS

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("QPong")
clock = pygame.time.Clock()

def main():

    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        # set game framerate
        clock.tick(FPS)

if __name__ == "__main__":
    main()


