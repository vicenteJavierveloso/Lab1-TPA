import Camara as *
class Dispositivo(Camara):
    def __init__(self, id, nombre, resolucion, marca, modelo):
        super().__init__(id, nombre, resolucion)
        self.marca = marca
        self.modelo = modelo