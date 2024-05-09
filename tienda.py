from producto import Producto


class Tienda:
    def __init__(self, nombre: str, costo_delivery: int):
        self._nombre = nombre
        self._listado_productos_nombre = []
        self._listado_productos_precio = []
        self._listado_productos_stock = []
        self._costo_delivery = costo_delivery

    def agregar_producto(
        self, nombre_producto: str, precio_producto: int, stock_producto=0
    ):
        if nombre_producto not in self.listado_productos_nombre:
            self.nombre_producto = Producto(
                nombre_producto, precio_producto, stock_producto
            )
            self.listado_productos_nombre = self.nombre_producto.nombre
            self.listado_productos_precio = self.nombre_producto.precio
            self.listado_productos_stock = self.nombre_producto.stock
        else:
            index = self.listado_productos_nombre.index(nombre_producto)
            self.listado_productos_stock[index] = self.nombre_producto.actualizar_stock(
                stock_producto
            )

    def enlistar_productos(self):
        print(self.nombre)
        print("----------------------")
        for producto in range(len(self.listado_productos_nombre)):
            print(
                f"{self.listado_productos_nombre[producto]}: ${self.listado_productos_precio[producto]}"
            )

            if (
                self.nombre == "Farmacia"
                and self.listado_productos_precio[producto] > 15000
            ):
                print("***Envío gratis al solicitar este producto***")
                print("")

            if self.nombre != "Restaurante" and self.nombre != "Farmacia":
                if self.nombre == "Supermercado":
                    if self.listado_productos_stock[producto] < 10:
                        print("***Pocos productos disponibles***")
                    print(f"{self.listado_productos_stock[producto]} unidades en stock")
                else:
                    print(f"{self.listado_productos_stock[producto]} unidades en stock")
                print("")

    def realizacion_venta(self, producto: str, cantidad: int):
        index = self.listado_productos_nombre.index(producto)
        if self.nombre == "Restaurante":
            pass

        elif self.nombre == "Farmacia":
            if cantidad > 3:
                print("No se puede solicitar más de tres productos")
            else:
                self.listado_productos_stock[index] = (
                    self.nombre_producto.actualizar_stock(-cantidad)
                )

        else:
            self.listado_productos_stock[index] = self.nombre_producto.actualizar_stock(
                -cantidad
            )

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def listado_productos_nombre(self) -> set:
        return self._listado_productos_nombre

    @listado_productos_nombre.setter
    def listado_productos_nombre(self, value):
        self._listado_productos_nombre.append(value)

    @property
    def listado_productos_precio(self):
        return self._listado_productos_precio

    @listado_productos_precio.setter
    def listado_productos_precio(self, value):
        self._listado_productos_precio.append(value)

    @property
    def listado_productos_stock(self):
        return self._listado_productos_stock

    @listado_productos_stock.setter
    def listado_productos_stock(self, value):
        self._listado_productos_stock.append(value)

    @property
    def costo_delivery(self) -> int:
        return self._costo_delivery
