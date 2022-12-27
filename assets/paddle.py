import pygame

from . import globals

class Paddle(pygame.sprite.Sprite):

    def __init__(self, x_pos: int = 0, y_pos: int = 0) -> None:
        super().__init__()

        self.image = pygame.Surface([globals.WIDTH_UNIT, globals.PADDLE_HEIGHT])
        self.image.fill(globals.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

class QuantumPaddles:

    def __init__(self, x_pos: int) -> None:
        self.paddles = []
        for i in range(2**globals.NUM_QUBITS):
            self.paddles.append(Paddle(x_pos=x_pos, y_pos=i*globals.PADDLE_HEIGHT))

