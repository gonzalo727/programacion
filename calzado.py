from datetime import datetime

class Calzado:
    def __init__(self, fecha_creacion, origen, marca, tipo, numero, suela, modelo, materiales, stocks):
        self.fecha_creacion = fecha_creacion  # tipo datetime
        self.origen = origen  # tipo string
        self.marca = marca  # tipo string
        self.tipo = tipo  # tipo string
        self.numero = numero  # tipo int
        self.suela = suela  # tipo string
        self.modelo = modelo  # tipo string
        self.materiales = materiales  # tipo list de strings
        self.stocks = stocks  # tipo int

    def __str__(self):
        return (f"Calzado:\n"
                f"  Fecha de Creación: {self.fecha_creacion.strftime('%Y-%m-%d')}\n"
                f"  Origen: {self.origen}\n"
                f"  Marca: {self.marca}\n"
                f"  Tipo: {self.tipo}\n"
                f"  Número: {self.numero}\n"
                f"  Suela: {self.suela}\n"
                f"  Modelo: {self.modelo}\n"
                f"  Materiales: {', '.join(self.materiales)}\n"
                f"  Stocks: {self.stocks}")

# Ejemplo de uso:
fecha = datetime(2024, 9, 1)
calzado = Calzado(
    fecha_creacion=fecha,
    origen="España",
    marca="Nike",
    tipo="Deportivo",
    numero=42,
    suela="Goma",
    modelo="Air Max",
    materiales=["Cuero", "Malla", "Goma"],
    stocks=100
)

print(calzado)
