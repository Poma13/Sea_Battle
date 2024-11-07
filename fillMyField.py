import time
from filling_field_functions import dontPut
import pygame
from random import randint
"""
def VG(keys, vg):
    if keys[pygame.K_SPACE]:
        return (vg+1)%2
    else:
        return vg
"""


def moveMF(keys, speed, x, y, decks, vorg):

    if vorg == 1:
        stopPosX = 400 - decks * 40
        stopPosY = 360
    if vorg == 0:
        stopPosY = 400 - decks * 40
        stopPosX = 360
    if keys[pygame.K_LEFT]:
        x -= speed
        if x < 0:
            x += speed
    elif keys[pygame.K_UP]:
        y -= speed
        if y < 0:
            y += speed

    elif keys[pygame.K_RIGHT]:
        x += speed
        if x > stopPosX:
            x -= speed

    elif keys[pygame.K_DOWN]:
        y += speed
        if y > stopPosY:
            y -= speed
    time.sleep(0.1)
    return [x, y]

def buildBoat(myl, my_boats_coord, coord, vorg, decks, myBoats):
    yes = False
    put = True
    lst = []
    if vorg:
        for c in range(decks):
            lst.append(coord + c)
        for i in lst:
            if myl[i].addBoat == False:
                put = False

        if put:
            my_boats_coord.append([])
            for i in range(decks):
                myl[coord + i].status = 'boat'
                my_boats_coord[myBoats].append(coord + i)
            myl = dontPut(my_boats_coord[myBoats], myl)
            yes = True

    else:
        for c in range(decks):
            lst.append(coord + c * 10)
        for i in lst:
            if myl[i].addBoat == False:
                put = False
        if put:
            my_boats_coord.append([])
            for i in range(decks):
                myl[coord + i * 10].status = 'boat'
                my_boats_coord[myBoats].append(coord + i * 10)
            myl = dontPut(my_boats_coord[myBoats], myl)
            yes = True

    time.sleep(0.2)
    return [myl, my_boats_coord, yes]

def drawMyRect(decks, vorg):
    if vorg:
        w = decks * 40
        h = 40
    else:
        w = 40
        h = decks * 40

    return [w, h]
