# Classe base Veículo - Representa um veículo genérico
class Veiculo:
    def __init__(self, placa, marca, tipo):
        self._placa = placa
        self._marca = marca
        self._tipo = tipo

    # Métodos Get
    def get_placa(self):
        return self._placa

    def get_marca(self):
        return self._marca

    def get_tipo(self):
        return self._tipo

    # Método para representar o veículo como string
    def __str__(self):
        return f"Placa: {self._placa}, Marca: {self._marca}, Tipo: {self._tipo}"

# Classe Carro herdando de Veículo
class Carro(Veiculo):
    def __init__(self, placa, marca, numportas):
        super().__init__(placa, marca, "Carro")
        self._numportas = numportas

    # Método Get
    def get_numportas(self):
        return self._numportas

    # Método para representar o carro como string
    def __str__(self):
        return f"{super().__str__()}, Número de Portas: {self._numportas}"

# Classe Caminhão herdando de Veículo
class Caminhao(Veiculo):
    def __init__(self, placa, marca, capacidadeCarga):
        super().__init__(placa, marca, "Caminhão")
        self._capacidadeCarga = capacidadeCarga

    # Método Get
    def get_capacidade_carga(self):
        return self._capacidadeCarga

    # Método para representar o caminhão como string
    def __str__(self):
        return f"{super().__str__()}, Capacidade de Carga: {self._capacidadeCarga} toneladas"

# Classe Motorista - utiliza agregação com a classe Veículo
class Motorista:
    def __init__(self, nome):
        self._nome = nome
        self._veiculos = []  # Lista de veículos, representando a agregação

    # Método para adicionar um veículo ao motorista
    def addVeiculo(self, veiculo):
        if isinstance(veiculo, Veiculo):
            self._veiculos.append(veiculo)
            print(f"Veículo '{veiculo.get_placa()}' adicionado ao motorista '{self._nome}'.")
        else:
            print("Erro: Somente instâncias da classe Veículo podem ser adicionadas.")

    # Método para remover um veículo do motorista pela placa
    def remVeiculo(self, placa):
        for veiculo in self._veiculos:
            if veiculo.get_placa() == placa:
                self._veiculos.remove(veiculo)
                print(f"Veículo com placa '{placa}' removido do motorista '{self._nome}'.")
                return
        print(f"Veículo com placa '{placa}' não encontrado para o motorista '{self._nome}'.")

    # Método para listar todos os veículos do motorista
    def listarVeiculos(self):
        if not self._veiculos:
            print(f"Motorista '{self._nome}' não possui veículos.")
        else:
            print(f"Veículos do motorista '{self._nome}':")
            for veiculo in self._veiculos:
                print(veiculo)

    # Método para representar o motorista como string
    def __str__(self):
        return f"Motorista: {self._nome}, Total de Veículos: {len(self._veiculos)}"

# Exemplo de uso
# Criando veículos
carro1 = Carro("ABC-1234", "Toyota", 4)
carro2 = Carro("XYZ-5678", "Honda", 2)
caminhao1 = Caminhao("DEF-9101", "Volvo", 12)

# Criando um motorista e associando veículos
motorista = Motorista("Carlos Silva")
motorista.addVeiculo(carro1)
motorista.addVeiculo(caminhao1)

# Listando os veículos do motorista
motorista.listarVeiculos()

# Adicionando mais um veículo
motorista.addVeiculo(carro2)

# Removendo um veículo do motorista
motorista.remVeiculo("ABC-1234")

# Listando novamente os veículos após remoção
motorista.listarVeiculos()