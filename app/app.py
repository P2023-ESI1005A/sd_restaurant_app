from comanda.comanda import Comanda
from mesero.mesero import Mesero

class Aplicacion:
    def __init__(self) -> None:
        self.queue: list [Comanda] = []
        self.lista_meseros: list[Mesero] = []
        self.menu = {
            "1": "Hamburguesa",
            "2": "Pizza",
            "3": "Papas",
            "4": "Refresco"
        }
        
    def div_cuenta () -> None:
        pass

    def alta_orden () -> None:
        pass

    def cancelar_orden () -> None:
        pass
    
    def alta_mesero () -> None:
        pass
    
    def baja_mesero () -> None:
        pass

    def add_comanda(self, comanda: Comanda) -> None:
        self.queue.append(comanda)

    def cancelar_pedido_online (self, comanda) -> None:
        for i in self.queue:
            if i.num_orden == comanda.num_orden:
                if i.tipo_orden == "online":
                    i.status = "Cancelada"
                    self.queue.remove(i)
                    print("Pedido online cancelado\n")
                    return None
        print("No se encontro el pedido\n")
    
    def cancelar_pedido_presencial (self, comanda: Comanda) -> None:
        for i in self.queue:
            if i.num_orden == comanda.num_orden:
                if i.tipo_orden == "presencial":
                    self.queue.remove(i)
                    print("Pedido presencial cancelado\n")
                    return None
        print("No se encontro el pedido\n")

    def __str__(self) -> str:
        return "".join([str(i.num_orden) + " " + i.tipo_orden + " " + i.fecha +"\n" for i in self.queue])
        
