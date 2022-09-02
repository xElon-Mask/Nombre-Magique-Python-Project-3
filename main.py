NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = 5

# exo 1 : ecrire la fonction pour demander à l'utilisateur le nombre magique

def demander_nombre(nb_min, nb_max):
    # quel est le nombre magique (entre 1 et 10)
    nb_demande = int(input(f"Quel est le nombre magique (entre {NOMBRE_MIN} et {NOMBRE_MAX}) ?"))
    # return int
    return nb_demande
    

nb_devine = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)

# exo 2 : comparer le nombre demandé au nombre magique
# le nombre magique est plus petit
# le nombre magique est plus grand
# Bravo, vous avez trouvé !

if nb_devine == NOMBRE_MAGIQUE:
    print("Bravo, vous avez gagné !")
elif nb_devine < NOMBRE_MAGIQUE:
    print("Le nombre magique est plus grand")
else:
    print("Le nombre magique est plus petit")
