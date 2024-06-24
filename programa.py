from producto import Producto
from tienda import Restaurante, Supermercado, Farmacia

def main():
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante, Supermercado o Farmacia): ").lower()
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))
    
    if tipo_tienda == "restaurante":
        tienda = Restaurante(nombre_tienda, costo_delivery)
    elif tipo_tienda == "supermercado":
        tienda = Supermercado(nombre_tienda, costo_delivery)
    elif tipo_tienda == "farmacia":
        tienda = Farmacia(nombre_tienda, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return
    
    while True:
        opcion = input("\nSeleccione una opción:\n1. Ingresar producto\n2. Listar productos\n3. Realizar venta\n4. Salir\nOpción: ")
        
        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = float(input("Ingrese el precio del producto: "))
            stock_producto = int(input("Ingrese el stock del producto: "))
            producto = Producto(nombre_producto, precio_producto, stock_producto)
            tienda.ingresar_producto(producto)
        elif opcion == "2":
            print("Productos existentes:\n", tienda.listar_productos())
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            tienda.realizar_venta(nombre_producto, cantidad)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()