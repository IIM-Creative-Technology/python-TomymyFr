password = input("Mot de passe à définir : ")
check_password = input("Bonjour, votre mot de passe SVP : ")

if check_password == password:
    print("Bienvenue")
else:
    print("I'm a teapot")