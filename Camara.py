from abc import ABC, abstractmethod

class Camara(ABC):
    @abstractmethod
    def get_id(self):
        pass
    
    @abstractmethod
    def transmitir(self):
        pass