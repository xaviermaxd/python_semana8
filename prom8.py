div  = 0
suma = 0
n = int(input("ingrese un numero : "))
while div < n-1:
    div += 1
    if n % div == 0 :
        suma += div
if suma == n:
    print("el numero es perfecto")
else:
    print("el numero es no perfecto")
