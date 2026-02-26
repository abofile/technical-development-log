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
snail_x_pos = 800

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    snail_x_pos -= 4
    if snail_x_pos <= -100:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos,250))

    pygame.display.update()
    clock.tick(60)


