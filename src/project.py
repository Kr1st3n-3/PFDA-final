import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('fire_frame1.PNG'))
        self.sprites.append(pygame.image.load('fire_frame2.PNG'))
        self.sprites.append(pygame.image.load('fire_frame3.PNG'))
        self.sprites.append(pygame.image.load('fire_frame4.PNG'))
        self.sprites.append(pygame.image.load('fire_frame5.PNG'))
        self.sprites.append(pygame.image.load('fire_frame6.PNG'))
        self.sprites.append(pygame.image.load('fire_frame7.PNG'))
        self.sprites.append(pygame.image.load('fire_frame8.PNG'))
        self.sprites.append(pygame.image.load('fire_frame9.PNG'))
        self.sprites.append(pygame.image.load('fire_frame10.PNG'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        
        




def main():
    pygame.init()
    clock = pygame.time.Clock()
        #Game Screen
    pygame.display.set_caption("Nighttime Fun")
    resolution = (800, 800)
    screen = pygame.display.set_mode(resolution)
    background_img = pygame.image.load("final_BG.PNG").convert_alpha()
    background_img = pygame.transform.scale(background_img, (resolution))

    running = True
    moving_sprites = pygame.sprite.Group()
    player = Player(100,100)
    moving_sprites.add(player)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background_img, (0,0))
        pygame.display.flip()
                
    pygame.quit()
    sys.exit()  

    screen.fill(0,0,0)
    moving_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(24)

if __name__ == "__main__":
    main()