import requests

endpoint = "https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey=E01CCF95-56F6-42CD-9ABA-67E8380016F1"

moneda_from = input("Moneda de origen: ")

moneda_to = input("Moneda a conseguir: ")

r = requests.get(endpoint.format(moneda_from, moneda_to))

print(round(r.json()["rate"],2))