###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

from os import system
if system("clear") != 0: system("cls")

# Creamos una lista con valores
lista1 = ['a', 'b', 'c', 'd']

# Añadir o insertar elementos a la lista
lista1.append('e') # Añade un elemento al final
print(lista1)

lista1.insert(1, '@' ) # Inserta un elemento en la posición que le indiquemos como primer argumento
print(lista1)

lista1.extend(['😃', '😍']) # Agrega elementos al final de la lista
print(lista1)

# Eliminar elementos de la lista
lista1.remove('@') # Eliminar la primera aparición de la cadena de texto @
print(lista1)

ultimo = lista1.pop() # Eliminar el último elemento de la lista y además te lo devuelve
print(ultimo)
print(lista1)

lista1.pop(1) # Eliminar el segundo elemento de la lista (es el índice 1)
print(lista1)

# Eliminar por lo bestia un índice
del lista1[-1]
print(lista1)
 
# Eliminar un rango de elementos
lista1 = ['🐼', '🐨', '🐶', '😿', '🐹']
del lista1[1:3] # eliminamos los elementos del índice 1 al 3 (no incluye el índice 3)
print(lista1)


lista1.clear() # Eliminar todos los elementos de la lista
print(lista1)

# Más métodos útiles
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶','🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

print("SOLUCION EJERCICIO 1")
lista2 = list(range(1,6,1))
lista2.append(6)
lista2.insert(1,10) #considerando que el primer elemento de la lista es el 0.
lista2[0] = 0
print(lista2)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

print("SOLUCION EJERCICIO 2")
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
print(lista_a)
lista_a.extend(lista_b)
print(lista_a)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
print("SOLUCION EJERCICIO 3")
lista = list(range(1,11,1))
lista2 = lista[0:2:1] + lista[5::1]
print(f"usando slicing {lista2}")

lista3 = lista
del lista3[2:5:1]
print(f"usando del {lista3}")

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
print("SOLUCION EJERCICIO 4")
lista =  [5, 2, 8, 1, 9, 4, 2]
lista.sort()
print(lista)
lista.count(2)
print(f"El numero 2 aparece = {lista.count(2)} veces")
esta_el_7_en_la_lista = 7 in lista
print(f"está el 7 en la lista? {esta_el_7_en_la_lista}")

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

print("SOLUCION EJERCICIO 5")
original = [1, 2, 3]
print(f"Lista original antes de modificar la referencia = {original}")
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
print(f"Lista referencia = {referencia}")
referencia[0] = 0
print(f"Lista referencia modificada = {referencia}")
print(f"Lista original despues de modificar la referencia. NOTA en el codigo no se modificó a original = {original}")
print(f"Lista copia_1 = {copia_1}")
print(f"Lista copia_2 = {copia_2}")


# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
lista_str = ["Manzana", "pera", "BANANA", "naranja"]
lista_str.sort()
print(lista_str)