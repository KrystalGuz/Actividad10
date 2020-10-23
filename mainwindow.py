from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from AlmacenP import AlmacenDeParticulas
from Particulas import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.AlmacenP = AlmacenDeParticulas()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.AgregarFinal.clicked.connect(self.click_agregar)
        self.ui.AgregarInicio.clicked.connect(self.click_agregarInicio)
        self.ui.Mostrar.clicked.connect(self.click_mostrar)

    @Slot()
    def click_mostrar(self):
        #self.AlmacenP.mostrar()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.AlmacenP))
    
    @Slot()
    def click_agregar(self):
        Id = self.ui.Id_spinBox.value()
        OrigenX = self.ui.OrigenX_spinBox.value()
        OrigenY = self.ui.OrigenY_spinBox.value()
        DestinoX = self.ui.DestinoX_spinBox.value()
        DestinoY = self.ui.DestinoY_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Blue = self.ui.Blue_spinBox.value()

        Particulas = Particula(Id, OrigenX, OrigenY, DestinoX, DestinoY, Velocidad, Red, Green, Blue)
        self.AlmacenP.agregar_final(Particulas)

        # print(Id, OrigenX, OrigenY, DestinoX, DestinoY, Velocidad, Red, Green, Blue)
        # self.ui.plainTextEdit.insertPlainText(str(Id) + str(OrigenX) + str(OrigenY) + str(DestinoX) + str(DestinoY) + str(Velocidad) + str(Red) + str(Green) + str(Blue))
        
    @Slot()
    def click_agregarInicio(self):
        Id = self.ui.Id_spinBox.value()
        OrigenX = self.ui.OrigenX_spinBox.value()
        OrigenY = self.ui.OrigenY_spinBox.value()
        DestinoX = self.ui.DestinoX_spinBox.value()
        DestinoY = self.ui.DestinoY_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Blue = self.ui.Blue_spinBox.value()

        Particulas = Particula(Id, OrigenX, OrigenY, DestinoX, DestinoY, Velocidad, Red, Green, Blue)
        self.AlmacenP.agregar_inicio(Particulas)