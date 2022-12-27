# GAME FRAMERATE
FPS = 60

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAGENTA = (255, 0, 255)
GRAY = (127, 127, 127)

# NUMBER OF QUBITS FOR THE QUANTUM CIRCUIT
NUM_QUBITS = 3

# GAME DIMENSIONS
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 750
FIELD_HEIGHT = round(WINDOW_HEIGHT * 0.7) # height of pong play field
WIDTH_UNIT = round(WINDOW_WIDTH / 100) # which unit used for scaling the game
PADDLE_HEIGHT = round(FIELD_HEIGHT / 2**NUM_QUBITS)

# COOLDOWN TIME (IN MILLISECONDS) BEFORE THE NEXT MEASUREMENT IS ALLOWED
MEASUREMENT_COOLDOWN_TIME = 4000

# SCORE TO WIN A GAME
WIN_SCORE = 5