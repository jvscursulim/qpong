class Computer:

    def __init__(self) -> None:
        pass

    def update(self) -> None:
        pass

class ClassicalComputer(Computer):

    def __init__(self, paddle) -> None:
        super().__init__()
        self.paddle = paddle
        self.score = 0
        self.speed = 3

    def update(self, ball):

        if self.paddle.rect.centery - ball.rect.centery > 0:
            self.paddle.rect.y -= self.speed
        else:
            self.paddle.rect.y += self.speed