class OperasBasicas:
    # Delaración de propiedades de clases
    num1 = 0
    num2 = 0
    res = 0

    # Declaración de constructor
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    # Declaración de metodos de clase

    def suma(self):
        self.res = self.num1 + self.num2
        print(f'Resultado: {self.res}')


def main():
    obj = OperasBasicas(1, 2)
    obj.suma()


if __name__ == '__main__':
    main()
