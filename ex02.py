# Classe Prato - representa um prato com nome e preço
class Prato:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    # Métodos Get
    def get_nome(self):
        return self._nome

    def get_preco(self):
        return self._preco

    # Método para representar o prato como string
    def __str__(self):
        return f"Prato: {self._nome}, Preço: R${self._preco:.2f}"

# Classe Pedido - usa composição, pois contém instâncias de Prato
class Pedido:
    def __init__(self, numPedido):
        self._numPedido = numPedido
        self._pratos = []  # Lista de pratos, representando a composição

    # Método para adicionar um prato ao pedido
    def addPrato(self, prato):
        if isinstance(prato, Prato):
            self._pratos.append(prato)
            print(f"Prato '{prato.get_nome()}' adicionado ao pedido {self._numPedido}.")
        else:
            print("Erro: Somente instâncias da classe Prato podem ser adicionadas.")

    # Método para remover um prato do pedido pelo nome
    def remPrato(self, nome_prato):
        for prato in self._pratos:
            if prato.get_nome() == nome_prato:
                self._pratos.remove(prato)
                print(f"Prato '{nome_prato}' removido do pedido {self._numPedido}.")
                return
        print(f"Prato '{nome_prato}' não encontrado no pedido {self._numPedido}.")

    # Método para calcular o total do pedido
    def calcularTotal(self):
        return sum(prato.get_preco() for prato in self._pratos)

    # Método para representar o pedido como string
    def __str__(self):
        pratos_str = ', '.join([prato.get_nome() for prato in self._pratos])
        total = self.calcularTotal()
        return f"Pedido {self._numPedido}: Pratos: [{pratos_str}], Total: R${total:.2f}"

# Classe Cliente - usa agregação, pois contém instâncias de Pedido
class Cliente:
    def __init__(self, nome):
        self._nome = nome
        self._pedidos = []  # Lista de pedidos, representando a agregação

    # Método para adicionar um pedido ao cliente
    def addPedido(self, pedido):
        if isinstance(pedido, Pedido):
            self._pedidos.append(pedido)
            print(f"Pedido {pedido._numPedido} adicionado ao cliente '{self._nome}'.")
        else:
            print("Erro: Somente instâncias da classe Pedido podem ser adicionadas.")

    # Método para remover um pedido do cliente pelo número do pedido
    def remPedido(self, num_pedido):
        for pedido in self._pedidos:
            if pedido._numPedido == num_pedido:
                self._pedidos.remove(pedido)
                print(f"Pedido {num_pedido} removido do cliente '{self._nome}'.")
                return
        print(f"Pedido {num_pedido} não encontrado para o cliente '{self._nome}'.")

    # Método para listar todos os pedidos do cliente
    def listarPedidos(self):
        if not self._pedidos:
            print(f"Cliente '{self._nome}' não possui pedidos.")
        else:
            print(f"Pedidos do cliente '{self._nome}':")
            for pedido in self._pedidos:
                print(pedido)

    # Método para representar o cliente como string
    def __str__(self):
        return f"Cliente: {self._nome}, Total de Pedidos: {len(self._pedidos)}"

# Exemplo de uso
# Criando pratos
prato1 = Prato("Lasanha", 25.90)
prato2 = Prato("Pizza Margherita", 32.50)
prato3 = Prato("Salada Caesar", 18.20)

# Criando um pedido
pedido1 = Pedido(101)
pedido1.addPrato(prato1)
pedido1.addPrato(prato2)
pedido1.addPrato(prato3)

# Criando outro pedido
pedido2 = Pedido(102)
pedido2.addPrato(prato3)
pedido2.addPrato(prato2)

# Criando um cliente e associando pedidos
cliente = Cliente("João Silva")
cliente.addPedido(pedido1)
cliente.addPedido(pedido2)

# Listando os pedidos do cliente
cliente.listarPedidos()

# Removendo um pedido do cliente
cliente.remPedido(101)

# Listando novamente os pedidos após remoção
cliente.listarPedidos()
    