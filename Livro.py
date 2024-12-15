class Livro:
    def __init__(self, id: int, nome: str, genero: str, autor: str, preco: int):
        if not isinstance(id, int):
            raise TypeError("O 'id' deve ser um inteiro.")
        if not isinstance(nome, str):
            raise TypeError("O 'nome' deve ser uma string.")
        if not isinstance(genero, str):
            raise TypeError("O 'genero' deve ser uma string.")
        if not isinstance(autor, str):
            raise TypeError("O 'autor' deve ser uma string.")
        if not isinstance(preco, int):
            raise TypeError("O 'preco' deve ser um inteiro.")

        self.__id = id
        self.__nome = nome
        self.__genero = genero
        self.__autor = autor
        self.__preco = preco

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def setNome(self, nome: str):
        if not isinstance(nome, str):
            raise TypeError("O 'nome' deve ser uma string.")
        self.__nome = nome

    def getGenero(self):
        return self.__genero

    def setGenero(self, genero: str):
        if not isinstance(genero, str):
            raise TypeError("O 'genero' deve ser uma string.")
        self.__genero = genero

    def getAutor(self):
        return self.__autor

    def setAutor(self, autor: str):
        if not isinstance(autor, str):
            raise TypeError("O 'autor' deve ser uma string.")
        self.__autor = autor

    def getPreco(self):
        return self.__preco

    def setPreco(self, preco: int):
        if not isinstance(preco, int):
            raise TypeError("O 'preco' deve ser um inteiro.")
        self.__preco = preco