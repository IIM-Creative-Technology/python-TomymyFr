import pygame

module_charge = pygame.init()
print(module_charge)

ecran = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Space Invader 3000")
#image = pygame.image.load("logo.png").convert()
#pygame.display.set_icon(image)

#print(image)

# Boucle du jeu

loop = True
i = 0
position_x = 250
position_y = 250
while loop:
    #ecran.blit(image, (250, 250))
    # pygame event
    ecran.fill((0,0,0))
    circle = pygame.draw.circle(ecran, (0, 0, 255), (position_x, position_y), 20)
    vitesse = 5
    keys=pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        position_y += vitesse
    if keys[pygame.K_UP]:
        position_y -= vitesse
    if keys[pygame.K_LEFT]:
            position_x -= vitesse
    if keys[pygame.K_RIGHT]:
            position_x += vitesse
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                loop = False
        if event.type == pygame.QUIT:
            loop = False
     # affichage ecran
    pygame.display.flip()

# vide le cache
pygame.quit()