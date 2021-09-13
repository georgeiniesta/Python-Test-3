# Paso 1: Crea una lista vacía llamada beatles.

beatles = [ ]

# Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison
beatles.append ('John Lennon')
beatles.append ('Paul McCartney')
beatles.append ('George Harrison')
print("Step 2:", beatles)

# Paso 3: Emplea el ciclofor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.
print ("Add Stu Sutcliffe, and Pete Best to the list")
for i in range (2):
  beatles.append (input())
  print ("Step 3:", beatles)
 
# Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
del beatles [3:5]
print("Step 4:", beatles)

# Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.
for i in range(1):
   beatles.insert(0, 'Ringo Starr')
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))