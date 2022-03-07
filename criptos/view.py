from criptos import MONEDAS


class CriptoValorView:
    def __init__(self):
        self.origen = ""
        self.destino = ""

    def pedir(self):
        origen = input("Moneda origen: ")
        while origen not in MONEDAS:
            print ("La moneda debe ser una de las siguientes:")
            print(",".join(MONEDAS))
            origen = input("Moneda origen: ")

        self.origen = origen
        destino = input("Moneda a convertir: ")
        while destino not in MONEDAS:
            print ("La moneda debe ser una de las siguientes:")
            print(", ".join(MONEDAS))
            destino = input("Moneda origen: ")

        self.destino = destino

    def mostrar(self, tasa):
        print(f"1 {self.origen} son {tasa:.2f} {self.destino}")

    def mostrarError(self,error):
        if error[0] == 401:
            print("API KEY inválida ")
        else:
            print(error[1])