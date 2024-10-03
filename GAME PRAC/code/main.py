import pygame
from random import randint
from os.path import join    #for different os

# from pygame.examples.multiplayer_joystick import player


class Player(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.surf = pygame.image.load(join('images','player.png')).convert_alpha()
        self.rec = self.surf.get_rect(center = (640,540))

pygame.init()

Window_width, Window_height = 1280, 720
display_screen = pygame.display.set_mode((Window_width, Window_height))
pygame.display.set_caption('Pewpew')
running = True
clock = pygame.time.Clock()
                                                            #convert_alpha - not transparent
                                   #refer to top               #convert()-transparent image
# player_surface = pygame.image.load(join('images','player.png')).convert_alpha() #not transparent
# player_rec = player_surface.get_frect(center = (640,540))
# player_direction = pygame.math.Vector2()
# player_speed = 300

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

stars = pygame.image.load(join('images','star.png')).convert_alpha()
star_postion = [(randint(0,Window_width),randint(0,Window_height)) for i in range(20)]

meteor_surface = pygame.image.load(join('images','meteor.png')).convert_alpha()
meteor_rec = meteor_surface.get_frect(center = (Window_width / 2, Window_height / 2))

laser_surface = pygame.image.load(join('images','laser.png')).convert_alpha()
laser_rec = laser_surface.get_frect(bottomleft = (20, Window_height -20))

while running:
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        #     print(1)
        # if event.type == pygame.MOUSEMOTION:
        #     player_rec.center = event.pos

    # key = pygame.key.get_pressed()
    # player_direction.x = int(key[pygame.K_RIGHT]) - int(key[pygame.K_LEFT])
    # player_direction.y = int(key[pygame.K_DOWN]) - int(key[pygame.K_UP])
    # player_direction = player_direction.normalize() if player_direction else player_direction
    # player_rec.center += player_direction * player_speed * dt

    recent_key = pygame.key.get_just_pressed()
    if recent_key[pygame.K_SPACE]:
        print('fire laser')

    display_screen.fill('grey')
    for pos in star_postion:
        display_screen.blit(stars, pos)

    display_screen.blit(meteor_surface, meteor_rec)
    display_screen.blit(laser_surface, laser_rec)

    # player_rec.center +=player_direction * player_speed * dt
    # if player_rec.bottom > Window_height or player_rec.top < 0:
    #     player_direction.y *= -1
    # if player_rec.right > Window_width or player_rec.left < 0:
    #     player_direction.x *= -1
    # display_screen.blit(player_surface, player_rec)
    # display_screen.blit(player.surf, player.rec)
    all_sprites.draw(display_screen)

    pygame.display.update()

pygame.quit()