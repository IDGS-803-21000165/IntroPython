num1 = int(input("Escribe el primer número: "))
num2 = int(input("Escribe el segundo número: "))

if num1 > num2:
    print(f'El número {num1} es mayor que el número {num2}')
else:
    print(f'El número {num2} es mayor que el número {num1}')

print("Dame una edad".center(50, '-'))

edad = int(input("Ingresa tu edad"))

if edad > 18:
    print("Eres mayor de edad")
elif 18 == 18:
    print("tienes 18 años")
else:
    print("Eres menor de edad")
