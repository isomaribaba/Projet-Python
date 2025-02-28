with open('teste.txt','a') as fille:
    for student in students_list:
        fille.write(student + "\n")
    fille.close()
