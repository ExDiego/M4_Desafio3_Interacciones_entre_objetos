


class Producto:
    def __init__(self, nombre, precio, stock = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        
    @property
    def obtener_nombre(self):
        return self.__nombre
    
    @property
    def obtener_precio(self):
        return self.__precio
    
    @property
    def obtener_stock(self):
        return self.__stock
    
    @obtener_stock.setter
    def obtener_stock(self, cantidad):
        if cantidad < 0:
            self.__stock = 0
        else:
            self.__stock = cantidad
    
    
    def __str__(self):
        return f"Producto: {self.__nombre}       Precio{self.__precio}       stock: {self.__stock}"
    
    
    