import time
continuer = True

while continuer :
    entree_string = input("Entrez un nombre entier positif (0 pour terminer) : ") # Prendre l'entrée de l'utilisateur et la convertir en int
    if entree_string.isnumeric():
        entree = int(entree_string)
        if entree < 0 : # Rejeter les valeurs négatives
            print("Erreur, entrée non valide.")
        elif entree > 0: # Trouver les facteurs premiers
            start = time.perf_counter()
            valeur_depart = entree
            facteurs = ()
            i = 2 # Nombre à vérifier, commence à 2 et est incrémenté au fil de la recherche
            while i * i <= valeur_depart: # Vérifier les valeurs jusqu'à la racine carrée pour optimiser
                if entree % i == 0 :
                    facteurs = facteurs + (i,)
                    entree = entree // i
                else :
                    i = i + 1
            if entree > 1 :
                facteurs = facteurs + (entree,)
            print("La décomposition en facteurs premiers est : ", end='')
            if len(facteurs) > 0 :
                print(facteurs[0], end='')
                for i in range(1, len(facteurs)):
                    print(" * ", facteurs[i], sep='', end='')
                print("")
            else :
                print(1)
            end = time.perf_counter()
            print("Time to compute: {:0.4f} seconds".format(end - start))
        else : # Sortir de la boucle
            continuer = False
    else:
        print("Erreur, entrée non valide.")
