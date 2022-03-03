import requests

respuesta = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC?apikey=E01CCF95-56F6-42CD-9ABA-67E8380016F1")

print (respuesta.status_code)
data = respuesta.json()

print(data["rates"][3]["rate"])
