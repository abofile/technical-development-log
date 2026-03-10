import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner") 
clock = pygame.time.Clock()#FPS
test_font = pygame.font.Font('font/PT.ttf', 50)

#test_surface = pygame.Surface((100,200)) #init and size a Surface
#test_surface.fill('#00FF00') #same colors methods as TK fill command is to fill the surface with a color

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render("Hello", False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha() # convert_alpha makes the image run better try to emplemete it if posssible
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    
    snail_rect.left += 3
    screen.blit(snail_surface,snail_rect)
    player_rect.right += 1  # picks a postion of the rect and moves it
    screen.blit(player_surf,(player_rect))

    pygame.display.update()
    clock.tick(60)


