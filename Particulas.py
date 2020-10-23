class Particula:
    def __init__(self, Id=0, OrigenX=0, OrigenY=0, DestinoX=0, DestinoY=0, Velocidad=0, Red=0, Green=0, Blue=0):
        self.__Id = Id
        self.__OrigenX = OrigenX
        self.__OrigenY = OrigenY
        self.__DestinoX = DestinoX
        self.__DestinoY = DestinoY
        self.__Velocidad = Velocidad
        self.__Red = Red
        self.__Green = Green
        self.__Blue = Blue
    
    def __str__(self):
        return (
            'Id: ' + str(self.__Id) + '\n' +
            'Origen en X: ' + str(self.__OrigenX) + '\n' +
            'Origen en Y: ' + str(self.__OrigenY) + '\n' +
            'Destino en X: ' + str(self.__DestinoX) + '\n' +
            'Destino en Y: ' + str(self.__DestinoY) + '\n' +
            'Velocidad: ' + str(self.__Velocidad) + '\n' +
            'Red: ' + str(self.__Red) + '\n' +
            'Green: ' + str(self.__Green) + '\n' +
            'Blue: ' + str(self.__Blue) + '\n'
        )