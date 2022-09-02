import random


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NOMBRE_VIES = 4

vies = NOMBRE_VIES

# exo 1 : ecrire la fonction pour demander à l'utilisateur le nombre magique

def demander_nombre(nb_min, nb_max):
    # quel est le nombre magique (entre 1 et 10)
    nb_demande_convert = 0
    while nb_demande_convert == 0:
        nb_demande = input(f"Quel est le nombre magique (entre {NOMBRE_MIN} et {NOMBRE_MAX}) ?")
        try:
            nb_demande_convert = int(nb_demande)       
        except:
            print("ERREUR :Vous devez rentrer un chiffre. Réessayez !")
        else:
            if nb_demande_convert < nb_min or nb_demande_convert > nb_max:
                print(f"ERREUR: Le nombre doit être entre {nb_min} et {nb_max}. Réessayez.")
                nb_demande_convert = 0
        # return int
    return nb_demande_convert
    
    

#nb_devine = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)

# exo 2 : comparer le nombre demandé au nombre magique
# le nombre magique est plus petit
# le nombre magique est plus grand
# Bravo, vous avez trouvé !

# exo 3 : Il faut demander plusieurs fois à l'utilisateur de demander le nombre magique, tant qu'il n'a pas réussi à trouver le nombre magique

nb_devine = 0
while not nb_devine == NOMBRE_MAGIQUE and not vies == 0:
    print(f"vous reste {vies} vies")
    nb_devine = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nb_devine == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné !")
    elif nb_devine < NOMBRE_MAGIQUE:
        print("Le nombre magique est plus grand")
        vies -= 1
    else:
        print("Le nombre magique est plus petit")
        vies -= 1
        
        
if vies == 0:
    print(f"Vous avez perdu ! Le nombre magique était {NOMBRE_MAGIQUE}")





