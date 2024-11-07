from random import randint


def getCoords(deck):
    'Генерирует координаты корабля по количеству палуб'
    coords = []
    if randint(0, 1):
        while 1:
            a = randint(0, 99)
            if a // 10 <= 10 - deck:
                break
        for i in range(deck):
            coords.append(a + i * 10)
    else:
        while 1:
            a = randint(0, 99)
            if a % 10 <= 10 - deck:
                break
        for i in range(deck):
            coords.append(a + i)
    return coords


def dontPut(coords, field):
    'Меняет аттрибут клеткок около корабля, который показывает, можно ли ставить на эти клетки корабль, на False'
    for c in coords:
        tl, t, tr, bl, b, br, l, r = True, True, True, True, True, True, True, True
        if c < 10:
            tl = False
            t = False
            tr = False
        if c >= 90:
            bl = False
            b = False
            br = False
        if c % 10 == 0:
            tl = False
            l = False
            bl = False
        if c % 10 == 9:
            tr = False
            r = False
            br = False
        if tl:
            field[c - 11].addBoat = False
        if t:
            field[c - 10].addBoat = False
        if tr:
            field[c - 9].addBoat = False
        if l:
            field[c - 1].addBoat = False
        if r:
            field[c + 1].addBoat = False
        if bl:
            field[c + 9].addBoat = False
        if b:
            field[c + 10].addBoat = False
        if br:
            field[c + 11].addBoat = False
        field[c].addBoat = False
    return field


def check(coords, field):
    'Проверяет, можно ли поставить корабль'
    imp = 1
    for i in coords:
        if field[i].addBoat == False:
            imp = 0
    return imp


def fillingField(field):
    "Заполнение поля"
    boats = []
    for i in range(1, 5):
        for j in range(i):
            while 1:
                coords = getCoords(5 - i)
                if check(coords, field):
                    break
            boats.append(coords)
            dontPut(coords, field)
            for coord in coords:
                field[coord].status = 'boat'
    return [field, boats] # boats - список с координатами каждого вражеского корабля
