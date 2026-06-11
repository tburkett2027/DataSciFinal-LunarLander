from math import sin, cos
import numpy as np
import Constants

class Rocket:
    def __init__(self):
        self.position: np.ndarray = np.array([100.0, 100.0]) ## Default position
        self.velocity: np.ndarray = np.array([000.0, 0.0])
        self.angular_velocity: float = 0.0
        self.angle: float = 0.0
        self.color: tuple[int, int, int] = (255, 255, 255)
        self.vertices: list[tuple[float, float]] = [
            (0, -120), # tip
            (40, -40), # topleft
            (40, 120),  # bottomleft
            (-40, 120), # bottomright
            (-40, -40) # topright
        ]


    # rotate, accelerate due to gravity, move
    def update(self, delta: float) -> None:
        self.angular_velocity -= self.angular_velocity / 175 # rotation decay
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
    def scoreSelf(self, gameTime: float) -> int:
        print("\n:=====: SCORING LOGIC :=====:")
        print(f"Time elapsed: {gameTime}s")
        print(f"Rocket angle (degrees): {self.angle}")
        magVelo: float = (self.velocity[0]**2 + self.velocity[1]**2)**0.5
        print(f"Rocket velocity magnitude: {magVelo}")
        unitVelo: tuple[float,float] = self.velocity/magVelo
        print(f"Rocket velocity unit: {unitVelo}\n")

        angleScore: int = 0
        timeScore: int = 0
        velocityScore: int = 0
        convertedAngle: float = abs((self.angle+180) % 360 - 180)

        if convertedAngle > 10:
            print("Rocket angle from vertical too big\n")
            return -1
        elif magVelo > 42:
            print("Rocket speed too high")
            return -1

        if convertedAngle <= 2: angleScore += 5
        elif convertedAngle <= 5: angleScore += 4
        elif convertedAngle <= 7: angleScore += 3
        elif convertedAngle <= 8: angleScore += 2
        elif convertedAngle <= 10: angleScore += 1
        print(f"\nAngle score: {angleScore}")

        if gameTime <= 13: timeScore += 5
        elif gameTime <= 22: timeScore += 4
        elif gameTime <= 30: timeScore += 3
        elif gameTime <= 45: timeScore += 2
        else: timeScore += 1
        print(f"Time score: {timeScore}")

        # good speed score <= 12
        # speed breakpoints: 18-5, 24-4, 30-3, 36-2, 42-1
        if magVelo <= 18: velocityScore += 5
        elif magVelo <= 24: velocityScore += 4
        elif magVelo <= 30: velocityScore += 3
        elif magVelo <= 36: velocityScore += 2
        elif magVelo <= 42: velocityScore += 1
        print(f"Velocity score: {velocityScore}\n")


        return velocityScore + angleScore + timeScore