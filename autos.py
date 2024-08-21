# crear una clase fabrica que tenga los atributos llantas, color y precio; Luego crear 2 clases mas que hereden de fabrica las cuales son moto y carro.
# crear metodos que muestren la cantidad de llantas, color y precios de cada transporte. 
# Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_info(self):
        print(f"Llantas: {self.llantas}, Color: {self.color}, Precio: {self.precio}")

    def aplicar_descuento(self):
        if self.precio > 100000:
            descuento = self.precio * 0.10
            precio_con_descuento = self.precio - descuento
            return precio_con_descuento
        elif self.precio<100000:
            print("El producto no alcanza el valor de 100.000. Por ende, no se aplica el descuento. ")

class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(2, color, precio)

class Auto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(4, color, precio)

# Crear objetos
moto = Moto("Rojo", 1500)
auto = Auto("Azul", 250000)  # Cambié el precio a 250,000 para mostrar el descuento

# Mostrar información y precios con descuento si aplican
print("Información de la moto:")
moto.mostrar_info()
print(f"Precio con descuento: {moto.aplicar_descuento()}")

print("\nInformación del carro:")
auto.mostrar_info()
print(f"Precio con descuento: {auto.aplicar_descuento()}")
