# Ecrivez votre code ici !
nombre1 = input("Entrez un premier nombre :")
nombre2 = input("Entrez un second nombre :")

if nombre1.isnumeric() and nombre2.isnumeric() :
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)
    operation = input("Choisissez le type d'opération : ")
    if operation == "+" :
        resultat = nombre1 + nombre2
        #print(resultat)
    elif operation == "-" :
        resultat = nombre1 - nombre2
        #print(resultat)
    elif operation == "*" :
        resultat = nombre1 * nombre2
        #print(resultat)
    elif operation == "/" :
        if nombre2 > 0 : 
            resultat = nombre1 / nombre2
            resultat = round(resultat)
        else : 
            raise SystemExit("fin du programme")
    else :
        raise SystemExit("fin du programme")
else : 
    raise SystemExit("Fin du programme")
print(resultat)
