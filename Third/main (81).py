def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

if esUnTriangulo(a, b, c):
    print("Felicidades, puede ser un triángulo.")
else:
    print("Lo siento, no puede ser un triángulo.")
