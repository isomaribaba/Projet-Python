try:
    nbr = int(input("Donner un nombre : "))
    print(10 /nbr)
except ZeroDivisionError:
    print(f"le nombre saisi est {nbr}. {nbr} n'est divisible par 10 ")
except ValueError:
    print(f"Veuillez saisir un autre nombre")


try:
    fic = open('exercice.txt',"r")
except Exception as ex:
    print(f"Ya une erreur le nom du fichier {ex}")
else:
    print(fic.read())
finally:
    print(f" Fin du programme ")

