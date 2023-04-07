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
    def iniciarTransmision(self):
        if self.__inicio == "":
            self.__inicio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.__camara.transmitir()
            return True
        else:
            return False
    def terminarTransmision(self):
        if self.__inicio != "":
            self.__fin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            return True
        else:
            return False

    def cambiarCamara(self):
        if self.__inicio != "":
            indice_cam_actual = self.__lista_camaras.index(self.__camara)
            if indice_cam_actual == len(self.__lista_camaras)-1:
                self.__camara = self.__lista_camaras[0]
                self.__camara.transmitir()
            else:
                self.__camara = self.__lista_camaras[indice_cam_actual+1]
                self.__camara.transmitir()
        else:
            return False

    def get_camara(self):
        return self.__camara.get_id()