div  = 0
n = int(input("ingrese un numero : "))
while div <= n:
    div += 1
    if n % div == 0 :
        print(div)