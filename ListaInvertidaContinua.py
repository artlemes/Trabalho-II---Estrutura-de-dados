from ListaInvertida import ListaInvertida


class ListaInvertidaContinua(ListaInvertida):
    def __init__(self):
        super().__init__()
    
    def buscaPorCategoria(self, sinal, valor):

        if sinal == "=":
            if valor not in super().getDict():
                return []
            
            return super().getDict()[valor]

        if sinal == ">":
            keyList = list(super().getDict().keys())

            for key in keyList:
                if not key > valor:
                    keyList.remove(key)
            
            returnList = []

            for key in keyList:
                for value in super().getDict()[key]:
                    returnList.append(value)
            
            return returnList
        
        if sinal == "<":
            keyList = list(super().getDict().keys())

            for key in keyList:
                if not key < valor:
                    keyList.remove(key)
            
            returnList = []

            for key in keyList:
                for value in super().getDict()[key]:
                    returnList.append(value)
            
            return returnList