class Humano:
    def __init__(self,edad):
        self.edad = edad

    def hablar (self, mensaje):
        print (self.edad)
        print (mensaje)

pedro = Humano(20)
raul = Humano(10)

print ("Soy pedro y tengo, " , pedro.edad)
print ("Soy raul y tengo, " , raul.edad)

pedro.hablar('Hola')
raul.hablar('Hola, Pedro')