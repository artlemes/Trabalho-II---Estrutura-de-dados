

class ListaInvertida:
    def __init__(self):
        self.__dict = {}

    def incluir(self, categoria, id: int):
        if categoria not in dict:
            self.__dict[categoria] = []
        
        if id not in self.__dict[categoria]:
            self.__dict[categoria].append(id)

    def remover(self, categoria, id: int):
        if categoria not in dict:
            return

        if id not in self.__dict[categoria]:
            return

        self.__dict[categoria].remove(id)
    
    def buscaPorCategoria(self, categoria):
        if categoria not in dict:
            return []
        
        return self.__dict[categoria]