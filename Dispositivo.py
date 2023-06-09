from Camara import Camara

#Campos
#__id: int
#__nombre: str
#__resolucion: str
#__marca: str
#__modelo: str

class Dispositivo(Camara):
    def __init__(self, id, nombre, resolucion, marca, modelo):
        assert type(id)==int, "id debe ser un entero"
        assert type(nombre)==str, "nombre debe ser una palabra"
        assert type(resolucion)==str, "resolucion debe ser una palabra"
        assert type(marca)==str, "marca debe ser una palabra"
        assert type(modelo)==str, "nombre debe ser una palabra"

        self.__id = id
        self.__nombre = nombre
        self.__resolucion = resolucion
        self.__marca = marca
        self.__modelo = modelo

    def get_id(self):
        return self.__id
    
    def get_info(self):
        return (self.__nombre, self.__resolucion, self.__marca, self.__modelo)
    
    def transmitir(self):
        print(f"La cámara {self.__nombre} está transmitiendo en vivo.")
