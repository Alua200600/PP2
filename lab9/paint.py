import pygame
import random
import math
pygame.init()
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()
    
    radius = 15
    mode = (0, 0, 0)
    last_pos = None
    
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
                
                # Define color
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
                elif event.key == pygame.K_s: #square
                    drawRectangle(screen, pygame.mouse.get_pos(), 100, 100, mode) 
                elif event.key == pygame.K_d:
                    drawRhombus(screen,pygame.mouse.get_pos(),100,100,mode)
                elif event.key == pygame.K_t:
                    drawRightTriangle(screen,pygame.mouse.get_pos(),50, 50, mode)
                elif event.key == pygame.K_e:
                    drawEquilateralTriangle(screen, pygame.mouse.get_pos(), 50 , mode)
                
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

def drawRhombus(screen,mouse_pos,width, height, color):
    #Draw Rhombus  сenter is mouse_pos
    cx ,cy = mouse_pos
    p1 = (cx , cy - height//2)
    p2 = (cx+width//2,cy)
    p3 = (cx,cy+height//2)
    p4 = (cx-width//2,cy)
    pygame.draw.polygon(screen,color,[p1,p2,p3,p4],3)

def drawRightTriangle(screen,mouse_pos,c1, c2, color):
    tx,ty = mouse_pos
    p1 = tx,ty
    p2 = (tx+c1,ty)
    p3 = (tx,ty-c2)
    pygame.draw.polygon(screen,color,[p1,p2,p3],3)


def drawEquilateralTriangle(screen, center, size, color):
    cx, cy = center
    h = (math.sqrt(3) / 3) * size  # Height from the center to the top vertex
    # Calculate the coordinates of the three vertices
    top = (cx, cy - 2 * h / 3)  # Top vertex
    bottom_left = (cx - size / 2, cy + h / 3)  # Bottom-left verte
    bottom_right = (cx + size / 2, cy + h / 3)  # Bottom-right vertex
    # Draw the triangle
    pygame.draw.polygon(screen, color, [top, bottom_left, bottom_right], 3)

main()
