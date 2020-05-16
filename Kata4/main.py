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
    global speed
    if rectangulo.top + 50 < screen_height:
        rectangulo.top += speed

rectangulo = pygame.Rect(10,10,50,50)
speed = 0
while True:
    screen.fill(light_gray)
for event in pygame.event.get():
    if.event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            speed = 3
        if event.key == pygame.K_DOWN:
            speed = 3
    

    mover_rectangulo()
    pygame.draw.rect(screen, white_color, rectangulo)
    pygame.display.flip()
    clock.tick(60)