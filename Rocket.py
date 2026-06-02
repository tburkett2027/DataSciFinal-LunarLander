import math
import numpy as np

class Rocket:
    def __init__(self):
        self.position: np.ndarray = np.array([100.0, 100.0]) ## DEBUG VALUE, CHANGE LATER
        self.velocity: np.ndarray = np.array([100.0, 0.0]) ## DEBUG VALUE, CHANGE LATER
        self.angular_velocity: float = 1.0 ## DEBUG VALUE, CHANGE LATER
        self.angle: float = 0.0
        self.vertices: list[tuple[float, float]] = [
            (0, -110),
            (50, -35),
            (50, 90),
            (-50, 90),
            (-50, -35)
        ]

    def update(self, delta: float) -> None:
        self.position += self.velocity * delta
        self.angle += self.angular_velocity * delta


    def getVertices(self) -> np.ndarray:
        calcVerts: np.ndarray = np.array([
            (x*math.cos(self.angle) - y*math.sin(self.angle),
             x*math.sin(self.angle) + y*math.cos(self.angle))
            for x, y in self.vertices])
        
        # some math to calculate where the vertices are
        # default vertices for debug purposes
        return calcVerts * 0.25 + np.array(self.position)