import pygame
import time

pygame.init()

# Window size
screen = pygame.display.set_mode((960,540))

clock = pygame.time.Clock()


start_time: float = time.perf_counter()
def gamePrint(inp: str) -> float:
    print(f"{round(time.perf_counter() - start_time, 4)}s {inp}")

gamePrint("Starting game")

deltaTime: float = 0.0 # fix later

while True:

    # ===== INPUT CONTROL GOES HERE =====

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()

            if key[pygame.K_ESCAPE]:
                gamePrint("<!> Quitting! <!>")
                pygame.quit()
                raise SystemExit


    # ===== LOGIC GOES HERE =====
    


    # ===== RENDERING GOES HERE =====

    screen.fill("black")
    # this prevents old stuff from still being on screen


    # End
    pygame.display.flip()
    clock.tick(60)
