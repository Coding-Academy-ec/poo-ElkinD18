
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura  # Fórmula del área de un rectángulo


class Circulo:
    pi = 3.141592653589793

    def __init__(self, radio):
        self.radio = radio  # Inicialización del radio

    def area(self):
        return self.pi * (self.radio ** 2)  # Fórmula del área de un círculo
