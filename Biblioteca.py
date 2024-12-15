from Livro import Livro

class Biblioteca():

    def __init__(self):
        self.__estante = {}
    """ self.__listaInvertidaGenero = ListaInvertida()
        self.__listaInvertidaAutor = ListaInvertida()
        self.__listaInvertidaPreco = ListaInvertida()
    """
    def incluirLivro(self, id: int, nome: str, genero: str, autor: str, preco: int):

        repetido = False

        for identificador, livro in self.__estante:
            if identificador == id:
                repetido = True
        
        if not repetido:

            novo = Livro(id, nome, genero, autor, preco)

            self.__estante[id] = novo
        else:
            print("Livro repetido, não pode ser incluido")