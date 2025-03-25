import pygame
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()
    
    radius = 15
    mode = (0, 0, 0)
    last_pos = None
    points = []
    
    screen.fill((255, 255, 255))  
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Выбор цвета
                if event.key == pygame.K_r:
                    mode = (255, 0, 0)
                elif event.key == pygame.K_g:
                    mode = (0, 255, 0)
                elif event.key == pygame.K_b:
                    mode = (0, 0, 255)
                elif event.key == pygame.K_y:
                    mode = (255, 255, 0)
                elif event.key == pygame.K_BACKSPACE:
                    mode = (255, 255, 255)  # eraser
                elif event.key == pygame.K_x:
                    mode = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                
                # drawing figure
                elif event.key == pygame.K_w:
                    drawRectangle(screen, pygame.mouse.get_pos(), 200, 100, mode)
                elif event.key == pygame.K_c:
                    drawCircle(screen, pygame.mouse.get_pos(), mode)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    last_pos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEMOTION and event.buttons[0]:
                if last_pos:
                    drawLineBetween(screen, last_pos, pygame.mouse.get_pos(), radius, mode)
                    last_pos = pygame.mouse.get_pos()
                else:
                    last_pos = pygame.mouse.get_pos()
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, mouse_pos, w, h, color):
    x, y = mouse_pos
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3)

def drawCircle(screen, mouse_pos, color):
    x, y = mouse_pos
    pygame.draw.circle(screen, color, (x, y), 100, 3)

main()
