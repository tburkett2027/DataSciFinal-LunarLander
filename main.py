import pygame
import time

import Constants
from Rocket import Rocket
from Ground import Ground, Space
from TextBox import TextBox

pygame.init()

# Window size
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
pygame.display.set_caption("Lunar Lander")

clock = pygame.time.Clock()


# Literally just a print function but shows how long into execution it ran
start_time: float = time.perf_counter()
def gamePrint(inp: str) -> float:
    print(f"<{round(time.perf_counter() - start_time, 4)}s>\t{inp}")

gamePrint("<!> Starting game <!>")

RocketGameObj: Rocket = Rocket()
GroundGameObj: Ground = Ground()
SpaceBackground: Space = Space()

gameActive: bool = True

gameScore: int = 0 # THIS IS UPDATED AT THE VERY END
scoreDisplay: TextBox = TextBox()

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
        RocketGameObj.tilt(-1)
    if key[pygame.K_d]:
        RocketGameObj.tilt(1)
    if key[pygame.K_w]:
        if gameActive:
            RocketGameObj.color = (255, 255, 0)
        RocketGameObj.thrust()



    # ===== LOGIC GOES HERE =====
    rocketVerts = RocketGameObj.getVertices()
    groundVerts = GroundGameObj.getVertices()

    if gameActive:
        RocketGameObj.update(dt)

        # Horizontal wrapping (Left Right)
        if RocketGameObj.position[0] > Constants.SCREEN_SIZE[0]:
            RocketGameObj.position[0] = 0  # Reappear on the left side
        elif RocketGameObj.position[0] < 0:
            RocketGameObj.position[0] = Constants.SCREEN_SIZE[0]  # Reappear on the right side

        collided: bool = False
        for vert in rocketVerts:
            if GroundGameObj.isPointIn(vert):
                gamePrint(f"Collision found at Rocket vert {vert}")
                collided = True
                gameActive = False
                break

        if collided:
            gameScore = RocketGameObj.scoreSelf(time.perf_counter()-start_time)
            landing: bool = GroundGameObj.isPointLanding(RocketGameObj.position)
            print(f"Score: {gameScore}\nLanding: {landing}")

            if gameScore == -1:
                scoreDisplay.setText("You crashed LMAO")
                RocketGameObj.color = (218, 73, 51)
            else:
                scoreDisplay.setText(f"You landed! :D     Score: {gameScore}")
                RocketGameObj.color = (0, 128, 0)



    # ===== RENDERING GOES HERE =====
    # fills buffer frame with black
    screen.fill("black")

    spaceVerts = SpaceBackground.getVertices()
    for vert in spaceVerts:
        pygame.draw.circle(screen, (255, 255, 255), vert, 2)
    rocketVerts = RocketGameObj.getVertices()
    rocketrect = pygame.draw.polygon(screen, RocketGameObj.color, rocketVerts)
    groundrect = pygame.draw.polygon(screen, GroundGameObj.color, groundVerts)
    if gameActive:
        RocketGameObj.color = (255, 255, 255)

    landingZone = pygame.draw.line(screen, (255, 238, 0), GroundGameObj.landingZone[0], GroundGameObj.landingZone[1])

    if not gameActive:
        scoreDisplay.draw(screen)

    # swaps the screen frame with the buffer frame, reversing their roles.
    # basically the buffer frame is what we're changing while the screen frame
    # puts on a show. then the buffer frame goes on stage and the screen frame becomes
    # the buffer frame to edit once again.
    pygame.display.flip()

pygame.quit()