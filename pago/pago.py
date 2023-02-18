from comanda.comanda import Comanda


class Pago(Comanda):
    def _init_(self, total):
        super.__init__(total)
        self.paid: float = 0

    def efectivo(self, amount: float):
        self.paid += amount

    def tarjeta(self, amount: float):
        self.paid += amount

    def transferencia(self, amount: float):
        self.paid += amount

    def comprobar(self):
        if self.paid == self.total:
            return "Pago completado"
        elif self.paid < self.total:
            return f"Pago pendiente: {self.total - self.paid} por pagar"
        else:
            return f"Pago excedido: {self.paid - self.total} reembolsado"
