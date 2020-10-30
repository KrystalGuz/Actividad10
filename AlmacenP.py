from Particulas import Particula
import json

class AlmacenDeParticulas:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self, Particulas:Particula):
        self.__particulas.append(Particulas)

    def agregar_inicio(self, Particulas:Particula):
        self.__particulas.insert(0, Particulas)

    def mostrar(self):
        for Particulas in self.__particulas:
            print(Particulas)

    def __str__(self):
        return "".join(
            str(Particulas) + '\n'for Particulas in self.__particulas
            
        )
    
    def guardar(self, ubication):
        try:
            with open(ubication, 'w') as archivo:
                lista = [Particulas.to_dict() for Particulas in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 
            
    def abrir(self, ubication):
        try:
            with open(ubication, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**Particulas) for Particulas in lista]
            return 1
        except:
            return 0