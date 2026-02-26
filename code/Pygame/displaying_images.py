import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((288,600))
pygame.display.set_caption("game") 
clock = pygame.time.Clock()#FPS
test_font = pygame.font.Font('font/PT.ttf', 50)

#test_surface = pygame.Surface((100,200)) #init and size a Surface
#test_surface.fill('#00FF00') #same colors methods as TK fill command is to fill the surface with a color


ground_surface = pygame.image.load('graphics/base.png')
sky_surface = pygame.image.load('graphics/background-night.png')
text_surface = test_font.render("Hello", False, 'Red')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    
    screen.blit(ground_surface,(0,500)) # the origin point is the top left corner 
    screen.blit(sky_surface,(0,-10))
    screen.blit(text_surface,(144,300))

    pygame.display.update()
    clock.tick(60)


