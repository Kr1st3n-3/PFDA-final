import pygame, sys
from PIL import Image

def main():
    pygame.init()
    pygame.display.set_caption("Nighttime Fun")
    resolution = (800, 800)
    screen = pygame.display.set_mode(resolution)
    background_img = pygame.image.load("final_BG.PNG").convert_alpha()
    background_img = pygame.transform.scale(background_img, (resolution))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background_img, (0,0))
        pygame.display.flip()
                
    pygame.quit()

if __name__ == "__main__":
    main()