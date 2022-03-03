import requests
from . import API_KEY, URL_TASA_ESPECIFICA
from criptos.errors import APIError



class CriptoValorModel:
    def __init__(self,origen: str, destino: str):
        self.origen = origen
        self.destino = destino

        self.tasa = 0.0
    
    def obtenerTasa(self):
        self.respuesta = requests.get(URL_TASA_ESPECIFICA.format(self.origen, self.destino, API_KEY))

        if self.respuesta.status_code != 200:
            raise APIError(self.respuesta.json()["error"])
        
        self.tasa = round(self.respuesta.json()["rate"],2)
        