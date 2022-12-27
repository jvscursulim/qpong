import pygame
from assets import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, FIELD_HEIGHT, WIDTH_UNIT, BLACK
from assets import CircuitGrid, ui, paddle, ball

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("QPong")
clock = pygame.time.Clock()

def main():

    # initialize game
    circuit_grid = CircuitGrid(xpos=5, ypos=FIELD_HEIGHT)
    classical_paddle = paddle.Paddle()
    quantum_paddles = paddle.QuantumPaddles(WINDOW_WIDTH - 9*WIDTH_UNIT)
    pong_ball = ball.Ball()
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(classical_paddle)
    moving_sprites.add(quantum_paddles.paddles)
    moving_sprites.add(pong_ball)

    exit = False
    while not exit:
        # update game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)

        pong_ball.update()

        # draw game
        screen.fill(BLACK)
        circuit_grid.draw(screen)
        ui.draw_statevector_grid(screen)
        moving_sprites.draw(screen)
        pygame.display.flip()

        # set game framerate
        clock.tick(FPS)

if __name__ == "__main__":
    main()


