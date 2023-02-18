class Mesero:
    def __init__(self, nombre: str, rfc: str, salario: float, propina: float) -> None:
        self.nombre:str = nombre
        self.rfc:str = rfc
        self.salario:float = salario
        self.propina:float = propina

    def asignacion_mesa(self, num_mesa:int):
        return (f"Te asignaron la mesa {num_mesa}")
    
    def revision_constante(self, num_mesa) -> str:
        return f"Revisando la mesa {num_mesa}"
