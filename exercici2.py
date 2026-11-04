# exercici 2
# crear una calculadora que sumi, resti, multipliqui i divideixi dos nombres
# pedimos al usuario que ingrese dos números
num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))
# pedimos al usuario que ingrese la operación a realizar
operacion = input("Introdueix l'operació a realitzar (+, -, *, /): ")
# realizamos la operación correspondiente
if operacion == "+":
    resultat = num1 + num2
    print("El resultat de la suma és:", resultat)
elif operacion == "-":
    resultat = num1 - num2
    print("El resultat de la resta és:", resultat)
elif operacion == "*":
    resultat = num1 * num2
    print("El resultat de la multiplicació és:", resultat)
elif operacion == "/":
    if num2 != 0:
        resultat = num1 / num2
        print("El resultat de la divisió és:", resultat)
    else:
        print("Error: No es pot dividir per zero.")
            