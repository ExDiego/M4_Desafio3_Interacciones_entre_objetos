from producto import Producto

class Tienda:
    def __init__(self, nombre_tienda, costo_delivery):
        self._nombre_tienda = nombre_tienda
        self._costo_delivery = costo_delivery
        self._productos = []
        
    def ingresar_producto(self, arg_producto):
        for prod in self._productos:
            if prod.obtener_nombre == arg_producto.obtener_nombre:
                prod.obtener_stock += arg_producto.obtener_stock
                break
        else:
            self._productos.append(arg_producto)

    def listar_productos(self):
        lista = ""
        for producto in self._productos:
            lista += str(producto) + "\n"
        return lista
    
    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self._productos:
            if producto.obtener_nombre == nombre_producto:
                if producto.obtener_stock < cantidad:
                    cantidad = producto.obtener_stock
                producto.obtener_stock -= cantidad
                break
                
class Restaurante(Tienda):
    pass

class Supermercado(Tienda):
    def listar_productos(self):
        lista_productos = ""
        for producto in self._productos:
            stock_info = f"Pocos productos disponibles ({producto.obtener_stock})" if producto.obtener_stock < 10 else ""
            lista_productos += f"Nombre: {producto.obtener_nombre}, Precio: ${producto.obtener_precio}, Stock: {producto.obtener_stock} {stock_info}\n"
        return lista_productos

class Farmacia(Tienda):
    def listar_productos(self):
        lista_productos = ""
        for producto in self._productos:
            envio_gratis = "Envío gratis al solicitar este producto" if producto.obtener_precio > 1500 else ""
            lista_productos += f"Nombre: {producto.obtener_nombre}, Precio: ${producto.obtener_precio}, Stock: {producto.obtener_stock} {envio_gratis}\n"
        return lista_productos
