from __future__ import annotations
# from mesero.mesero import Mesero

# class Mesa(Mesero):
#     def __init__(self, num: int, capacidad: int, mesero: Mesero) -> None:
#         self.num:int =  num
#         self.capacidad:int = capacidad
#         self.empleado_asignado:Mesero = mesero.nombre

from abc import ABC
from ast import List

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
        


class Empleados:
    def __init__(self, nombre:str, rfc:str, tipo:str) -> None:
        self.nombre:str = nombre
        self.rfc:str = rfc
        self.tipo:str = tipo


class Mesero(ABC):
    def __init__(self, salario:float, propina:float) -> None:
        self.salario:float = salario
        self.propina:float = propina
    
    def asignacionMesa(self, num_mesa:int):
        return (f"Te asignaron la mesa {num_mesa}")
    
    def revisionConstanste(self, num_mesa) -> str:
        return f"Revisando la mesa {num_mesa}"
    
class Gerente:
    def __init__(self, salario:int) -> None:
        self.salario = salario


class Cocinero:
    def __init__(self, salario: int, propinas: int) -> None:
        self.salario: int = salario
        self.propinas: int = propinas
    









#cLIENTE

#com1 = Comandas(1, "Juan", 2, 5)
#print(com1.agregar_productos()," Se realizo algo ")


