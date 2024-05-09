from tienda import Tienda
from producto import Producto

restaurante = Tienda("Restaurante", 10000)
supermercado = Tienda("Supermercado", 20000)
farmacia = Tienda("Farmacia", 30000)

continuar = "si"

print(
    "Bienvenido a la prueba del proyecto de emprendimiento para la compra y reparto de productos."
)
print('Actualmente se tienen tres tiendas: "Restaurante", "Supermercado" y "Farmacia"')
print("")
print("Comencemos agregando los productos a las tiendas")

while continuar == "si":
    tienda_producto = input("Ingrese a que tienda pertenece el producto\n>").lower()
    nombre_producto = input("Ingrese el nombre del producto\n>")
    precio_producto = int(input("Ingrese el precio del producto\n>"))
    if tienda_producto != "restaurante":
        stock_producto = int(input("Ingrese el stock del producto\n>"))

    if tienda_producto == "restaurante":
        restaurante.agregar_producto(nombre_producto, precio_producto)
    elif tienda_producto == "supermercado":
        supermercado.agregar_producto(nombre_producto, precio_producto, stock_producto)
    elif tienda_producto == "farmacia":
        farmacia.agregar_producto(nombre_producto, precio_producto, stock_producto)

    continuar = input("¿Deseas continuar agregando productos? (Si/No)\n>").lower()

continuar = "si"

while continuar == "si":
    print("Muy bien, ¿ahora que deseas realizar?")
    print("1: Listar los productos existentes")
    print("2: Realizar una venta")
    print("3: Salir del programa")
    opcion = input(">")

    if opcion == "1":
        restaurante.enlistar_productos()
        print("")
        supermercado.enlistar_productos()
        print("")
        farmacia.enlistar_productos()

    elif opcion == "2":
        tienda_producto = input(
            "Ingrese en que tienda quiere realizar la venta\n>"
        ).lower()
        if tienda_producto == "restaurante":
            print("")
            print("Los productos son los siguientes:")
            restaurante.enlistar_productos()
            producto_vendido = input("Escriba que producto quiere vender:\n>")
            restaurante.realizacion_venta(producto_vendido, 0)

        elif tienda_producto == "supermercado":
            print("")
            print("Los productos son los siguientes:")
            supermercado.enlistar_productos()
            producto_vendido = input("Escriba que producto quiere vender:\n>")
            cantidad_vendida = int(input("Ingrese la cantidad que será vendida:\n>"))
            supermercado.realizacion_venta(producto_vendido, cantidad_vendida)

        elif tienda_producto == "farmacia":
            print("")
            print("Los productos son los siguientes:")
            farmacia.enlistar_productos()
            producto_vendido = input("Escriba que producto quiere vender:\n>")
            cantidad_vendida = int(input(
                "Ingrese la cantidad que será vendida, recuerde que el máximo es 3:\n>"
            ))
            farmacia.realizacion_venta(producto_vendido, cantidad_vendida)

    elif opcion == "3":
        print("Gracias por usar el programa")
        break

    continuar = input("¿Deseas realizar otra operación? (Si/No)\n>").lower()
