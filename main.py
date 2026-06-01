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
pressedKeys: set[str] = set()

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
            
            if key[pygame.K_w]: pressedKeys.add('w')
            if key[pygame.K_a]: pressedKeys.add('a')
            if key[pygame.K_s]: pressedKeys.add('s')
            if key[pygame.K_d]: pressedKeys.add('d')

        if event.type == pygame.KEYUP:
            key = pygame.key.get_pressed()
            if key[pygame.K_w]: pressedKeys.discard('w')
            if key[pygame.K_a]: pressedKeys.discard('a')
            if key[pygame.K_s]: pressedKeys.discard('s')
            if key[pygame.K_d]: pressedKeys.discard('d')


    # ===== LOGIC GOES HERE =====
    print(f"Pressed keys: {pressedKeys}")

    # input logic demo
    if 'w' in pressedKeys:
        print("wow that's really cool")


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
