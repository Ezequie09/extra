# Clase Producto
class Producto:
    def __init__(self, id_producto:int,nombre: str, precio: float, cantidad: int):
       # Encapsulamiento
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    # Métodos getters para acceder a los atributos privados
    @property
    def nombre(self):
        return self.__nombre
    @property
    def precio(self):
        return self.__precio
    @property
    def cantidad(self):
        return self.__cantidad

    # Actualizar el inventario después de una venta
    def actualizar_inventario(self, cantidad_vendida: int):
        if cantidad_vendida <= 0:  # Manejo de errores
            raise ValueError("La cantidad vendida debe ser mayor a 0.")
        if cantidad_vendida > self.__cantidad:
            raise ValueError("Inventario insuficiente.")
        self.__cantidad -= cantidad_vendida
        return self.__cantidad


# Clase Cliente
class Cliente:
    def __init__(self,id_cliente: int, nombre: str, correo: str):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__correo = correo

    @property
    def nombre(self):
        return self.__nombre

    def realizar_compra(self):
        return f"Cliente {self.__nombre} está realizando una compra."


# Clase Pedidos
class Pedidos:
    def __init__(self, id_pedido: int):
        self.__id_pedido = id_pedido

    def imprimir_pedido(self):
        return f"Imprimiendo detalles del pedido ID: {self.__id_pedido}"


# Clase Informes (heredando de Pedidos)
class Informes(Pedidos):
    def __init__(self, id_orden: int, cliente: Cliente, producto: Producto):
        super().__init__(id_orden)  # Llamar al constructor de la clase base (Pedidos)
        self.__cliente = cliente
        self.__producto = producto
        self.__total = 0.0

    def calcular_total(self, cantidad: int):
        if cantidad <= 0:  # Manejo de errores
            raise ValueError("La cantidad debe ser mayor que 0.")
        self.__total = self.__producto.precio * cantidad
        return self.__total

    def generar_factura(self):
        factura = f"""
        --- Factura ---
        Orden ID: {self.__id_pedido}
        Cliente: {self.__cliente.nombre}
        Producto: {self.__producto.nombre}
        Total: ${self.__total:.2f}
        """
        return factura


# Clase ControlPedido
class ControlPedido:
    def __init__(self, id_pago: int, id_orden: str, metodo_pago: str):
        self.__id_pago = id_pago
        self.__id_orden = id_orden
        self.__metodo_pago = metodo_pago

    def procesar_pago(self):
        return f"Pago procesado para la orden {self.__id_orden} con método {self.__metodo_pago}"
