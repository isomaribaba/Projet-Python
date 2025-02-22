#creation d'un jeux au hasard
#on importe de random pour choisir un nombre aleatoirement choisir entre 1 à 100
import random
nombre_aleatoire = random.randint(1, 100)
nombre_donne = 0
nombre_daisse = 5
print ("Le nombre rechercher est entre 1 à 100 ")
while nombre_donne != 0 and nombre_daisse > 5:
    nombre_daisse = nombre_daisse - 1
    nombre_donne = int(input("Donner un nombre :"))
    if nombre_donne  > nombre_aleatoire:
        print('choisir un nombr plus petit :')
    elif nombre_donne < nombre_aleatoire :
        print('choisir un nombre plus grand :')
    else:
        print('Brovo,vous avez gagner ')
if nombre_daisse == 0:
    print ('Vous avez perdu essayer une autre fois. ')
    print('Le nombre choisir etait ', nombre_aleatoire)
