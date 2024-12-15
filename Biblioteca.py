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
                return None

        livroNovo = Livro(id, nome, genero, autor, preco)
        
        self.__estante[id] = livroNovo

        self.__listaInvertidaAutor.incluir(livroNovo.getAutor(), id)
        self.__listaInvertidaGenero.incluir(livroNovo.getGenero(), id)
        self.__listaInvertidaPreco.incluir(livroNovo.getPreco(), id)

    def buscarPorId(self, id):

        for identificador, livro in self.__estante:

            if identificador == id:
                return livro
        
        return None
    
    def removerPorId(self, id):

        livro = self.buscarPorId(id)

        self.__listaInvertidaAutor.remover(livro.getAutor(), id)
        self.__listaInvertidaGenero.remover(livro.getGenero(), id)
        self.__listaInvertidaPreco.remover(livro.getPreco(), id)

        self.__estante.pop(id)
        
    def exibirTodosDados(self):
        print(self.__estante)
