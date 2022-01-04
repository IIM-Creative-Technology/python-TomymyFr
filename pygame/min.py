import pygame as pg
import time as tm
# import os
import random as rd

mc = pg.init()
# pr(mc)
ex = 500
ey = 500
e = pg.display.set_mode((ex, ey))
pg.display.set_caption("ZE labyrinth")
#image = pg.image.load("logo.png").convert()
#pg.display.set_icon(image)

#pr(image)

def pr(m):
    print(m)

# Boucle du jeu

lo = True
i = 0
px = 475
py = 25
ra = 15
li = False
fj = False
pr("\033[95mBienvenue sur ZE Labyrith\033[0m")
pr("\033[96mLe but est de déplacer le cercle jaune du carré rouge au carré vert\nsans toucher les lignes grises.\033[0m")
pr("\033[96mUne ligne de touchée : une vie perdue :(\033[0m")
pr("Les bordures de l'écran ne font pas perdre de vies !")
v = int(input("Nombre de vie : ") or 10)
t = False
eg = False


ch = rd.randrange(90)
if ch <= 30:
    cc = ["column19", "column29", "column36","column38", "column46", "column48", "column52", "column58" ,"column62", "column68" ,"column74", "column76", "column84", "column86", "column94", "column96", "column310", "column410", "column510", "column610", "column710", "column810", "column910"]
    cl = ["line29","line34", "line36","line39","line44", "line46", "line49", "line54", "line64", "line72", "line76", "line79", "line82", "line86", "line89","line99", "line102", "line100", "line109"]
    # pr(f"ch n°1")
elif ch > 30 and ch <= 60:
    cc = ["column29", "column38", "column47", "column56", "column65", "column74", "column83", "column92", "column110"]
    cl = ["line29", "line38", "line47", "line56", "line65", "line74", "line83", "line92", "line101"]
    # pr(f"ch n°2")
else:
    cc = ["column19", "column21","column22","column31","column32","column41","column42","column51","column52","column61","column62","column71","column72","column81","column82","column91","column92","column101","column110","column210", "column310", "column410", "column510", "column610", "column710", "column810", "column910"]
    cl = ["line20","line30","line31", "line39","line40","line41","line49","line50","line51","line59","line60","line61", "line69","line70","line71", "line79","line80","line81", "line89","line90", "line91", "line99", "line109"]
    # pr(f"ch n°3")
while lo:
    # e.blit(image, (250, 250))
    # pg ev
    e.fill((0,0,0))
    df = pg.draw.rect(e, (255,255,255),(10, 475, 2, 2))
    sd = pg.draw.rect(e, (255,73,0),(450, 0, 50, 50))
    sf = pg.draw.rect(e, (45,232,25),(0, 450, 50, 50))
    if eg == True:
        c = pg.draw.circle(e, (rd.randrange(255), rd.randrange(255), rd.randrange(255)), (px, py), ra)
    else:
        c = pg.draw.circle(e, (255, 255, 0), (px, py), ra)
    # Lignes
    ln = "line"
    cn = "column"
    j = 0
    k = 0
    o = 1
    p = 1
    while j < 500 and k < 500:
        fl = (ln + str(p) + str(o))
        # pr(fl)
        if fl not in cl:
            fl = pg.draw.line(e, (100, 100, 100), (j, k), (j+50, k), 4)
            if c.colliderect(fl) and t == False:
                fl = pg.draw.line(e, (255, 0, 0), (j, k), (j+50, k), 4)
                if c.colliderect(sd) == False:
                    v -= 1
                    if v >= 0:
                        pr(f"Nombre de vie : {v}")
                t = True
            if t == True:
                px = 475
                py = 25
                t = False
        j = j+50
        o += 1
        if j == 500:
            j = 0
            k +=50
            p += 1
            o = 0
        if k == 500:
            break
    l = 0
    m = 0
    r = 1
    s = 1
    while l < 500 and m < 500:
        fc = (cn + str(r) + str(s))
        # pr(fc)
        r += 1
        if fc not in cc:
            fc = pg.draw.line(e, (100, 100, 100), (l, m), (l, m+50), 4)
            if c.colliderect(fc) and t == False:
                fc = pg.draw.line(e, (255, 0, 0), (l, m), (l, m+50), 4)
                if c.colliderect(sd) == False:
                    v -= 1
                    if v >= 0:
                        pr(f"Nombre de vie : {v}")
                t = True      
            if t == True:
                px = 475
                py = 25
                t = False
        l = l+50
        if l == 500:
            m +=50
            l = 0
            s += 1
            r = 0
        if m == 500:
            break
    vi = 2
    ke=pg.key.get_pressed()
    if fj == False:
        if ke[pg.K_DOWN]:
            if py > ey - ra * 1.5:
                if li == False:
                    # pr("Hors li -Y !")
                    li = True
            else: 
                py += vi
                li = False
                t = False
        if ke[pg.K_UP]:
            if py < 0 + ra * 1.5:
                if li == False:
                    # pr("Hors li +Y !")
                    li = True
            else:
                py -= vi
                li = False
                t = False
        if ke[pg.K_LEFT]:
            if px < 0 + ra * 1.5:
                if li == False:
                    # pr("Hors li -X !")
                    li = True
            else:
                px -= vi
                li = False
                t = False
        if ke[pg.K_RIGHT]:
            if px > ex - ra * 1.5:
                if li == False:
                    # pr("Hors li +X !")
                    li = True
            else:
                px += vi
                li = False
                t = False
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_j:
                lo = False
            if ev.key == pg.K_m:
                if eg == False:
                    eg = True
                else:
                    eg = False
            ''' 
            if ev.key == pg.K_k:
                os.system("exit")
                os.system("python3 spaceinvader.py") 
            '''
        if ev.type == pg.QUIT:
            lo = False
    if v <= 0 and fj == False:
        pr("#########################\n          \033[91mPerdu\033[0m          \n#########################")
        fj = True
        tm.sleep(3)
        pr("Merci d'avoir joué")
        lo = False

    if df.colliderect(c) and fj == False: 
        pr("#########################\n          \033[92mBravo\033[0m         \n#########################")
        fj = True
        tm.sleep(3)
        pr("Merci d'avoir joué")
        lo = False
    # affichage e
    pg.display.flip()

# vide le cache
pg.quit()