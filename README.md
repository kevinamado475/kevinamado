# Practica 02: intrducion a la programacion de python"
-**alumne:** [kevin andres amado linares]
-**curs:** [smx2-b]
-**modul:** [proyecte intermodular]
## Resum del proyecte  
## training 2 : variables y casting
### ejercicio 1 (area de un cuadrado)
¿ que hace ?
pide la medida de un costado de un cuadrado por teclado y calcula el area total de un cuadrado
¿como lo hace? 
se utiliza "input()" para leer el dato , "float()" para convertir el texto a numero decimal y la operador "**2" para elevar el costado al cuadrado 
### ejercicio 2 (calculadora basica)
¿Que hace?
recibe los numero por el teclado y muestra el resultado de su suma , resta, multiplicacion , divicion ,
¿como lo hace ?
Guarda los numeros en variables utilizando "float" y realiza las 4 operaciones basicas.
### ejercicio 3 (union de palabras)
¿que hace?
lee las 3 palabras por separado y las combina para mostrar una frase completa.
¿como lo hace?
utiliza "input" 3 veces y se utiliza "print" para colocar las palabras (variables)
### ejercicio 4 (casting float a int)
¿que hace?
recibe dos numero en decimales y devuelve el resultado en formato entero
¿como lo hace?
suma los dos numeros decimales y aplica la funcion "int()" para eliminar la parte decimal (casting)

## training 3: condicionales
### ejercicio 1 (mayor de edad)
¿que hace ? 
pide al usuario que introduzca la edad e indica si es mayor o menor de edad 
¿como lo hace? utilizando una estructura "if >=18" para comprobar si es mayor o igual de 18 años.
### ejercicio 2 (numero mas grande de los 3)
¿que hace?
compara los tres numero introducidos por el usuario y determina cual de ellos es el mayor 
¿como lo hace?
se evalua mediante la funciona de "max()"
### ejercicio 3 (postivo o negativo)
¿que hace?
lee un numero y comprueba si es positivo o negativo (considerando el 0 como positivo)
¿como lo hace?
comprueba con "if num >= 0" para clasificar si el numero es positivo o pasar al bloque "else" como negativo
## training 4 : bucles
### ejercicio 1 (numero pares)
¿que hace? 
muestra en pantalla todos los numeros pares comprendidos entre 1 al 200
¿como lo hace?
utiliza un bucle "for num in range(1,201)" tambien " if num % 2 ==0" y print para que muestre el bucle
### ejercicio 2 (busqueda al numero 10)
¿que hace?
colocamos varios numero y si hay un numero 10 enviara un mensaje que si hay un numero 10 y para finalizar es -1
¿como lo hace?
utiliza un bucle "while nota != -1 " y una variable que cambia a "true" si se detecta un 10
### ejercicio 3 (detectar numero negativos)
¿que hace?
en un rango de 10 numeros de ingreso va verificar si hay un numero negativo
¿como lo hace?
ejecuta un bucle "for" de 10 repeticiones y evalua con "if nume < 0 " para avisar si hay un numero negatvio
