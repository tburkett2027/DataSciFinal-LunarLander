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
                Constants.GROUND_HEIGHT + randint(-Constants.GROUND_VARIANCE+5,Constants.GROUND_VARIANCE+5)
            )
            for x in range(self.numRegions+1)
        ]
        self.regions: list[int] = [v[0] for v in self.vertices]
        self.landingZone: tuple[tuple[int,int],tuple[int,int]] = self.genLandingZone()

        # these last two vertices are just so that it goes to the
        # bottom of the screen
        self.vertices.append(Constants.SCREEN_SIZE)
        self.vertices.append((0, Constants.SCREEN_SIZE[1]))


    ## Generates 
    def genLandingZone(self) -> tuple[tuple[int, int], tuple[int, int]]:
        i: int = randint(0, self.numRegions-1)
        self.vertices[i+1] = (self.regions[i+1], self.vertices[i][1])
        return (self.vertices[i], self.vertices[i+1])


    ## Ehh kinda useless but safer than GroundGameObj.vertices
    def getVertices(self) -> list[tuple[int, int]]:
        return self.vertices


    ## Gets ground region at a point
    def getRegion(self, point: tuple[int, int]) -> int:
        return min(self.numRegions-1,int(point[0]*(self.numRegions)/Constants.SCREEN_SIZE[0]))


    ## Checks what region a point is in
    def isPointIn(self, point: tuple[int, int]) -> bool:
        region = self.getRegion(point)

        zone: tuple[tuple[int,int],tuple[int,int]] = (
            self.vertices[region], self.vertices[region+1]
        )

        # print(f"zone: {zone}, slope: {-(zone[1][1]-zone[0][1]) / (zone[1][0]-zone[0][0])}")
        y = lambda x: (
            (zone[1][1]-zone[0][1]) /
            (zone[1][0]-zone[0][0]) *
            (x - zone[0][0]) + zone[0][1]
        )

        return point[1] >= y(point[0])

    
    def isPointLanding(self, point: tuple[int, int]) -> bool:
        return self.landingZone[0][0] <= point[0] and point[0] <= self.landingZone[1][0]


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
