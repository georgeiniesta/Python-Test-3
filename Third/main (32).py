bloques = int(input("Ingrese el número de bloques:"))
h = 0
utilizados = 0 
fila = 1 #+= es suma asignacion

# Escribe tu código aquí.
while True: 
    utilizados += fila
    if utilizados >bloques:
        break
    h += 1
    fila +=1

print("La altura de la pirámide:", h)

#usamos += para decir usa 1 y suma a ese el proximo, es decir quita 1 de bloques y usa lo demas 