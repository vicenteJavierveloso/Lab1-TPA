from Dispositivo import Dispositivo
from datetime import datetime

#Campos:
# __id: int
# __nombre_asignatura: str
# __nombre_profesor: str
# __sala: str
# __fecha_de_clase: str
# __inicio: str
# __fin: str
# __camara: Camara
# __lista_camaras: list

class Sesion:
    def __init__(self, id, nombre_asignatura, nombre_profesor, sala, fecha_de_clase, camara, lista_camaras):
        self.__id = id
        self.__nombre_asignatura = nombre_asignatura
        self.__nombre_profesor = nombre_profesor
        self.__sala = sala
        self.__fecha_de_clase = fecha_de_clase
        self.__inicio = ""
        self.__fin = ""
        self.__camara = camara
        self.__lista_camaras = lista_camaras
        self.__estado_transmision = 0
    def iniciarTransmision(self):
        if self.__estado_transmision == 0:
            self.__inicio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.__estado_transmision = 1
            self.__camara.transmitir()
            
    def terminarTransmision(self):
        if self.__estado_transmision == 1:
            self.__fin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.__estado_transmision = 0

    def cambiarCamara(self):
        indice_cam_actual = self.__lista_camaras.index(self.__camara)
        if indice_cam_actual == len(self.__lista_camaras)-1:
            self.__camara = self.__lista_camaras[0]
            self.__camara.transmitir()
        else:
            self.__camara = self.__lista_camaras[indice_cam_actual+1]
            self.__camara.transmitir()

    def get_camara(self):
        return self.__camara.get_id()
    
    def get_lista_camaras(self):
        aux = ""
        for i in range(len(self.__lista_camaras)):
            if self.__camara.get_id() == self.__lista_camaras[i].get_id():
                aux += "* "
                aux += f"Camara {i+1}, ID:{self.__lista_camaras[i].get_id()} Nombre: {self.__lista_camaras[i].get_info()[0]}, Resolucion: {self.__lista_camaras[i].get_info()[1]}, Marca: {self.__lista_camaras[i].get_info()[2]}, Modelo: {self.__lista_camaras[i].get_info()[3]}\n"
            else:
                aux += f"Camara {i+1}, ID:{self.__lista_camaras[i].get_id()} Nombre: {self.__lista_camaras[i].get_info()[0]}, Resolucion: {self.__lista_camaras[i].get_info()[1]}, Marca: {self.__lista_camaras[i].get_info()[2]}, Modelo: {self.__lista_camaras[i].get_info()[3]}\n"
        return aux
    
    def get_estado(self):
        return self.__estado_transmision