class Producto:
    def __init__(self, nombre: str, precio: int, stock=0):
        self._nombre = nombre
        self._precio = precio
        if stock < 0:
            self._stock = 0
        else:
            self._stock = stock
        
    def actualizar_stock(self, stock: int):
        if self._stock + stock < 0:
            return 0
        else:
            return self._stock + stock
        
    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        if self._stock > 0:
            return self._stock
        else:
            return 0

    @stock.setter
    def stock(self, value):
        if self._stock > 0:
            return self._stock
        else:
            return 0


# #En un archivo producto.py, definir la clase que permita instanciar productos.
# Considera para la definición de esta clase lo señalado en la descripción de la
# problemática (utilice ENCAPSULAMIENTO).
# (2 Puntos)
