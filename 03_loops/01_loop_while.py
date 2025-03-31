###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

from os import system
import math
if system("clear") != 0: system("cls")

# print("\n Bucle while:")

# # Bucle con una simple condición
# contador = 0

# while contador <= 5:
#   print(contador)
#   contador += 1 # es super importante para evitar un bucle infinito

# # utilizando la palabra break, para romper el bucle
# print("\n Bucle while con break:")
# contador = 0

# while True:
#   print(contador)
#   contador += 1
#   if contador == 5:
#     break # sale del bucle

# # continue, que lo hace es saltar esa iteración en concreto
# # y continuar con el bucle
# print("\n Bucle con continue")
# contador = 0
# while contador < 10:
#   contador += 1

#   if contador % 2 == 0:
#     continue

#   print(contador)

# # else, esta condición cuando se ejecuta?
# print("\n Bucle while con else:")
# contador = 0
# while contador < 5:
#   print(contador)
#   contador += 1
# else:
#   print("El bucle ha terminado")

# # else, esta condición cuando se ejecuta?
# print("\n Bucle while con else:")
# contador = 0
# while contador < 5:
#   print(contador)
#   contador += 1
# else:
#   print("El bucle ha terminado")

# # pedirle al usuario un número que tiene
# # que ser positivo si no, no le dejamos en paz
# numero = -1
# while numero < 0:
#   numero = int(input("Escribe un número positivo: "))
#   if numero < 0:
#     print("El número debe ser positivo. Intenta otra vez, majo o maja.")

# print(f"El número que has introducido es {numero}")

# numero = -1
# while numero < 0:
#   try:
#     numero = int(input("Escribe un número positivo: "))
#     if numero < 0:
#       print("El número debe ser positivo. Intenta otra vez, majo o maja.")
#   except:
#     print("Lo que introduces debe ser un número, que si no peta!")

# print(f"El número que has introducido es {numero}")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
# print("\nEjercicio 1:")
# cont = 0
# while cont<10:
#   cont = cont+1
#   print(cont)



# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
# print("\nEjercicio 2:")
# it = 0
# sum = 0
# while it<20:
#   it = it + 1
#   if it%2 == 0:
#     sum = sum +it

# print(f"La suma final es = {sum}")
     


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
# print("\nEjercicio 3:")
# numero = -1

# while numero <=0:
#   numero_str = input("introduduzca un numero entero >= 1\n")
#   try:
#     numero_int = int(numero_str)
#     numero_float = float(numero_str)
#     if numero_int-numero_float == 0 and numero_int>0:
#       count = numero_int
#       resultado = 1
#       numero = numero_int
#       while count > 1:
#         resultado = resultado* count
#         count = count - 1
    
#       print(f"El factorial de {numero} es = {resultado}")
    
#     else:
#       numero = -1
#       print("Debe introducir un numero entero mayor o igual a 1-")

#   except:
#     numero = -1
#     print("Debe introducir un numero entero mayor o igual a 1")
  
# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
# print("\nEjercicio 4:")
# contrasena = ""
# while len(contrasena)<8:
#   contrasena = input("introduzca una contraseña de mínimo 8 caracteres")
#   if len(contrasena)>=8:
#     print("La contraseña es valida")


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
# print("\nEjercicio 5:")
# numero = -1
# while numero<1:
#   numero_str = input("Introduzca un numero entero, positivo y mayor a 0\n")
#   try:
#     numero_int = int(numero_str)
#     numero_float = float(numero_str)
#     if numero_int-numero_float == 0 and numero_int>0:
#       count = numero_int
#       numero = numero_int
#       print("Calculando la tabla de multiplicar del {numero}")
#       it = 0
#       while it < 10:
#         print(f"{numero} x {it} = {numero*it}")
#         it = it + 1
#   except:
#     numero = -1
#     print("Debe introducir un numero entero mayor o igual a 1")  
    



# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
numero = -1
while numero<1:
  numero_str = input("Introduzca un numero entero, positivo y mayor a 0\n")
  try:
    numero_int = int(numero_str)
    numero_float = float(numero_str)
    if numero_int-numero_float == 0 and numero_int>0:
      numero = numero_int
      print(f"Calculando todos los numeros primeros menores o iguales a {numero}")
      n = 1 # número actual
      lista_de_primos = [1]
      while n<numero:
        n = n + 1
        es_primo = True
        if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
          if n==2 or n == 3 or n == 5 or n == 7:
            es_primo = True
          else:
            es_primo = False
        else:
          es_primo = True
        if es_primo:
          lista_de_primos.append(n)
          
    print(lista_de_primos)
  except:
    numero = -1
    print("Debe introducir un numero entero mayor o igual a 1")  
    