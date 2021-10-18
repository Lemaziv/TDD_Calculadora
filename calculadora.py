class Calculadora:

    def valor(self):
        return self.total

    def suma(self, x, y):
        self.total = x+y
    
    def resta(self, x, y):
        self.total = x-y

    def multiplicacion(self, x, y):
        self.total = x*y

    def division(self, x, y):
        self.total = x/y