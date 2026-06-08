from math import sin, cos
import numpy as np
import Constants

class Rocket:
    def __init__(self):
        self.position: np.ndarray = np.array([100.0, 100.0]) ## Default position
        self.velocity: np.ndarray = np.array([000.0, 0.0])
        self.angular_velocity: float = 0.0
        self.angle: float = 0.0
        self.color: tuple[int, int, int] = (218, 73, 51)
        self.vertices: list[tuple[float, float]] = [
            (0, -120), # tip
            (40, -40), # topleft
            (40, 120),  # bottomleft
            (-40, 120), # bottomright
            (-40, -40) # topright
        ]


    # rotate, accelerate due to gravity, move
    def update(self, delta: float) -> None:
        self.angular_velocity -= self.angular_velocity / 250 # rotation decay
        self.angle = (self.angle + (self.angular_velocity * delta)) % 360
        self.velocity += np.array([0.0, Constants.GRAVITY])
        self.position += self.velocity * delta


    ## If tilting left, direction should be -1, else 1
    def tilt(self, direction: int) -> None:
        self.angular_velocity += direction * Constants.ROTATION_ACCEL
    

    def thrust(self) -> None:
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
        return calcVerts * 0.25 + np.array(self.position)


    # Scoring 5 points come from angle, the other 5 come from time, adding up to 10

    #if rocket angle is greater than 10 -10 Explode
        #between 2 -2 is a 5
        # 5 -5 is a 4
        # 7 -7 is a 3
        # 8 -8 is a 2
        # 10 -10 is a 1
    #if time is greater then 45 secconds 1 point
    #45 30 2pts
    #30 22 3pts
    #22 13 4 pts
    #less then 13 5 pts
    def scoreSelf(self, gameTime: float) -> float:
        print("\n\t:=====: SCORING LOGIC :=====:")
        print(f"Time elapsed: {gameTime}s")
        print(f"Rocket angle (degrees): {self.angle}")
        magVelo: float = (self.velocity[0]**2 + self.velocity[1]**2)**0.5
        unitVelo: tuple[float,float] = self.velocity/magVelo
        print(f"Rocket velocity magnitude: {magVelo}")
        print(f"Rocket velocity unit: {unitVelo}")

        score: float = 0.0
        convertedAngle: float = abs((self.angle+180) % 360 - 180)

        if convertedAngle <= 2: score += 5
        elif convertedAngle <= 5: score += 4
        elif convertedAngle <= 7: score += 3
        elif convertedAngle <= 8: score += 2
        elif convertedAngle <= 10: score += 1

        print("")