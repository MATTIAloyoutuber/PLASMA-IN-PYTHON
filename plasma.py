import pygame
import math

def rgb_plasma_pygame():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))  # Screen resolution
    i = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        for x in range(1920):
            for y in range(1080):
                fx = (math.sin(x / 500 - y / 1080 * 0.1) + i / 5)
                fx2 = (math.sin(y / 500 - x / 1920 * 0.1) + i / 5)
                fx3 = (math.sin(x / 500 - y / 1080 * 0.1) + i / 5)
                fx4 = (fx + fx2 + fx3) * (fx + fx2 + fx3)
                r = int((math.sin(fx4) + 1) * 127.5)
                g = int((math.sin(fx4 + 2) + 1) * 127.5)
                b = int((math.sin(fx4 + 4) + 1) * 127.5)
                screen.set_at((x, y), (r, g, b))
        pygame.display.flip()
        i += 1

if __name__ == "__main__":
    rgb_plasma_pygame()
