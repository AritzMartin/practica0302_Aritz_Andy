class Pedido(Producto):
    def __int__(self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades
        return
    def total_pedido(self):
        return