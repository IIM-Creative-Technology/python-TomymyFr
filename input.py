name = input("Entrer un nom : ")
print(name, ", bonjour")
x = input("Entrer un nombre de type int ou float x : ")
while type(x) is not int and type(x) is not float:
    try:
        x = float(x)
    except:
        print("Erreur")
        print(type(x))
        x = input("Entrer un nombre x : ")
print(x + 2)