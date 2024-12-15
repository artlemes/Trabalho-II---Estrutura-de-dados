from Livro import Livro
from ListaInvertida import ListaInvertida
from ListaInvertidaContinua import ListaInvertidaContinua

class Biblioteca():

    def __init__(self):
        self.__estante = {}
        self.__listaInvertidaGenero = ListaInvertida()
        self.__listaInvertidaAutor = ListaInvertida()
        self.__listaInvertidaPreco = ListaInvertidaContinua()
    
    def incluirLivro(self, id: int, nome: str, genero: str, autor: str, preco: int):

        for identificador, livro in self.__estante:
            if identificador == id:
                print("Livro repetido, não pode ser incluido")
                return

        novo = Livro(id, nome, genero, autor, preco)
        self.__estante[id] = novo

    def buscarPorId(self, id):

        for identificador, livro in self.__estante:

            if identificador == id:
                return livro
        
        return None
    
    def remover(self, id):

        genero = None
        autor = None
        preco = None

        for identificador, livro in self.__estante:

            if identificador == id:

                livro = self.__estante[id]

                genero = livro.getGenero()
                autor = livro.getAutor()
                preco = livro.getPreco()

                self.__estante.pop(id)

        self.__listaInvertidaAutor.remover(autor, id)
        self.__listaInvertidaGenero.remover(genero, id)
        self.__listaInvertidaPreco.remover(preco, id)
        
    def exibirTodosDados(self):
        print(self.__estante)
