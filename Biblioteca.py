from Livro import Livro
from ListaInvertida import ListaInvertida
from ListaInvertidaContinua import ListaInvertidaContinua

class Biblioteca():

    def __init__(self):
        self.__estante = {}
        self.__listaInvertidaGenero = ListaInvertida()
        self.__listaInvertidaAutor = ListaInvertida()
        self.__listaInvertidaPreco = ListaInvertidaContinua()
    
    # Inclui um livro novo a biblioteca.
    def incluirLivro(self, id: int, nome: str, genero: str, autor: str, preco: int):

        for identificador in self.__estante:
            livro = self.__estante[identificador]
            if identificador == id:
                print(f"Livro de nome '{livro.getNome()}' já tem este id, inclusão de '{nome}' falhou.")
                return None

        livroNovo = Livro(id, nome, genero, autor, preco)
        
        self.__estante[id] = livroNovo

        self.__listaInvertidaGenero.incluir(livroNovo.getGenero(), id)
        self.__listaInvertidaAutor.incluir(livroNovo.getAutor(), id)
        self.__listaInvertidaPreco.incluir(livroNovo.getPreco(), id)

    # Busca um único livro pelo seu identificador único (ID)
    def buscarPorId(self, id):

        for identificador in self.__estante:
            livro = self.__estante[identificador]

            if identificador == id:
                return livro
        
        return None
    
    # Remover um único livro pelo seu identificar único (ID)
    def removerPorId(self, id):

        livro = self.buscarPorId(id)

        self.__listaInvertidaGenero.remover(livro.getGenero(), id)
        self.__listaInvertidaAutor.remover(livro.getAutor(), id)
        self.__listaInvertidaPreco.remover(livro.getPreco(), id)

        self.__estante.pop(id)

    # Busca todos os IDs (identificadores únicos) de livros com os parâmetros informados
    def buscaPorCategoria(self, genero = None, autor = None, precoCompLogica = None, precoValor = None):

        if precoCompLogica == None and precoValor != None:
            precoCompLogica = "="

        listaRetorno = set()

        listaDeIdPorGenero = self.__listaInvertidaGenero.buscaPorCategoria(genero)
        listaDeIdPorAutor = self.__listaInvertidaAutor.buscaPorCategoria(autor)
        listaDeIdPorPreco = self.__listaInvertidaPreco.buscaPorCategoria(precoCompLogica, precoValor)

        if genero != None:
            listaRetorno = listaRetorno | set(listaDeIdPorGenero)
        
        if autor != None:
            if genero != None:
                listaRetorno = listaRetorno & set(listaDeIdPorAutor)
            else:
                listaRetorno = listaRetorno | set(listaDeIdPorAutor)
        
        if precoValor != None:
            if genero != None or autor != None:
                listaRetorno = listaRetorno & set(listaDeIdPorPreco)
            else:
                listaRetorno = listaRetorno | set(listaDeIdPorPreco)
        
        return list(listaRetorno)

    # Mostra todos os livros da bibliotéca
    def exibirTodosDados(self):
        print(self.__estante)
