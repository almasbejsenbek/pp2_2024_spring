import pygame
import time
import random

pygame.init()

# Ekran parametrlari
sirina = 800
visota = 600
razmer_kletki = 20

# Tsvetlar
beliy = (255, 255, 255)
cherniy = (0, 0, 0)
krasniy = (255, 0, 0)
zeleniy = (0, 255, 0)
sinii = (0, 0, 255)

# Ekranni tanlash
ekran = pygame.display.set_mode((sirina, visota))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

# Zmeyka funksiyasi
def zmei(razmer_kletki, spisok):
    for x in spisok:
        pygame.draw.rect(ekran, zeleniy, [x[0], x[1], razmer_kletki, razmer_kletki])

# Qizil rangli yemni o'rnatish funksiyasi
def qizil_yem():
    x = round(random.randrange(0, sirina - razmer_kletki) / razmer_kletki) * razmer_kletki
    y = round(random.randrange(0, visota - razmer_kletki) / razmer_kletki) * razmer_kletki
    pygame.draw.rect(ekran, krasniy, [x, y, razmer_kletki, razmer_kletki])
    return x, y

# Sinii rangli yemni o'rnatish funksiyasi
def sinii_yem():
    x = round(random.randrange(0, sirina - razmer_kletki) / razmer_kletki) * razmer_kletki
    y = round(random.randrange(0, visota - razmer_kletki) / razmer_kletki) * razmer_kletki
    pygame.draw.rect(ekran, sinii, [x, y, razmer_kletki, razmer_kletki])
    return x, y

# Asosiy oyin loop'i
def oyin():
    game_over = False
    game_close = False

    x = sirina / 2
    y = visota / 2

    x_spd = 0
    y_spd = 0

    telo_zmei = []
    dlina_zmei = 1

    # Yemlar vaqtincha chiqib ketishi
    qizil_x, qizil_y = qizil_yem()
    sinii_x, sinii_y = sinii_yem()
    qizil_timer = time.time() + 5
    sinii_timer = time.time() + 7

    while not game_over:

        while game_close == True:
            ekran.fill(cherniy)
            font_stroka = pygame.font.SysFont(None, 100)
            tekst = font_stroka.render("Game over", True, beliy)
            ekran.blit(tekst, [sirina / 4, visota / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        oyin()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_spd = -razmer_kletki
                    y_spd = 0
                elif event.key == pygame.K_RIGHT:
                    x_spd = razmer_kletki
                    y_spd = 0
                elif event.key == pygame.K_UP:
                    y_spd = -razmer_kletki
                    x_spd = 0
                elif event.key == pygame.K_DOWN:
                    y_spd = razmer_kletki
                    x_spd = 0

        if x >= sirina or x < 0 or y >= visota or y < 0:
            game_close = True
        x += x_spd
        y += y_spd
        ekran.fill(cherniy)
        
        # Qizil yemni chiqarish va uning vaqtincha chiqib ketishini tekshirish
        if time.time() > qizil_timer:
            qizil_x, qizil_y = qizil_yem()
            qizil_timer = time.time() + 5

        # Sinii yemni chiqarish va uning vaqtincha chiqib ketishini tekshirish
        if time.time() > sinii_timer:
            sinii_x, sinii_y = sinii_yem()
            sinii_timer = time.time() + 7

        pygame.draw.rect(ekran, krasniy, [qizil_x, qizil_y, razmer_kletki, razmer_kletki])
        pygame.draw.rect(ekran, sinii, [sinii_x, sinii_y, razmer_kletki, razmer_kletki])

        telo_zmei.append([x, y])
        if len(telo_zmei) > dlina_zmei:
            del telo_zmei[0]

        for blok in telo_zmei[:-1]:
            if blok == [x, y]:
                game_close = True

        zmei(razmer_kletki, telo_zmei)

        pygame.display.update()

        if x == qizil_x and y == qizil_y:
            qizil_x, qizil_y = qizil_yem()
            qizil_timer = time.time() + 5
            dlina_zmei += 1

        if x == sinii_x and y == sinii_y:
            sinii_x, sinii_y = sinii_yem()
            sinii_timer = time.time() + 7
            dlina_zmei -= 1

        clock.tick(10)

    pygame.quit()
    quit()

oyin()