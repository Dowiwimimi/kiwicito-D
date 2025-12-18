# =========================================
# Ejemplo del Mundo Real usando POO
# Sistema básico de una Tienda
# =========================================

# Clase Producto
class Producto:
    def __init__(self, nombre, precio):
        # Atributos del producto
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        # Método para mostrar la información del producto
        print(f"Producto: {self.nombre} | Precio: ${self.precio}")


# Clase Cliente
class Cliente:
    def __init__(self, nombre):
        # Atributo del cliente
        self.nombre = nombre
        self.carrito = []  # Lista de productos comprados

    def agregar_producto(self, producto):
        # Método para agregar un producto al carrito
        self.carrito.append(producto)
        print(f"{producto.nombre} agregado al carrito de {self.nombre}")

    def total_compra(self):
        # Calcula el total a pagar
        total = 0
        for producto in self.carrito:
            total += producto.precio
        return total


# Clase Tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        # Agrega productos disponibles en la tienda
        self.productos.append(producto)

    def mostrar_productos(self):
        # Muestra los productos disponibles
        print(f"\nProductos disponibles en {self.nombre}:")
        for producto in self.productos:
            producto.mostrar_info()


# ==========================
# Uso del sistema
# ==========================

# Crear tienda
tienda = Tienda("Tienda Virtual")

# Crear productos
producto1 = Producto("Camiseta", 15)
producto2 = Producto("Pantalón", 25)

# Agregar productos a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

# Mostrar productos disponibles
tienda.mostrar_productos()

# Crear cliente
cliente = Cliente("Ana")

# Cliente compra productos
cliente.agregar_producto(producto1)
cliente.agregar_producto(producto2)

# Mostrar total de la compra
print(f"\nTotal a pagar por {cliente.nombre}: ${cliente.total_compra()}")
