div = 0
cont = 0
n = int(input("ingrese un numero: "))
while div <= n:
    div += 1
    if n % div == 0:
        cont += 1
if cont == 2:
    print("el numero es primo")
else:
    print("el numero es no primo")