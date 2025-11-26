import pygame, sys

# ==== Player class stays exactly the same ====
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
        
    def update(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

# ==== Main program ====
def main():
    pygame.init()
    clock = pygame.time.Clock()

    pygame.display.set_caption("Nighttime Fun")
    resolution = (800, 800)
    screen = pygame.display.set_mode(resolution)
    background_img = pygame.image.load("final_BG.PNG").convert_alpha()
    background_img = pygame.transform.scale(background_img, resolution)

    # Create sprite group and player
    moving_sprites = pygame.sprite.Group()
    player = Player(80, 170)  # somewhere visible
    moving_sprites.add(player)

    # Scale all frames so fire is visible
    for i in range(len(player.sprites)):
        player.sprites[i] = pygame.transform.scale(player.sprites[i], (600, 600))
    player.image = player.sprites[player.current_sprite]


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw background first
        screen.blit(background_img, (0, 0))
        # Update fire animation every frame
        moving_sprites.update()
        # Draw player on top
        moving_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(24)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

