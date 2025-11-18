import pygame, sys

def main():
    pygame.init()
    pygame.display.set_caption("Nighttime Fun")
    resolution = (2048, 2048)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("final BG.PNG")
    pygame.quit()

if __name__ == "__main__":
    main()