import pygame, sys
from pygame import mixer 

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites = [pygame.image.load(f'fire_frame{i}.PNG')
                        for i in range(1,11)]
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
        self1.sprites = [pygame.image.load(f'fireflys_frame{i}.PNG')
                         for i in range (1,11)]
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

class Player2(pygame.sprite.Sprite):
    def __init__(self2, pos_x,pos_y):
        super().__init__()
        self2.is_animating = False
        self2.sprites = [pygame.image.load(f'owl_frame{i}.PNG')
                for i in range (1,39)]
        self2.current_sprite = 0
        self2.image = self2.sprites[self2.current_sprite]

        self2.rect = self2.image.get_rect()
        self2.rect.topleft = [pos_x, pos_y]

    def animate(self2):
        self2.is_animating = True
        
    def update(self2,fps=0.5):
        if self2.is_animating == True:
            self2.current_sprite += fps

        if self2.current_sprite >= len(self2.sprites):
            self2.current_sprite = 0
            self2.is_animating = False
            
        self2.image = self2.sprites[int(self2.current_sprite)]

def main():
    pygame.mixer.init()
    pygame.font.init()
    pygame.init()
    clock = pygame.time.Clock()
    owl_sound = pygame.mixer.Sound("owl-hooting.mp3")
    firefly_sound = pygame.mixer.Sound("twinklesparkle.mp3")
    fire_sound = pygame.mixer.Sound("campfire_crackling.mp3")
    mixer.music.load("night_crickets.mp3")
    mixer.music.play(-1)

    pygame.display.set_caption("Nighttime Fun")
    resolution = (800, 800)
    screen = pygame.display.set_mode(resolution)
    background_img = pygame.image.load("final_BG.PNG").convert_alpha()
    background_img = pygame.transform.scale(background_img, resolution)

    white = (255,255,255)
    my_font = pygame.font.SysFont("Arial", 24)
    text_surface = my_font.render("Press A, W, or D for a bit of nightime fun:)",True, white)
    text_rect = text_surface.get_rect() 
    text_rect = (180,30)

    moving_sprites = pygame.sprite.Group()
    player = Player(80, 170) 
    player1 = Player1(80,100)
    player2 = Player2(20,23)
    moving_sprites.add(player,player1,player2)

    for i in range(len(player.sprites)):
        player.sprites[i] = pygame.transform.scale(player.sprites[i], (600, 600))
    player.image = player.sprites[player.current_sprite]

    for i in range(len(player1.sprites)):
        player1.sprites[i] = pygame.transform.scale(player1.sprites[i], (650, 650))
    player1.image = player1.sprites[player1.current_sprite]

    for i in range(len(player2.sprites)):
        player2.sprites[i] = pygame.transform.scale(player2.sprites[i], (650, 650))
    player2.image = player2.sprites[player2.current_sprite]


    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.animate()
                    fire_sound.play()
                if event.key == pygame.K_w:
                    player1.animate()
                    firefly_sound.play()
                if event.key == pygame.K_d:
                    player2.animate()
                    owl_sound.play()
            
        
        screen.blit(background_img, (0, 0))
        screen.blit(text_surface, text_rect)
        moving_sprites.update(0.25)
        moving_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(24)
            
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

