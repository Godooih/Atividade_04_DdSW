# Superclasse ItemBiblioteca
class ItemBiblioteca:
    def __init__(self, codigo, titulo):
        # define os itens comuns para todos os livros
        self._codigo = codigo
        self._titulo = titulo

    # Métodos Get
    def get_codigo(self):
        return self._codigo

    def get_titulo(self):
        return self._titulo

    def __str__(self):
        return f"Código: {self._codigo}, Título: {self._titulo}"

# Subclasse Livro herdando de ItemBiblioteca
class Livro(ItemBiblioteca):
    def __init__(self, codigo, titulo, autor, genero):
        super().__init__(codigo, titulo)  # está puxando essas caracteristicas da superclasse
        # adicionando mais itens
        self._autor = autor
        self._genero = genero

    # Métodos Get
    def get_autor(self):
        return self._autor

    def get_genero(self):
        return self._genero

    def __str__(self):
        return f"{super().__str__()}, Autor: {self._autor}, Gênero: {self._genero}"

# Subclasse Revista herdando de ItemBiblioteca
class Revista(ItemBiblioteca):
    def __init__(self, codigo, titulo, edicao, mesPublicacao):
        super().__init__(codigo, titulo)
        self._edicao = edicao
        self._mesPublicacao = mesPublicacao

    # Métodos Get
    def get_edicao(self):
        return self._edicao

    def get_mes_publicacao(self):
        return self._mesPublicacao

    def __str__(self):
        return f"{super().__str__()}, Edição: {self._edicao}, Mês de Publicação: {self._mesPublicacao}"

# Classe Biblioteca com associação simples de itens
class Biblioteca:
    def __init__(self, nome):
        self._nome = nome
        self._itensBiblioteca = []  # define uma lista vazia para armazenar os itens

    # Métodos Get
    def get_nome(self):
        return self._nome

    def get_itens_biblioteca(self):
        return self._itensBiblioteca

    def adicionarItem(self, item):
        self._itensBiblioteca.append(item)
        print(f"Item '{item.get_titulo()}' adicionado à biblioteca.")

    def removerItem(self, codigo):
        for item in self._itensBiblioteca:
            if item.get_codigo() == codigo:
                self._itensBiblioteca.remove(item)
                print(f"Item '{item.get_titulo()}' removido da biblioteca.")
                return
        print(f"Item com código {codigo} não encontrado.")

    def listarItens(self):
        if not self._itensBiblioteca:
            print("Nenhum item na biblioteca.")
        else:
            print("Itens na biblioteca:")
            for item in self._itensBiblioteca:
                print(item)

# Exemplo de uso
biblioteca = Biblioteca("Biblioteca Central")

# Criando itens
livro1 = Livro("001", "O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia")  # adicionando um livro
livro2 = Livro("002", "1984", "George Orwell", "Ficção Científica")
revista1 = Revista("003", "Revista Tecnologia", "Edição 5", "Outubro")  # adicionando uma revista

# Adicionando itens à biblioteca
biblioteca.adicionarItem(livro1)
biblioteca.adicionarItem(livro2)
biblioteca.adicionarItem(revista1)

# Listando itens da biblioteca
biblioteca.listarItens()

# Removendo um item da biblioteca
biblioteca.removerItem("002")

# Listando itens após remoção
biblioteca.listarItens()
