#imports
import requests
from termcolor import colored

#Request to web
urlOficial = "https://api-dolar-argentina.herokuapp.com/api/dolaroficial"
urlBlue = "https://api-dolar-argentina.herokuapp.com/api/dolarblue"
#global variables
reqOficial = requests.get(urlOficial)
data = reqOficial.json()
ventaIniOficial = reqOficial.json()['venta']
#function refresh
def refreshDolar():
    resp = requests.get(urlOficial)
    data = resp.json()
    return data;
while True:
    if data['venta'] > ventaIniOficial:
        print(colored('Dolar Oficial: \n Compra: ' + str(data['compra']) + ' Venta: ' + str(data['venta']) , 'green'))
        data = refreshDolar()
    if data['venta'] < ventaIniOficial:
        print(colored('Dolar Oficial: \n Compra: ' + str(data['compra']) + ' Venta: ' + str(data['venta']), 'red'))
        data = refreshDolar()
    if data['venta'] == ventaIniOficial:
        print('Dolar Oficial: \n Compra: ' + str(data['compra']) + ' Venta: ' + str(data['venta']) + ' Sec: ' + str(data['fecha'])[-2] + str(data['fecha'])[-1])
        data = refreshDolar()