from math import sin, cos
from random import randint
import numpy as np
import Constants

class Ground:
    def __init__(self):
        self.regions: list[tuple[int, int]] = [
            # add later
        ]
        self.vertices: list[tuple[int, int]] = [
            (Constants.SCREEN_SIZE[0]/Constants.GROUND_POINTS*x, Constants.GROUND_HEIGHT + randint(-10, 10))
            for x in range(GROUND_POINTS)
        ]
    
    def getVertices(self) -> list[tuple[int, int]]:
        return self.vertices
    
    def isPointIn(self, point: tuple[int, int]) -> bool:
        pass