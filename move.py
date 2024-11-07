import pygame, time
def move(keys, speed, x, y, H):
    if keys[pygame.K_LEFT]:
        x -= speed
        if x < 0:
            x += speed

    elif keys[pygame.K_RIGHT]:
        x += speed
        if x >= 400:
            x -= speed

    elif keys[pygame.K_UP]:
        y -= speed
        if y < 0:
            y += speed

    elif keys[pygame.K_DOWN]:
        y += speed
        if y > H - 40:
            y -= speed
    time.sleep(0.1)
    return [x, y]

