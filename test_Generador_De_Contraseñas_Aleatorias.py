import unittest
from random import randint

def CrearContrasena(numero):
    contra = []
    for i in range(numero):
        num = randint(33, 126)
        contra.append(chr(num))
        contrasena = ''.join(contra)
    print(contrasena)

n= int(input("De cuantos caracteres sera la contrasena?: "))
CrearContrasena(n)

class Test_Contrasena(unittest.TestCase):

    def test_la_contraseña_tiene_caracteres(self):
        self.assertFalse(self.CrearContrasena(8) != None)

    def test_la_contraseña_tiene_caracteres_tiene_5_caracteres(self):
        self.assertEqual(8,self.CrearContrasena(8))