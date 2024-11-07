import time, pygame#, sys
from random import randint
from sea_battle_main import game

def rndL():
    return (randint(235, 255), randint(235, 255), randint(235, 255))
def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 30
    W = 400
    H = 225
    size = [W, H]



    buttonClr = (255, 255, 255)#[210, 210, 210]
    buttonPressedClr = [160, 160, 160]
    color2 = buttonClr
    black = (50, 50, 50)

    f1 = pygame.font.Font(None, 50)
    f3 = pygame.font.Font(None, 35)
    textPlay = f1.render('Играть', True, black)
    textRules = f3.render('Правила и управление >', True, black)
    f2 = pygame.font.Font(None, 25)
    read = f2.render('Обязательно прочитай!', True, black)
    rules1 = f2.render('ПРАВИЛА:', True, black)
    rules2 = f2.render('Твои корабли не должны соприкасаться углами и сторонами', True, black)
    rules3 = f2.render('УПРАВЛЕНИЕ:', True, black)
    rules4 = f2.render('Перемещение курсора(зелёный прямоугольник) - стрелки', True, black)
    rules5 = f2.render('Поставить корабль - "B"(англ.)', True, black)
    rules6 = f2.render('Поменять расположение корабля(вертикально/горизонтально) - Пробел', True, black)
    rules7 = f2.render('Начать расстановку своих кораблей занаво - "R"(англ.)', True, black)
    rules8 = f2.render('Атака - "A"(англ.)', True, black)
    rules9 = f2.render('ИГРА:', True, black)
    rules10 = f2.render('Синий - мимо', True, black )
    rules11 = f2.render('Жёлтый - подбил корабль', True, black)
    rules12 = f2.render('Красный - потопил корабль', True, black)

    Rules = [rules1, rules2, rules3, rules4, rules5, rules6, rules7, rules8, rules9, rules10, rules11, rules12]

    pygame.display.set_caption("Морской бой")
    #pygame.display.set_icon(pygame.image.load("icon.png"))

    screen = pygame.display.set_mode(size, flags=pygame.SHOWN)

    buttonPlay = pygame.Rect(25, 25, 350, 75)
    buttonRules = pygame.Rect(25, 125, 350, 75)
    Run = True
    openRules = True

    while Run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if buttonPlay.collidepoint(mouse_pos):
                    screen = pygame.display.set_mode(size, flags=pygame.HIDDEN)
                    # subprocess.run(["python", r'C:\Users\user\PycharmProjects\sea_battle_game\sea_battle_main.py'])
                    game()
                    screen = pygame.display.set_mode(size, flags=pygame.SHOWN)
                if buttonRules.collidepoint(mouse_pos):
                    if openRules:
                        screen = pygame.display.set_mode([W + 270, H + 340], flags=pygame.SHOWN)
                        color2 = buttonPressedClr

                        textRules = f3.render('Правила и управление <', True, black)
                        openRules = False
                    else:
                        screen = pygame.display.set_mode([W, H], flags=pygame.SHOWN)
                        color2 = buttonClr
                        textRules = f3.render('Правила и управление >', True, black)

                        openRules = True

        screen.fill(rndL())

        pygame.draw.rect(screen, buttonClr, (35, 35, 330, 55))
        pygame.draw.rect(screen, color2, (35, 135, 330, 55))
        pygame.draw.rect(screen, buttonPressedClr, buttonPlay, 5)  # draw button
        pygame.draw.rect(screen, buttonPressedClr, buttonRules, 5)
        screen.blit(textPlay, (145, 45))
        screen.blit(textRules, (50, 140))
        screen.blit(read, (90, 170))
        if openRules == False:
            for i in range(len(Rules)):
                screen.blit(Rules[i], (25, 240 + 25 * i))
        pygame.display.update()
        time.sleep(0.2)
        clock.tick(fps)

    pygame.quit()
    #sys.exit


if __name__ == '__main__':
    main()