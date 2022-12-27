import qiskit

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

    def update(self, ball) -> None:

        if self.paddle.rect.centery - ball.rect.centery > 0:
            self.paddle.rect.y -= self.speed
        else:
            self.paddle.rect.y += self.speed

class QuantumComputer(Computer):

    def __init__(self, quantum_paddles, circuit_grid) -> None:
        super().__init__()
        self.paddles = quantum_paddles.paddles
        self.score = 0
        self.circuit_grid = circuit_grid

    def update(self, ball) -> None:

        simulator = qiskit.BasicAer.get_backend("statevector_simulator")
        circuit = self.circuit_grid.model.compute_circuit()
        transpiled_circuit = qiskit.transpile(circuits=circuit, backend=simulator)
        statevec = simulator.run(transpiled_circuit, shots=128).result().get_statevector()

        for basis_state, amplitude in enumerate(statevec):
            self.paddles[basis_state].image.set_alpha((amplitude**2)*255)
