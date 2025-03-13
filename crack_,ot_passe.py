import hashlib
import os
import time
import sys


def hash_crack(password_hashed, filename='liste_francais.txt', detail=False):
    """
    Fonction pour tenter de retrouver un mot de passe à partir d'un hash MD5 en utilisant un fichier de mots-clés.

    :param password_hashed: Le mot de passe hashé à retrouver
    :param filename: Nom du fichier contenant les mots-clés
    :param detail: Afficher la progression si True
    :return: Le mot de passe en clair s'il est trouvé, sinon None
    """
    debut = time.time()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                mots_dict = line.strip()
                if detail:
                    sys.stdout.write(f'\r{" " * 100}')
                    sys.stdout.write(f"\r{mots_dict} ")
                    sys.stdout.flush()
                    time.sleep(0.001)

                if hashlib.md5(mots_dict.encode('utf-8')).hexdigest() == password_hashed:
                    print(f"\nLe mot de passe est: {mots_dict}")
                    return mots_dict
    except FileNotFoundError:
        print("Le fichier n'existe pas")
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")

    print("Mot de passe introuvable / le mot hashé n'est pas dans la liste")
    print(f"Exécution en {(time.time() - debut):.2f} s")
    return None


# Exemple d'utilisation
def main():
    print('Dans crack dico')
    password_hash = input("Entrez le mot hashé : ")
    hash_crack(password_hash, detail=True)


if __name__ == "_main_":
    main()