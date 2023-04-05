from Camara import Camara
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
        if self.__fin == "":
            for i in self.__lista_camaras:
                if self.__camara.getId() == self.__lista_camaras[i].getId(): ##Si hay un match
                    if i+1 > len(self.__lista_camaras):
                        self.__camara = self.__lista_camaras[0]
                    else:
                        self.__camara = self.__lista_camaras[i+1]
                else:
                    continue
        else:
            return "La sesion ha finalizado"