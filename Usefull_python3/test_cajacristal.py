import unittest 


def es_mayor_de_dad(edad):
    if edad>=18 :
        return True
    else: 
        return False


class PruebaDeCristal(unittest.TestCase): #aca se hacn los tests
    def test_es_mayor_de_edad(self):
        edad = 20
        resultado= es_mayor_de_dad(edad)
        self.assertEqual(resultado,True)
    def test_es_mayor_de_edad(self):
        edad = 15
        resultado= es_mayor_de_dad(edad)
        self.assertEqual(resultado,False)
        

if __name__ == "__main__":
    unittest.main()