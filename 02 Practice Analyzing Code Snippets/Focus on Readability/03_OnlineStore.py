class Product:
    """Representa un producto con nombre, precio y cantidad disponible."""
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def purchase(self, quantity):
        """Reduce el stock cuando se realiza una compra."""
        if quantity > self.stock:
            print(f"Stock insuficiente de {self.name}.")
            return False
        self.stock -= quantity
        print(f"Has comprado {quantity} unidades de {self.name}.")
        return True

class ShoppingCart:
    """Simula un carrito de compras."""
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        """Añade un producto al carrito."""
        if product.purchase(quantity):
            self.items.append((product, quantity))

    def checkout(self):
        """Finaliza la compra mostrando los productos adquiridos."""
        print("Resumen de compra:")
        for product, quantity in self.items:
            print(f"{product.name}: {quantity} unidades - Total: ${product.price * quantity:.2f}")

# Productos disponibles
products = [
    Product("Laptop", 1200.99, 10),
    Product("Teclado", 35.50, 50),
    Product("Mouse", 25.00, 30)
]

# Simulación de compra
cart = ShoppingCart()
cart.add_to_cart(products[0], 1)
cart.add_to_cart(products[1], 2)
cart.checkout()
