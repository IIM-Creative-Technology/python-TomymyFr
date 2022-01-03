import time

x = input("Entrer un nombre de seconde : ")
'''
while type(x) is not int and type(x) is not float:
    try:
        x = int(x)
    except:
        print("Erreur")
        print(type(x))
        x = input("Entrer un nombre de seconde de type int ou float x : ")
'''
print("Début du minuteur")
for i in range(x):
    time.sleep(1)
    print("Wait")
print("DRING DRING \nFin du minuteur")
