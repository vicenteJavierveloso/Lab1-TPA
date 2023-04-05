class Camara:
    def __init__(self,id,nombre,resolucion):
        self.__id = id
        self.__nombre = nombre
        self.__resolucion = resolucion
    def transmitir(self):
        print(f"La cámara {self.nombre} está transmitiendo en vivo.")
    def get_id(self):
        return self.__id





    