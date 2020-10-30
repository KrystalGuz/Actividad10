from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
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

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

    @Slot()
    def action_abrir_archivo(self):
        #print('abrir_archivo')
        ubication = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.AlmacenP.abrir(ubication):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrio el archivo " + ubication
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Eror al abrir el archivo" + ubication
            )

    @Slot()
    def action_guardar_archivo(self):
        #print('Guardar_archivo')
        ubication = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubication)
        if self.AlmacenP.guardar(ubication):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubication
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo" + ubication
            )


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