import requests
from . import  URL_TASA_ESPECIFICA
from criptos.errors import APIError
from criptos.config import API_KEY



class CriptoValorModel:
    def __init__(self,apikey, origen = "", destino = ""):
        self.apikey = apikey
        self.origen = origen
        self.destino = destino

        self.tasa = 0.0
    
    def obtenerTasa(self):
        respuesta = requests.get(URL_TASA_ESPECIFICA.format(self.origen, self.destino, self.apikey))

        if respuesta.status_code != 200:
            raise APIError(respuesta.status_code, respuesta.json()["error"])
         
        self.tasa = round(respuesta.json()["rate"],2)
        