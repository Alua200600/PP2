import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey-Clock")

background = pygame.image.load('clock.png')
im_min = pygame.image.load('min_hand.png')
im_sec = pygame.image.load('sec_hand.png')


def blitRotate(surf, image, pos, originPos, angle):
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_rect = rotated_image.get_rect(center=pos) 
    surf.blit(rotated_image, rotated_rect.topleft)


done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    t = time.localtime()
    seconds = t.tm_sec
    minutes = t.tm_min
    hours = t.tm_hour % 12


    sec_angle = -59 + seconds * 6
    min_angle = 50 + minutes * 6

    screen.blit(background, (0, 0))
    pos = (screen.get_width() / 2, screen.get_height() / 2)

    blitRotate(screen, im_min, pos, (im_min.get_width() / 2, im_min.get_height() / 2), min_angle)
    blitRotate(screen, im_sec, pos, (im_sec.get_width() / 2, im_sec.get_height() / 2), sec_angle)

    pygame.display.flip()

pygame.quit()