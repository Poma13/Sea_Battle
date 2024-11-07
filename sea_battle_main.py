
# print('Идет генерация вражеского поля.')
# print('Это может занять несколько секунд.')


import pygame
import time
from move import move
from filling_field_functions import fillingField, dontPut
from myAttack import myAttack, checkKill
from fillMyField import moveMF, buildBoat, drawMyRect
from botAttack import botAttack

pygame.init()
def game():
    W = 840
    H = 400

    sc = pygame.display.set_mode((W, H+70))
    pygame.display.set_caption("Морской бой")
    #pygame.display.set_icon(pygame.image.load("icon.png"))


    f2 = pygame.font.Font(None, 32)
    # Colors
    WHITE = (255, 255, 255)
    BLUE = (100, 100, 255)
    BLUE2 = (200, 200, 255)
    GREEN = (0, 200, 0)
    RED = (225, 40, 40)
    BLACK = (0, 0, 0)
    BOAT = (50, 50, 50)
    YELLOW = (220, 200, 0)



    def drawLines():
        'Рисуем линии'
        l = 40
        for i in range(20):
            pygame.draw.line(sc, BLACK, (l, 0), (l, 400), 1)
            l += 40
        d = 40
        for i in range(9):
            pygame.draw.line(sc, BLACK, (0, d), (W, d), 1)
            d += 40
        pygame.draw.line(sc, (0, 0, 0), (0, 400), (840, 400), 2)
        pygame.draw.rect(sc, WHITE, (400, 0, 40, 402))
        pygame.draw.line(sc, (0, 0, 0), (398, 0), (398, 400), 2)
        pygame.draw.line(sc, (0, 0, 0), (440, 0), (440, 400), 2)






    # Объявление класса "Мое поле"
    class MyField:
        state = 'invise'
        addBoat = True

        def string(self):
            print(self.YCoord, self.Xcoord)

        def __init__(self, x, y, st='water'):
            self.status = st
            self.Xcoord = x
            self.YCoord = y

        def draw(self):
            if self.status == 'water':
                if self.state == 'invise':
                    color = BLUE2
                elif self.state == 'killed':
                    color = BLUE
            if self.status == 'boat':
                if self.state == 'invise':
                    color = BOAT
                elif self.state == 'damaged':
                    color = YELLOW
                elif self.state == 'killed':
                    color = RED
            pygame.draw.rect(sc, color, (self.Xcoord * 40, self.YCoord * 40, 40, 40))


    myl = []
    for y in range(10):
        for x in range(10):
            myl.append(MyField(x, y))


    # Объявление класса "Вражеское поле"

    class EnemyField:
        addBoat = True  # Можно ли поставить корабль
        state = 'invise'

        def __init__(self, x, y, st='water'):
            self.status = st

            self.Xcoord = x
            self.YCoord = y

        def draw(self):
            if self.status == 'water':
                if self.state == 'invise':
                    color = BLUE2
                elif self.state == 'damaged':
                    color = BLUE
                elif self.state == 'killed':
                    color = BLUE
            if self.status == 'boat':
                if self.state == 'invise':
                    color = BLUE2
                elif self.state == 'damaged':
                    color = YELLOW
                elif self.state == 'killed':
                    color = RED

            pygame.draw.rect(sc, color, (self.Xcoord * 40 + 440, self.YCoord * 40, 40, 40))


    enemyl = []
    for y in range(10):
        for x in range(10):
            enemyl.append(EnemyField(x, y))

    xyz = fillingField(enemyl)
    enemyl = xyz[0]
    enemy_boats = xyz[1]

    my_boats_coord = []

    vars = []
    for i in range(100):
        vars.append(i)

    class BotsMove:
        def __init__(self, coord, status):
            self.coord = coord
            self.status = status


    botsmovelist = []


    # Конец работы с классами

    FPS = 40  # число кадров в секунду
    clock = pygame.time.Clock()

    x = 0
    y = 0
    speed = 40
    start_time = time.time()

    vorg = 0
    myBoats = 0
    RUN = True
    throw = 'me'
    newDd = False
    naprav = ''
    shot = False
    MnewDd = 0
    EnewDd = 0




    def boatsCount(txtm, txte, sc = sc):
        sc.blit(txtm, (10, 420))
        sc.blit(txte, (450, 420))
    # Main Loop

    while RUN:

        els = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False


        run_time = time.time() - start_time

        txtMyBoats = f2.render(f'Твоих кораблей осталось: {10 - MnewDd}', True, BLACK)
        txtEnemyBoats = f2.render(f'Вражеских кораблей осталось: {10 - EnewDd}', True, BLACK)

        if round(run_time, 1) % 1 > 0.5:
            GREEN = (0, 120, 0)
        if round(run_time, 1) % 1 <= 0.5:
            GREEN = (0, 210, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            RUN = False

        sc.fill(WHITE)

        for i in myl:
            i.draw()

        for j in enemyl:
            j.draw()

        if EnewDd == 10:
            txt = f2.render('Ты выиграл!', True, (0, 100, 0))
            sc.blit(txt, (347, 420))
            drawLines()
            pygame.display.update()
            time.sleep(4)
            break

        if MnewDd == 10:
            txt = f2.render('Ты проиграл!', True, (150, 0, 0))
            sc.blit(txt, (347, 420))
            drawLines()
            pygame.display.update()
            time.sleep(4)
            break

        if throw == 'bot':

            # Вызов функции хода бота

            rtrnBA = botAttack(myl, my_boats_coord, vars, botsmovelist, newDd, naprav, shot)

            newDd, myl, vars, throw, BMcoord, naprav, shot = rtrnBA[1], rtrnBA[2], rtrnBA[3], rtrnBA[4], rtrnBA[5], rtrnBA[6], rtrnBA[7]
            if shot:
                BMstatus = 'dmg'
            else:
                BMstatus = 'miss'
            if newDd:
                MnewDd += 1
            botsmovelist.append(BotsMove(BMcoord, BMstatus))


            pygame.draw.rect(sc, GREEN, (x + 440, y, 20, 20))
            boatsCount(txtMyBoats, txtEnemyBoats)
            drawLines()
            pygame.display.update()
            clock.tick(FPS)
            time.sleep(0.3)
            continue

        coord = x // 40 + y // 4

        if myBoats < 10:
            # расстановка своих кораблей
            if keys[pygame.K_SPACE]:
                # поменять расположение корабля(вертикально/горизонтально)
                vorg = (vorg + 1) % 2
                x, y = 0, 0

                time.sleep(0.3)

            if myBoats == 0:
                # 4 палубы
                decks = 4
                sizes = drawMyRect(decks, vorg)
                movelist = moveMF(keys, speed, x, y, decks, vorg)
                y, x = movelist[1], movelist[0]
                coord = x // 40 + y // 4
                if keys[pygame.K_b]:
                    ret = buildBoat(myl, my_boats_coord, coord, vorg, decks, myBoats)
                    myl, my_boats_coord = ret[0], ret[1]
                    myBoats += 1
                    x, y = 0, 0

            elif myBoats == 1 or myBoats == 2:
                # 3 палубы
                decks = 3
                sizes = drawMyRect(decks, vorg)
                movelist = moveMF(keys, speed, x, y, decks, vorg)
                y, x = movelist[1], movelist[0]
                coord = x // 40 + y // 4
                if keys[pygame.K_b]:
                    ret = buildBoat(myl, my_boats_coord, coord, vorg, decks, myBoats)

                    if ret[2]:
                        myl, my_boats_coord = ret[0], ret[1]
                        myBoats += 1
                        x, y = 0, 0
                        time.sleep(0.2)
                    else:
                        txt1 = f2.render('Сюда поставить нельзя!', True, (150, 0, 0))
                        sc.blit(txt1, (290, 420))
                        sc.blit(f2.render('Расставь свои корабли', True, BLACK), (10, 420))
                        pygame.draw.rect(sc, RED, (x, y, sizes[0], sizes[1]))
                        drawLines()
                        pygame.display.update()
                        time.sleep(0.8)
                        continue

            elif myBoats > 2 and myBoats < 6:
                # 2 палубы
                decks = 2
                sizes = drawMyRect(decks, vorg)
                movelist = moveMF(keys, speed, x, y, decks, vorg)
                y, x = movelist[1], movelist[0]
                coord = x // 40 + y // 4
                if keys[pygame.K_b]:
                    ret = buildBoat(myl, my_boats_coord, coord, vorg, decks, myBoats)

                    if ret[2]:
                        myl, my_boats_coord = ret[0], ret[1]
                        myBoats += 1
                        x, y = 0, 0
                    else:
                        txt1 = f2.render('Сюда поставить нельзя!', True, (150, 0, 0))
                        sc.blit(txt1, (290, 420))
                        sc.blit(f2.render('Расставь свои корабли', True, BLACK), (10, 420))
                        pygame.draw.rect(sc, RED, (x, y, sizes[0], sizes[1]))
                        drawLines()
                        pygame.display.update()
                        time.sleep(0.8)
                        continue

            elif myBoats > 5:
                # 1 палубa
                decks = 1
                sizes = drawMyRect(decks, vorg)
                movelist = moveMF(keys, speed, x, y, decks, vorg)
                y, x = movelist[1], movelist[0]
                coord = x // 40 + y // 4
                if keys[pygame.K_b]:
                    ret = buildBoat(myl, my_boats_coord, coord, vorg, decks, myBoats)

                    if ret[2]:
                        myl, my_boats_coord = ret[0], ret[1]
                        myBoats += 1
                        x, y = 0, 0
                    else:
                        txt1 = f2.render('Сюда поставить нельзя!', True, (150, 0, 0))
                        sc.blit(txt1, (290, 420))
                        sc.blit(f2.render('Расставь свои корабли', True, BLACK), (10, 420))
                        pygame.draw.rect(sc, RED, (x, y, sizes[0], sizes[1]))
                        drawLines()
                        pygame.display.update()
                        time.sleep(0.8)
                        continue



            pygame.draw.rect(sc, GREEN, (x, y, sizes[0], sizes[1]))

        if myBoats < 10:
            sc.blit(f2.render('Расставь свои корабли', True, BLACK), (10, 420))

        if myBoats <= 10:
            if keys[pygame.K_r]:
                for i in myl:
                    i.status = 'water'
                    i.addBoat = True
                myBoats, x, y = 0, 0, 0
                my_boats_coord = []

        if myBoats == 10:
            sc.blit(f2.render('Для начала игры нажмите Пробел', True, BLACK), (240, 420))
            if keys[pygame.K_SPACE]:
                myBoats += 1
                drawLines()
                pygame.display.update()
                continue


        if myBoats > 10:
            moveCoords = move(keys, speed, x, y, H)
            y = moveCoords[1]
            x = moveCoords[0]
            # My attack
            if keys[pygame.K_a]:
                rtrnMA = myAttack(enemy_boats, enemyl, coord)
                enemyl, shot, kill = rtrnMA[0], rtrnMA[1], rtrnMA[2]
                if shot == False:
                    throw = 'bot'
                elif shot:
                    throw = 'me'
                if kill:
                    EnewDd += 1
                time.sleep(0.2)
            pygame.draw.rect(sc, GREEN, (x + 440, y, 20, 20))

            boatsCount(txtMyBoats, txtEnemyBoats)

        # Линии разметки (поверх всего)

        drawLines()


        pygame.display.update()
        clock.tick(FPS)




