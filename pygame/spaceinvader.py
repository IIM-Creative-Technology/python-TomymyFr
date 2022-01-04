import pygame
import time
# import os
import random

module_charge = pygame.init()
# print(module_charge)
ecran_x = 500
ecran_y = 500
ecran = pygame.display.set_mode((ecran_x, ecran_y))
pygame.display.set_caption("ZE labyrinth")
#image = pygame.image.load("logo.png").convert()
#pygame.display.set_icon(image)

#print(image)

# Boucle du jeu

loop = True
i = 0
position_x = 475
position_y = 25
radius = 15
limite = False
fin_jeu = False
vie = 10
touche = False


chemin = random.randrange(3)
print(f"chemin n°{chemin}")

if chemin == 1:
    check_column = ["column19", "column29", "column36","column38", "column46", "column48", "column52", "column58" ,"column62", "column68" ,"column74", "column76", "column84", "column86", "column94", "column96", "column310", "column410", "column510", "column610", "column710", "column810", "column910"]
    check_line = ["line29","line34", "line36","line39","line44", "line46", "line49", "line54", "line64", "line72", "line76", "line79", "line82", "line86", "line89","line99", "line102", "line100", "line109"]
elif chemin == 2:
    check_column = ["column29", "column38", "column47", "column56", "column65", "column74", "column83", "column92", "column110"]
    check_line = ["line29", "line38", "line47", "line56", "line65", "line74", "line83", "line92", "line101"]
else:
    check_column = ["column19", "column21","column22","column31","column32","column41","column42","column51","column52","column61","column62","column71","column72","column81","column82","column91","column92","column101","column110","column210", "column310", "column410", "column510", "column610", "column710", "column810", "column910"]
    check_line = ["line20","line30","line31", "line39","line40","line41","line49","line50","line51","line59","line60","line61", "line69","line70","line71", "line79","line80","line81", "line89","line90", "line91", "line99", "line109"]
while loop:
    # ecran.blit(image, (250, 250))
    # pygame event
    ecran.fill((0,0,0))
    detection_fin = pygame.draw.rect(ecran, (255,255,255),(10, 475, 2, 2))
    square_debut = pygame.draw.rect(ecran, (255,73,0),(450, 0, 50, 50))
    square_fin = pygame.draw.rect(ecran, (45,232,25),(0, 450, 50, 50))
    circle = pygame.draw.circle(ecran, (255, 255, 0), (position_x, position_y), radius)

    # Lignes
    linename = "line"
    columnname = "column"
    j = 0
    k = 0
    o = 1
    p = 1
    while j < 500 and k < 500:
        fullline = (linename + str(p) + str(o))
        # print(fullline)
        if fullline not in check_line:
            fullline = pygame.draw.line(ecran, (100, 100, 100), (j, k), (j+50, k), 4)
            if circle.colliderect(fullline) and touche == False:
                fullline = pygame.draw.line(ecran, (255, 0, 0), (j, k), (j+50, k), 4)
                if circle.colliderect(square_debut) == False:
                    vie -= 1
                    print(f"Nombre de vie : {vie}")
                touche = True
            if touche == True:
                position_x = 475
                position_y = 25
                touche = False
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
        fullcolumn = (columnname + str(r) + str(s))
        # print(fullcolumn)
        r += 1
        if fullcolumn not in check_column:
            fullcolumn = pygame.draw.line(ecran, (100, 100, 100), (l, m), (l, m+50), 4)
            if circle.colliderect(fullcolumn) and touche == False:
                fullcolumn = pygame.draw.line(ecran, (255, 0, 0), (l, m), (l, m+50), 4)
                if circle.colliderect(square_debut) == False:
                    vie -= 1
                    print(f"Nombre de vie : {vie}")
                touche = True      
            if touche == True:
                position_x = 475
                position_y = 25
                touche = False
        l = l+50
        if l == 500:
            m +=50
            l = 0
            s += 1
            r = 0
        if m == 500:
            break
    vitesse = 2
    keys=pygame.key.get_pressed()
    if fin_jeu == False:
        if keys[pygame.K_DOWN]:
            if position_y > ecran_y - radius * 1.5:
                if limite == False:
                    # print("Hors limite -Y !")
                    limite = True
            else: 
                position_y += vitesse
                limite = False
                touche = False
        if keys[pygame.K_UP]:
            if position_y < 0 + radius * 1.5:
                if limite == False:
                    # print("Hors limite +Y !")
                    limite = True
            else:
                position_y -= vitesse
                limite = False
                touche = False
        if keys[pygame.K_LEFT]:
            if position_x < 0 + radius * 1.5:
                if limite == False:
                    # print("Hors limite -X !")
                    limite = True
            else:
                position_x -= vitesse
                limite = False
                touche = False
        if keys[pygame.K_RIGHT]:
            if position_x > ecran_x - radius * 1.5:
                if limite == False:
                    # print("Hors limite +X !")
                    limite = True
            else:
                position_x += vitesse
                limite = False
                touche = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                loop = False
            ''' 
            if event.key == pygame.K_k:
                os.system("exit")
                os.system("python3 spaceinvader.py") 
            '''
        if event.type == pygame.QUIT:
            loop = False
    if vie <= 0 and fin_jeu == False:
        print("Perdu")
        fin_jeu = True
        time.sleep(3)
        print("Merci d'avoir joué")
        loop = False

    if detection_fin.colliderect(circle) and fin_jeu == False: 
        print("#########################\n          Bravo          \n#########################")
        fin_jeu = True
        time.sleep(3)
        print("Merci d'avoir joué")
        loop = False
    # affichage ecran
    pygame.display.flip()

# vide le cache
pygame.quit()