from Particulas import Particula

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