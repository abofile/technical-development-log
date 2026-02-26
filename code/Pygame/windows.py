import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((560,540))
pygame.display.set_caption("game") # this renames the window
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get(): #this grabs all user input 
        if event.type == pygame.QUIT: #here we look for closing user input 
            pygame.quit() #to be able to close the game using the close button with out intrupting or crashing the process 
            exit() # to break the loop we use this because it's safer than using break look more about the sys module 
    pygame.display.update()
    clock.tick(60)# set max frame rate

