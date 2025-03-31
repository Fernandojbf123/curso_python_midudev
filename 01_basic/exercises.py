###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
import math
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print("SOLUCION EJERCICIO 1")
nombre = "Fernando"
ciudad = "CDMX"
print(f"Mi nombre es {nombre} y vivo en {ciudad}")
print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(f"""
SOLUCION EJERCICIO 2
La variable a es de tipo = {type(a)}
la variable b es de tipo = {type(b)}
la variable c es de tipo = {type(c)}
la variable d es de tipo = {type(d)}
la variable e es de tipo = {type(e)}
""")


print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
print("SOLUCION EJERCICIO 3")
cadena = "12345"
print(int(cadena))
print(float(cadena))
mi_numero = 3.99
print(float(3.99))


print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
print("SOLUCION EJERCICIO 4")
nombre = "Fernando"
edad = 40
estatura = 1.73
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {estatura} metros")


print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

print(round(math.pi,0)/2)
## nota, el resultado debería ser 1.5. Error en las instrucciones?
