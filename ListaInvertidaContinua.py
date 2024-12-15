from ListaInvertida import ListaInvertida


class ListaInvertidaContinua(ListaInvertida):
    def __init__(self):
        super().__init__()
    
    def buscaPorCategoria(self, sinal, valor):

        if sinal == "=":
            if valor not in self.__dict:
                return []
            
            return self.__dict[valor]

        if sinal == ">":
            keyList = self.__dict.keys()

            for key in keyList:
                if not key > valor:
                    keyList.remove(key)
            
            returnList = []

            for key in keyList:
                for value in self.__dict[key]:
                    returnList.append(value)
            
            return returnList
        
        if sinal == "<":
            keyList = self.__dict.keys()

            for key in keyList:
                if not key < valor:
                    keyList.remove(key)
            
            returnList = []

            for key in keyList:
                for value in self.__dict[key]:
                    returnList.append(value)
            
            return returnList