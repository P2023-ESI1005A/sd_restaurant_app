from __future__ import annotations
from mesero.mesero import Mesero


class Mesa:
    def __init__(self, mesero:Mesero, numMesa:int, cupo:int, disponibilidad:bool) -> None:
        self.mesero:Mesero = mesero
        self.num_mesa:int = numMesa
        self.cupo:int = cupo
        self.disponibilidad:bool = disponibilidad

    def reservar(self) -> str:
        if(self.disponibilidad == True):
            self.disponibilidad = False
            return ("mesa no disponible")

        else:
            return("Mesa reservada")
