class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saluda(self, otra_persona):
        
        return f'Hola {otra_persona.nombre}, tú tienes {otra_persona.edad} años, me llamo {self.nombre} y yo tengo {self.edad} años.'


class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x) ** 2
        y_diff = (self.y - otra_coordenada.y) ** 2

        return (x_diff + y_diff) ** 0.5


if __name__ == '__main__':
    david = Persona("David", 35)
    erika = Persona("Erika", 32)
    print(david.saluda(erika))

    coordenada1 = Coordenada(3, 30)
    coordenada2 = Coordenada(4, 8)
    print(f"Distancia entre coordenadas: {coordenada1.distancia(coordenada2)}")
    print(f"Es instancia coordenada1: {isinstance(coordenada1, Coordenada)}")
    print(f"Es instancia entero 44: {isinstance(44, Coordenada)}")
