from __future__ import annotations
from producto.producto import Producto
import datetime
from random import randint

class Comanda():
    def __init__(self, orden: int, llevar:bool , total: float, subtotal: float, tipo: str) -> None:
        self.orden:int = orden
        self.llevar:bool = llevar
        self.total:float = total
        self.subtotal:float = subtotal
        self.fecha = datetime.datetime.now()
        self.list_product:list[Producto] = []
        self.status: bool 
        self.num_orden: int = randint(1000, 9999)
        self.tipo_orden = tipo

    def agregar_producto(self, producto: Producto) -> None:
        self.list_product.append(producto)
    
    def eliminar_producto(self, producto: Producto) -> None:
        self.list_product.remove(producto)

    def __str__(self) -> str:
        return f"{self.orden} {self.llevar} {self.total} {self.subtotal} {self.fecha} {self.list_product}"
