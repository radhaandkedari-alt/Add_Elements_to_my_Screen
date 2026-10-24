import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))
BACKGROUND_COLOR = (255, 255, 255)

pygame.display.set_caption("My first game screen")

my_rect = pygame.Rect(270, 190, 100, 100) 
RECT_COLOR = (255, 0, 0) 

font = pygame.font.SysFont(None, 36)
text_surface = font.render("Welcome to Pygame", True, (0, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, RECT_COLOR, my_rect)
    screen.blit(text_surface, (200, 50)) 
    
    pygame.display.flip()
