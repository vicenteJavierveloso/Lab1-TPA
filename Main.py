from Sesion import Sesion
from Camara import Camara
from Dispositivo import Dispositivo

if __name__ == "__main__":
    c1 = Dispositivo(1, "Webcam", "1080", "Epson", "Cualquiera")
    c2 = Dispositivo(2, "Webcam", "1080", "Epson", "Cualquiera")
    camaras = [c1,c2]
    clase = Sesion(1,"","","","",c1,camaras)
    print(clase.get_camara())
    clase.cambiarCamara()
    print(clase.get_camara())
    clase.cambiarCamara()
    print(clase.get_camara()) #tendria que volver a 1