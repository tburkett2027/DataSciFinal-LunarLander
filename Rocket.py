from math import sin, cos
import numpy as np
import Constants

class Rocket:
    def __init__(self):
        self.position: np.ndarray = np.array([100.0, 100.0]) ## DEBUG VALUE, CHANGE LATER
        self.velocity: np.ndarray = np.array([000.0, 0.0]) ## DEBUG VALUE, CHANGE LATER
        self.angular_velocity: float = 0.0 ## DEBUG VALUE, CHANGE LATER
        self.angle: float = 0.0
        self.vertices: list[tuple[float, float]] = [
            (0, -110), # tip
            (50, -35), # topleft
            (50, 90),  # bottomleft
            (-50, 90), # bottomright
            (-50, -35) # topright
        ]

    # rotate, accelerate due to gravity, move
    def update(self, delta: float) -> None:
        self.angular_velocity -= self.angular_velocity / 250 # rotation decay
        self.angle += self.angular_velocity * delta
        self.velocity += np.array([0.0, Constants.GRAVITY])
        self.position += self.velocity * delta


    ## If tilting left, direction should be -1, else 1
    def tilt(self, direction: int, delta: float) -> None:
        self.angular_velocity += delta * direction * Constants.ROTATION_ACCEL
    

    def thrust(self, delta: float) -> None:
        # self.velocity += np.array()
        angle = np.radians(self.angle-90)
        x_comp = cos(angle)
        y_comp = sin(angle)
        self.velocity += np.array([x_comp, y_comp]) * Constants.THRUST_FORCE


    def getVertices(self) -> np.ndarray:
        angle = np.radians(self.angle)

        calcVerts: np.ndarray = np.array([
            (x*cos(angle) - y*sin(angle),
             x*sin(angle) + y*cos(angle))
            for x, y in self.vertices])

        # some math to calculate where the vertices are
        # default vertices for debug purposes
        return calcVerts * 0.25 + np.array(self.position)