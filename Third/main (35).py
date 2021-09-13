numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo contenido de la lista original.

numeros[0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior.

numeros[1] = numeros[4]  # copiando el valor del quinto elemento al segundo
print("Nuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual.
