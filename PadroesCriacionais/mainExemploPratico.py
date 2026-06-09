import copy

class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

class Pizza:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def set_sabor(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __copy__(self):

        copia_nome = copy.copy(self.name)
        copia_ingredientes = copy.copy(self.ingredients)

        new = self.__class__(copia_nome, copia_ingredientes)
        new.__dict__.update(self.__dict__)
        return new
    
    def __deepcopy__(self, memo):
        
        if memo is None:
            memo = {}

        deep_copia_nome = copy.deepcopy(self.name, memo)
        deep_copia_ingredientes = copy.deepcopy(self.ingredients, memo)

        new = self.__class__(deep_copia_nome, deep_copia_ingredientes)
        new.__dict__.update(self.__dict__)
        return new  


class PedidoDelivery:
    def __init__(self, pizza, endereco):
        self.pizza = pizza
        self.endereco = endereco

    def __copy__(self):

        copia_pizza = copy.copy(self.pizza)
        copia_endereco = copy.copy(self.endereco)

        new = self.__class__(copia_pizza, copia_endereco)
        new.__dict__.update(self.__dict__)
        return new
    
    def __deepcopy__(self, memo):
        
        if memo is None:
            memo = {}

        deep_copia_pizza = copy.deepcopy(self.pizza, memo)
        deep_copia_endereco = copy.deepcopy(self.endereco, memo)

        new = self.__class__(deep_copia_pizza, deep_copia_endereco)
        new.__dict__.update(self.__dict__)
        return new  


if __name__ == "__main__":

    pizza1 = Pizza("Calabresa", ["calabresa", "queijo", "cebola"])
    pizza2 = copy.copy(pizza1)
    pizza3 = copy.deepcopy(pizza1)

    print(f"Pizza 1: {pizza1.name} - {pizza1.ingredients}")
    print(f"Pizza 2: {pizza2.name} - {pizza2.ingredients}")
    print(f"Pizza 3: {pizza3.name} - {pizza3.ingredients}")

    print("\nModificando a pizza 2...\n")

    pizza2.set_sabor("Mussarela", ["mussarela", "tomate", "orégano"])
    print(f"Pizza 1: {pizza1.name} - {pizza1.ingredients}")
    print(f"Pizza 2: {pizza2.name} - {pizza2.ingredients}")
    print(f"Pizza 3: {pizza3.name} - {pizza3.ingredients}")
    
    print("\nModificando a pizza 3...\n")

    pizza3.set_sabor("Frango com Catupiry", ["frango", "catupiry", "milho"])
    print(f"Pizza 1: {pizza1.name} - {pizza1.ingredients}")
    print(f"Pizza 2: {pizza2.name} - {pizza2.ingredients}")
    print(f"Pizza 3: {pizza3.name} - {pizza3.ingredients}")

    pedido1 = PedidoDelivery(pizza1, "Rua A, 123")
    print(f"\nPedido 1: Pizza - {pedido1.pizza.name}, Endereço - {pedido1.endereco}")
    
    pedido2 = copy.copy(pedido1)
    print(f"Pedido 2: Pizza - {pedido2.pizza.name}, Endereço - {pedido2.endereco}")

    pedido3 = copy.deepcopy(pedido1)
    print(f"Pedido 3: Pizza - {pedido3.pizza.name}, Endereço - {pedido3.endereco}")




