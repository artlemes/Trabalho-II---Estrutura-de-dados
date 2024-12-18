

class ListaInvertida:
    def __init__(self):
        self.__dict = {}
    
    def getDict(self):
        return self.__dict

    def incluir(self, categoria, id: int):
        if categoria not in self.__dict:
            self.__dict[categoria] = []
        
        if id not in self.__dict[categoria]:
            self.__dict[categoria].append(id)

    def remover(self, categoria, id: int):
        if categoria not in self.__dict:
            return None

        if id not in self.__dict[categoria]:
            return None

        self.__dict[categoria].remove(id)
    
    def buscaPorCategoria(self, categoria):
        if categoria not in self.__dict:
            return []
        
        return self.__dict[categoria]