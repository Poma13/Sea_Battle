def dontGo(coords, eneml):
    if coords != []:
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
                eneml[c - 11].state = 'killed'
            if t:
                eneml[c - 10].state = 'killed'
            if tr:
                eneml[c - 9].state = 'killed'
            if l:
                eneml[c - 1].state = 'killed'
            if r:
                eneml[c + 1].state = 'killed'
            if bl:
                eneml[c + 9].state = 'killed'
            if b:
                eneml[c + 10].state = 'killed'
            if br:
                eneml[c + 11].state = 'killed'
    return eneml


def myAttack(boats, enemies, coord):
    shot = False
    if enemies[coord].state == 'damaged' or enemies[coord].state == 'killed':
        shot = True
    if enemies[coord].status == 'water':
        enemies[coord].state = 'killed'

    else:
        if enemies[coord].state == 'invise':
            enemies[coord].state = 'damaged'
            shot = True

    lst = checkKill(enemies, boats)
    enemies, newDd = lst[0], lst[1]
    if newDd:
        enemies = dontGo(lst[2], enemies)

    return [enemies, shot, newDd]


def checkKill(enemies, boats):
    newDd = False
    Bt = []
    for bt in boats:
        kld = 0
        for c in bt:
            if enemies[c].state == 'damaged':
                kld += 1
        if kld == len(bt):
            for c in bt:
                enemies[c].state = 'killed'
            Bt = bt
            newDd = True
    return [enemies, newDd, Bt]
