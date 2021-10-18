import sys

class Calculadora:

    def valor(self):
        return self.total

    def suma(self, x, y):
        self.total = x+y
        print("La suma de los números es = ",self.total)
    
    def resta(self, x, y):
        self.total = x-y
        print("La resta de los números es = ",self.total)

    def multiplicacion(self, x, y):
        self.total = x*y
        print("La multiplicación de los números es = ",self.total)

    def division(self, x, y):
        self.total = x/y
        print("La división de los números es = ",self.total)

try:
    numero_1= int(input("Digame un numero: ")) 
except ValueError:
    print('Eso no es un numero')
    sys.exit()

try:
    numero_2= int(input("Digame otro numero: "))
except ValueError:
    print('Eso no es un numero')
    sys.exit()

print ("Que operacion quiere hacer:\n1) --> sumar\n2) --> restar\n3) --> multiplicar\n4) --> dividir")
try:
    operador= int(input('Opcion: '))
except ValueError:
    print('Eso no es un numero')
    sys.exit()

if operador == 1:
    Calculadora().suma(numero_1, numero_2)

elif operador == 2:
    Calculadora().resta(numero_1, numero_2)

elif operador == 3:
    Calculadora().multiplicacion(numero_1, numero_2)

elif operador == 4:
    Calculadora().division(numero_1, numero_2)
    

