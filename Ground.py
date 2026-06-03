from math import sin, cos
from random import randint
import numpy as np
import Constants

class Ground:
    def __init__(self):
        self.color = (105, 105, 105)
        self.numRegions = Constants.GROUND_POINTS
        self.vertices: list[tuple[int, int]] = [
            (
                x * Constants.SCREEN_SIZE[0]/self.numRegions,
                Constants.GROUND_HEIGHT + randint(-15, 15)
            )
            for x in range(self.numRegions+1)
        ]
        self.regions: list[int] = [v[0] for v in self.vertices]

        # these last two vertices are just so that it goes to the
        # bottom of the screen
        self.vertices.append(Constants.SCREEN_SIZE)
        self.vertices.append((0, Constants.SCREEN_SIZE[1]))
    

    def getVertices(self) -> list[tuple[int, int]]:
        return self.vertices
    

    def isPointIn(self, point: tuple[int, int]) -> bool:
        r = 0
        for i in range(len(self.regions)):
            if point[0] <= self.regions[i]:
                r = i-1
                break
        
        # some line math to find if point is under the line

        return False


# for drawing stars later
class Space:
    def __init__(self):
        self.numStars: int = 30
        self.dims: tuple[int, int] = Constants.SCREEN_SIZE
        self.vertices: list[tuple[int, int]] = [
            (randint(0,self.dims[0]), randint(0,self.dims[1]))
        ]
    
    def getVertices() -> list[tuple[int, int]]:
        return self.vertices
