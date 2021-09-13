lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# coloca tu código aquí
#
resultado = []
for i in lista:
    if i not in resultado:
        resultado.append(i)

print("La lista solo con elementos únicos:")
print(resultado)
