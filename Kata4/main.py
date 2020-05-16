import pygame  
screen_width = 1280
screen_height = 960
#Colors
white_color = (200, 200, 200)
light_gray = pygame.Color("grey12")

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

def mover_rectangulo():
    if rectangulo.top + 50 < screen_height:
        rectangulo.top += 3

rectangulo = pygame.Rect(10,10,50,50)
while True:
    screen.fill(light_gray)
    mover_rectangulo()
    pygame.draw.rect(screen, white_color, rectangulo)
    pygame.display.flip()
    clock.tick(60)