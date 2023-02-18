from mesero.mesero import Mesero


class Mesa(Mesero):
    def __init__(self, num: int, capacidad: int, mesero: Mesero) -> None:
        self.num:int =  num
        self.capacidad:int = capacidad
        self.empleado_asignado:Mesero = mesero.nombre
