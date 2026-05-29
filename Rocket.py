class Rocket:
    def __init__(self):
        self.position: tuple[float, float]
        self.velocity: tuple[float, float]
        self.angular_velocity: float
        self.angle: float

    def getVertices(self) -> tuple[tuple[float, float]]:
        # some math to calculate where the vertices are
        pass