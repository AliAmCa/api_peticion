from criptos.models import CriptoValorModel
from criptos.view import CriptoValorView


class CriptoValorController:
    def __init__(self):
        
        self.vista = CriptoValorView()
        self.modelo = CriptoValorModel()

    
    def ejecutar(self):
        self.vista.pedir()
        self.modelo.origen = self.vista.origen
        self.modelo.destino = self.vista.destino
        self.modelo.obtenerTasa()

        self.vista.mostrar(self.modelo.tasa)