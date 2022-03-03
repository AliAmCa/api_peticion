from criptos.models  import CriptoValorModel
from criptos.view import CriptoValorView
from criptos.errors import APIError

vista = CriptoValorView()
vista.pedir()


cvm = CriptoValorModel(vista.origen, vista.destino)

try:
    cvm.obtenerTasa()
    print(cvm.tasa)

except APIError:
    print("No se puede calcular la tasa")