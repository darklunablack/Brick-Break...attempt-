

import pygame
import random

pygame.init()

#Dimension of the screen
Width, Height = 600, 500

# colors
BLACK= (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED= (255,0,0)

font= pygame.font.Font('freesansbold.ttf', 15)

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption ('Block Breaker')

#to control the frame rate
clock= pygame.time.Clock()
FPS = 30