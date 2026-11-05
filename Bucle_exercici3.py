# exercici 3
#Escriu un programa que llegeixi 10 nombres, quan acabi ha d'indicar si "hi havia almenys un nombre negatiu" o "no hi ha cap nombre negatiu".
si_hay_negativo = False
for numeros in range (10):
    numeros = float(input("Introduce un número: "))
    if numeros < 0:
        si_hay_negativo = True
if si_hay_negativo:
    print("habia al menos un número negativo" )
else:
    print("no hay ningún número negativo")