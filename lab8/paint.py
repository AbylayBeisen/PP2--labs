import pygame 
pygame.init()

FPS = 120
clock = pygame.time.Clock() 
W, H = 800, 600 
active_size = 0
active_color = 'white' 
screen = pygame.display.set_mode((W, H)) 
pygame.display.set_caption('Paint')

painting = []
def draw_menu(size, color): 
    pygame.draw.rect(screen, 'gray', (0, 0, W, 70)) 
    pygame.draw.line(screen, 'black', (0, 70), (W, 70), 3) 
    xl_brush = pygame.draw.rect(screen, 'black', (10, 10, 50, 50)) 
    pygame.draw.circle(screen, 'white', (35, 35), 20) 
    l_brush = pygame.draw.rect(screen, 'black', (70, 10, 50, 50)) 
    pygame.draw.circle(screen, 'white', (95, 35), 15) 
    m_brush = pygame.draw.rect(screen, 'black', (130, 10, 50, 50)) 
    pygame.draw.circle(screen, 'white', (155, 35), 10) 
    s_brush = pygame.draw.rect(screen, 'black', (190, 10, 50, 50)) 
    pygame.draw.circle(screen, 'white', (215, 35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]
    if size == 20:
        pygame.draw.rect(screen, 'green', (10, 10, 50, 50), 3)
    elif size == 15:
        pygame.draw.rect(screen, 'green', (70, 10, 50, 50), 3)
    elif size == 10:
        pygame.draw.rect(screen, 'green', (130, 10, 50, 50), 3)
    elif size == 5:
        pygame.draw.rect(screen, 'green', (190, 10, 50, 50), 3)
    
    
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark grey', (400, 35), 30, 3)
    
    blue = pygame.draw.rect(screen, (0, 0, 255), (W - 35, 10, 25, 25))
    red = pygame.draw.rect(screen, (255, 0, 0), (W - 60, 10, 25, 25))
    green = pygame.draw.rect(screen, (0, 255, 0), (W - 85, 10, 25, 25))
    yellow = pygame.draw.rect(screen, (255, 0, 255), (W - 35, 35, 25, 25))
    purple = pygame.draw.rect(screen, (255, 255, 0), (W - 110, 10, 25, 25))
    aqua = pygame.draw.rect(screen, (0, 255, 255), (W - 60, 35, 25, 25))
    orange = pygame.draw.rect(screen, (255,128,0), (W - 85, 35, 25, 25))
    black = pygame.draw.rect(screen, (0, 0, 0), (W - 110, 35, 25, 25))

    color_rect = [blue, red, green, yellow, purple, aqua, orange, black]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 0, 255), (255, 255, 0), (0, 255, 255), (255,128,0), (0, 0, 0)]
    return brush_list, color_rect, rgb_list

def draw_painting(paints): 
    for i in range(len(paints)): 
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])

done = True
while done:
    clock.tick(FPS)
    screen.fill('white')
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    if left_click and mouse[1] > 70:
        painting.append((active_color, mouse, active_size))
        draw_painting(painting)
    if mouse[1] > 70:
        pygame.draw.circle(screen, active_color, mouse, active_size)
    brushes, colors, rgbs = draw_menu(active_size, active_color)
    draw_painting(painting)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, brush in enumerate(brushes):
                if brush.collidepoint(event.pos):
                    active_size = 20 - (i * 5)
            for i, color in enumerate(colors):
                if color.collidepoint(event.pos):
                    active_color = rgbs[i]
    pygame.display.update()
pygame.quit()