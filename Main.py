from Sesion import Sesion
from Dispositivo import Dispositivo

if __name__ == "__main__":
    print(f"Bienvenido, para crear una sesión ingrese los datos en el orden que se solicitan")
    print(f"Registre todas las camaras necesarias")
    aux = int(input("Cantidad de cámaras disponibles: "))
    assert aux > 0
    camaras = []
    for i in range(0, aux):
        camaras.append(Dispositivo(i+1, input(f"Nombre cámara {i+1} "), input(f"Resolución cámara {i+1} "), input(f"Marca cámara {i+1} "), input(f"Modelo cámara {i+1} ")))
    
    sesion_default = Sesion(1,input("Nombre de la asignatura: "), input("Nombre de el/la profesor/a: "), input("Sala: "), input("Fecha de la clase (dd/mm/aa) "), camaras[0], camaras)
    
    print("La sesión ha sido creada")
    while sesion_default.get_estado() == 0:
        print("\n---*---\n1.Iniciar transmisión\n2.Mostrar cámaras")
        aux = int(input("Opción "))
        if aux == 1:
            sesion_default.iniciarTransmision()
        elif aux == 2:
            print(sesion_default.get_lista_camaras())
    while sesion_default.get_estado() == 1:
        print(f"\n---*---\nCámara en uso: ID {sesion_default.get_camara()}\n1.Finalizar transmisión\n2.Mostrar cámaras\n3.Cambiar cámaras")
        aux = int(input("Opción "))
        if aux == 1:
            sesion_default.terminarTransmision()
        elif aux == 2:
            print(sesion_default.get_lista_camaras())
        elif aux == 3:
            sesion_default.cambiarCamara()

    print("Transmisión finalizada")