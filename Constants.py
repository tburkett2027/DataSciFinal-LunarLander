from pygame.font import SysFont, init as startFonts
startFonts()

PI: float = 3.14159265358979323846264338327950288419

# GAME CONTROL
SCREEN_SIZE: tuple[int, int] = (960, 540) # 16:9 aspect ratio
FONT = SysFont("arial", 24, False, False)

GROUND_HEIGHT: int = 500
GROUND_VARIANCE: int = 20
GROUND_POINTS: int = 12

# INPUTS
GRAVITY: float = 1.0
ROTATION_ACCEL: float = 2.25 # degrees
THRUST_FORCE: float = 3