from random import choice
from myAttack import checkKill


def dontGo(coords, vars, eneml):
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
            if c - 11 in vars:
                vars.remove(c - 11)
                eneml[c - 11].state = 'killed'
        if t:
            if c - 10 in vars:
                vars.remove(c - 10)
                eneml[c - 10].state = 'killed'
        if tr:
            if c - 9 in vars:
                vars.remove(c - 9)
                eneml[c - 9].state = 'killed'
        if l:
            if c - 1 in vars:
                vars.remove(c - 1)
                eneml[c - 1].state = 'killed'
        if r:
            if c + 1 in vars:
                vars.remove(c + 1)
                eneml[c + 1].state = 'killed'
        if bl:
            if c + 9 in vars:
                vars.remove(c + 9)
                eneml[c + 9].state = 'killed'
        if b:
            if c + 10 in vars:
                eneml[c + 10].state = 'killed'
                vars.remove(c + 10)
        if br:
            if c + 11 in vars:
                eneml[c + 11].state = 'killed'
                vars.remove(c + 11)
    if c in vars:
        vars.remove(c)
        # print(c)

    return [vars, eneml]


def helpFuncX(coord, vars):
    l = []
    if coord % 10 != 0:
        if coord - 1 in vars:
            l.append(coord - 1)
    if coord % 10 != 9:
        if coord + 1 in vars:
            l.append(coord + 1)

    return l


def helpFuncY(coord, vars):
    l = []
    if coord // 10 != 0:
        if coord - 10 in vars:
            l.append(coord - 10)
    if coord // 10 != 9:
        if coord + 10 in vars:
            l.append(coord + 10)

    return l


def chooseCoord(enemies, coord, vars, naprav):
    l = []
    newCoord = 0
    if naprav == '':
        lx = helpFuncX(coord, vars)
        ly = helpFuncY(coord, vars)
        for i in lx:
            l.append(i)
        for i in ly:
            l.append(i)
    elif naprav == 'x':
        lx = helpFuncX(coord, vars)
        for i in lx:
            l.append(i)
    elif naprav == 'y':
        ly = helpFuncY(coord, vars)
        for i in ly:
            l.append(i)
    if l != []:
        newCoord = choice(l)
        return newCoord
    else:
        if naprav == 'x':
            if enemies[coord - 1].status == 'boat':
                # ищем влево
                if coord - 2 in vars:
                    newCoord = coord - 2
                else:
                    newCoord = coord - 3

            else:
                # ищем вправо
                if coord + 2 in vars:
                    newCoord = coord + 2
                else:
                    newCoord = coord + 3

        elif naprav == 'y':

            if enemies[coord - 10].status == 'boat':
                # ищем вверх
                if coord - 20 in vars:
                    newCoord = coord - 20
                else:
                    newCoord = coord - 30
            else:
                # ищем вниз
                if coord + 20 in vars:
                    newCoord = coord + 20
                else:
                    newCoord = coord + 30
    return newCoord


def getNaprav(c1, c2):
    if c1 % 10 == c2 % 10:
        return 'y'
    if c1 // 10 == c2 // 10:
        return 'x'
    else:
        return ''


def botAttack(enemies, boats, vars, botsmoves, newDd, naprav, shot):
    throw = 'me'
    aaa = False
    endGame = False
    if len(vars) == 0:
        endGame = True

    else:
        if len(botsmoves) == 0 or newDd or botsmoves[-1].status == 'miss':
            naprav = ''
            nowhod = choice(vars)
            vars.remove(nowhod)
            if enemies[nowhod].status == 'boat':
                enemies[nowhod].state = 'damaged'
                throw = 'bot'
                shot = True

            if enemies[nowhod].status == 'water':
                enemies[nowhod].state = 'killed'
                shot = False

        elif botsmoves[-1].status == 'dmg':
            nowhod = chooseCoord(enemies, botsmoves[-1].coord, vars, naprav)
            vars.remove(nowhod)
            if enemies[nowhod].status == 'boat':
                naprav = getNaprav(nowhod, botsmoves[-1].coord)
                enemies[nowhod].state = 'damaged'
                throw = 'bot'
                shot = True
            if enemies[nowhod].status == 'water':
                enemies[nowhod].state = 'killed'
                shot = True
                aaa = True

        lst = checkKill(enemies, boats)
        enemies, newDd = lst[0], lst[1]
        if newDd:
            bt = []
            for i in boats:
                if nowhod in i:
                    bt = i
                    break
            lstDG = dontGo(bt, vars, enemies)
            vars, enemies = lstDG[0], lstDG[1]
        if aaa:
            nowhod = botsmoves[-1].coord

    return [endGame, newDd, enemies, vars, throw, nowhod, naprav, shot]

