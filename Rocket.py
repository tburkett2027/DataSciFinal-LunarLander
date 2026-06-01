class Rocket:
    def __init__(self):
        self.position: list[float]
        self.velocity: list[float]
        self.angular_velocity: float
        self.angle: float
        self.vertices: list[tuple(float, float)]

    def getVertices(self) -> list[tuple[float, float]]:
        # some math to calculate where the vertices are
        # default vertices for debug purposes
        return []