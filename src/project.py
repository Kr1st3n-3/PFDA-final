import pygame, sys

def main():
    pygame.init()
    pygame.display.set_caption("Nighttime Fun")
    resolution = (2048, 2048)
    screen = pygame.display.set_mode(resolution)
    pygame.quit()

if __name__ == "__main__":
    main()