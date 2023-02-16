from __future__ import annotations
from producto.producto import Producto
import datetime

class Comanda():
    def __init__(self, orden: int, llevar:bool , total: float, subtotal: float) -> None:
        self.orden:int = orden
        self.llevar:bool = llevar
        self.total:float = total
        self.subtotal:float = subtotal
        self.fecha = datetime.datetime.now()
        self.list_product:list[Producto] = []
        self.status: bool 

    def agregar_producto(self, producto: Producto) -> None:
        self.list.append(producto.nombre)
    
    def eliminar_producto(self, producto: Producto) -> None:
        self.list.remove(producto.nombre)

    def __str__(self) -> str:
        return f"{self.orden} {self.llevar} {self.total} {self.subtotal} {self.fecha} {self.list_product}"
