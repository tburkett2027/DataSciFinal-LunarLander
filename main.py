import pygame
import time
import Constants
from Rocket import Rocket
from Ground import Ground

pygame.init()

# Window size
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)

clock = pygame.time.Clock()

# Literally just a print function but shows how long into execution it ran
start_time: float = time.perf_counter()
def gamePrint(inp: str) -> float:
    print(f"<{round(time.perf_counter() - start_time, 4)}s>\t{inp}")

gamePrint("Starting game")

RocketGameObj: Rocket = Rocket()
GroundGameObj: Ground = Ground()

while True:
    # get delta time in seconds
    # this is the amount of time since the last frame was rendered
    dt = clock.tick(60) / 1000.0

    # ===== INPUT CONTROL GOES HERE =====

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamePrint("<!> Quitting! <!>")
            pygame.quit()
            raise SystemExit

    # EDUARDO!!!
    # to check a key, literally just call key[pygame.K_something]
    # all key codes are here https://www.pygame.org/docs/ref/key.html
    key = pygame.key.get_pressed()

    if key[pygame.K_ESCAPE]:
        gamePrint("<!> Quitting! <!>")
        pygame.quit()
        raise SystemExit
    
    if key[pygame.K_a]:
        RocketGameObj.tilt(-1, dt)
    if key[pygame.K_d]:
        RocketGameObj.tilt(1, dt)
    if key[pygame.K_w]:
        RocketGameObj.thrust(dt)    
    
    # if key[pygame.K_w]: gamePrint("we're going up up up")
    # if key[pygame.K_a]: gamePrint("to the left to the left to the left to the left")
    # if key[pygame.K_s]: gamePrint("watchu know about rolling down in the deep")
    # if key[pygame.K_d]: gamePrint("to the right to the right to the right to the right")


    # ===== LOGIC GOES HERE =====
    RocketGameObj.update(dt)
    # ===== RENDERING GOES HERE =====
    # fills buffer frame with black
    screen.fill("black")

    rocketrect = pygame.draw.polygon(screen, RocketGameObj.color, RocketGameObj.getVertices())
    groundrect = pygame.draw.polygon(screen, GroundGameObj.color, GroundGameObj.getVertices())
    # Horizontal wrapping (Left Right)
    if RocketGameObj.position[0] > 960:
        RocketGameObj.position[0] = 0  # Reappear on the left side
    elif RocketGameObj.position[0] < 0:
        RocketGameObj.position[0] = 960  # Reappear on the right side

    # yo rocket
    # give me your vertices so i can draw them
    # *draws vertices*

    # yo ground
    # give me your vertices so i can draw them
    # *draws vertices*

    # swaps the screen frame with the buffer frame, reversing their roles.
    # basically the buffer frame is what we're changing while the screen frame
    # puts on a show. then the buffer frame goes on stage and the screen frame becomes
    # the buffer frame to edit once again.

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
    pygame.display.flip()

pygame.quit()