num1 = 20
num2 = 4

print(f'La suma es: {num1+num2}')
print(f'La resta es: {num1-num2}')
print(f'La multiplicacion es: {num1*num2}')
print(f'La divicion es: {num1/num2}')
print(f'La divicion exacta es: {num1//num2}')
print(f'La potencia es: {num1**num2}')

# Concatenaciones en python
texto1 = "Hola"
texto2 = "Mundo"
textoFinal = texto1 + " " + texto2
print(textoFinal)
print("El saludo es: %s %s" % (texto1, texto2))
saludoFinal = "Saludo {} {}".format(texto1, texto2)
print(saludoFinal)

saludoFinal2 = "Saludo 2: {y} {x}".format(x=texto1, y=texto2)
print(saludoFinal2)
