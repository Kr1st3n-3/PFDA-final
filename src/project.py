import pygame, sys

# ==== Player class stays exactly the same ====
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
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

    def animate(self):
        self.is_animating = True
        
    def update(self,speed):
        if self.is_animating == True:
            self.current_sprite += speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.is_animating = False
            
        self.image = self.sprites[int(self.current_sprite)]

class Player1(pygame.sprite.Sprite):
    def __init__(self1, pos_x,pos_y):
        super().__init__()
        self1.sprites = []
        self1.is_animating = False
        self1.sprites.append(pygame.image.load('fireflys_frame1.PNG'))
        self1.sprites.append(pygame.image.load('fireflys_frame2.PNG'))
        self1.sprites.append(pygame.image.load('fireflys_frame3.PNG'))
        self1.sprites.append(pygame.image.load('fireflys_frame4.PNG'))
        self1.sprites.append(pygame.image.load('fireflys_frame5.PNG'))
        self1.sprites.append(pygame.image.load('fireflys_frame6.PNG'))
        self1.sprites.append(pygame.image.load('fireflys_frame7.PNG'))
        self1.sprites.append(pygame.image.load('fireflys_frame8.PNG'))
        self1.sprites.append(pygame.image.load('fireflys_frame9.PNG'))
        self1.sprites.append(pygame.image.load('fireflys_frame10.PNG'))
        self1.current_sprite = 0
        self1.image = self1.sprites[self1.current_sprite]

        self1.rect = self1.image.get_rect()
        self1.rect.topleft = [pos_x, pos_y]

    def animate(self1):
        self1.is_animating = True
        
    def update(self1,speed):
        if self1.is_animating == True:
            self1.current_sprite += speed

        if self1.current_sprite >= len(self1.sprites):
            self1.current_sprite = 0
            self1.is_animating = False
            
        self1.image = self1.sprites[int(self1.current_sprite)]


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
    player = Player(80, 170) 
    player1 = Player1(80,100) # somewhere visible
    moving_sprites.add(player,player1)

    # Scale all frames so fire is visible
    for i in range(len(player.sprites)):
        player.sprites[i] = pygame.transform.scale(player.sprites[i], (600, 600))
    player.image = player.sprites[player.current_sprite]

    for i in range(len(player1.sprites)):
        player1.sprites[i] = pygame.transform.scale(player1.sprites[i], (650, 650))
    player1.image = player1.sprites[player1.current_sprite]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.animate()
                if event.key == pygame.K_w:
                    player1.animate()
                    


        # Draw background first
        screen.blit(background_img, (0, 0))
        # Update fire animation every frame
        moving_sprites.update(0.25)
        # Draw player on top
        moving_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(24)
            
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

