from math import sin, cos
from random import randint
import numpy as np
import Constants

class Ground:
    def __init__(self):
        self.color: tuple[int,int,int] = (105, 105, 105)

        self.numRegions: int = Constants.GROUND_POINTS

        self.vertices: list[tuple[int, int]] = [
            (
                x * Constants.SCREEN_SIZE[0]/self.numRegions,
                Constants.GROUND_HEIGHT + randint(-15, 15)
            )
            for x in range(self.numRegions+1)
        ]
        self.regions: list[int] = [v[0] for v in self.vertices]
        self.landingZone: tuple[tuple[int,int],tuple[int,int]] = self.genLandingZone()

        # these last two vertices are just so that it goes to the
        # bottom of the screen
        self.vertices.append(Constants.SCREEN_SIZE)
        self.vertices.append((0, Constants.SCREEN_SIZE[1]))
        # print(np.polyfit(self.vertices[0], self.vertices[1], 1))
    

    def genLandingZone(self) -> tuple[tuple[int, int], tuple[int, int]]:
        i: int = randint(0, self.numRegions-1)
        self.vertices[i+1] = (self.regions[i+1], self.vertices[i][1])
        return (self.vertices[i], self.vertices[i+1])


    def getVertices(self) -> list[tuple[int, int]]:
        return self.vertices
    

    def isPointIn(self, point: tuple[int, int]) -> bool:
        region = 0
        for i in range(self.numRegions-1):
            if self.regions[i] <= point[0] and point[0] <= self.regions[i+1]:
                region = i-1
                
        zone: tuple[tuple[int,int],tuple[int,int]] = (
            self.vertices[region], self.vertices[region+1]
        )
        m, b = np.polyfit(zone[0], zone[1], 1)
        print(f"m: {m}\tb: {b}")
        # y = lambda x: (
        #     (zone[1][1]-zone[0][1]) /
        #     (zone[1][0]-zone[0][0]) *
        #     (x - zone[0][0]) + zone[0][1]
        # )
        
        return point[1] >= m*point[0]+b


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
