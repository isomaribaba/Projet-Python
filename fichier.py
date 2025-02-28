import os
import random

from django.template.defaultfilters import make_list

"""students_list = ['Ismaila','Mariatou','Zakaria','Omar Sylla']
with open('teste.txt','a') as fille:
    for student in students_list:
        fille.write(student + "\n")
    fille.close()
"""
if os.path.exists("exercice.txt"):
    with open('exercice.txt','r+') as fille:
       ma_liste = fille.readlines()
       plat_au_hasard = random.choice (ma_liste)
       print("Vous avez le plat", plat_au_hasard)
       #   print(fille.readline())
else:
    print("Le document n'exixte pas Attention au nom du fichier")
