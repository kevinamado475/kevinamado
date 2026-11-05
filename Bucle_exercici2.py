# exerici 2
# crea Escriu un programa que llegeixi una seqüència de notes (valors de 0 a 10) i finalitzarà la seqüència amb el valor -1. Quan finalitzi ens ha d'indicar si "Hi ha hagut alguna nota que té un 10" o "No hi ha cap 10".
un_diez = False
nota = float(input("introduce una nota (0-10) o -1 para finalizar: "))
# se utliza el bucle while para leer las notas hasta que se ingrese -1
while nota != -1:
    if nota == 10:
        un_diez = True
    nota = float(input("introduce una nota (0-10) o -1 para finalizar: "))
if un_diez:
    print("hay alguna nota que tiene un 10")
else:
    print("no hay ninguna nota que tenga un 10")
