import pygame
import time

pygame.init()

# Window size
screen = pygame.display.set_mode((960,540))

clock = pygame.time.Clock()


start_time: float = time.perf_counter()
def gamePrint(inp: str) -> float:
    print(f"<{round(time.perf_counter() - start_time, 4)}s>\t{inp}")

gamePrint("Starting game")

deltaTime: float = 0.0 # fix later

while True:

    # ===== INPUT CONTROL GOES HERE =====

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
        

    if key[pygame.K_w]: gamePrint("we're going up up up")
    if key[pygame.K_a]: gamePrint("to the left to the left to the left to the left")
    if key[pygame.K_s]: gamePrint("watchu know about rolling down in the deep")
    if key[pygame.K_d]: gamePrint("to the right to the right to the right to the right")


    # ===== LOGIC GOES HERE =====


    # ===== RENDERING GOES HERE =====
    # yo rocket
    # give me your vertices so i can draw them
    # *draws vertices*

    # yo ground
    # give me your vertices so i can draw them
    # *draws vertices*

    screen.fill("black")
    # this prevents old stuff from still being on screen


    # End
    pygame.display.flip()
    clock.tick(60)
