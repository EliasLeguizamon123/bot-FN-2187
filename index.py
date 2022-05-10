#imports
#!/user/bin/env python3
import requests
from termcolor import colored
from bs4 import BeautifulSoup
from time import sleep
#get link of the page and text values
url = requests.get('https://www.cronista.com/MercadosOnline/dolar.html')
soup = BeautifulSoup(url.text, 'html.parser')
# get the values of the page
def getDolar():
    resp = requests.get('https://www.cronista.com/MercadosOnline/dolar.html')
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup
# while loop to refresh the values
while True:
    valores = soup.find_all('tr')    
    for valor in valores:
            #set values of BNA Blue and MEP
            if "BNA" in valor.a.text or "BLUE" in valor.a.text or "MEP" in valor.a.text:
                venta = valor.find('div', class_='sell-value').text
                compra = valor.find('div', class_='buy-value').text
                print(valor.a.text)
                print(colored('Venta: ' + venta, 'green') + '\n' + colored('Compra: ' + compra, 'red'))
                soup = getDolar()
                continue
    sleep(5)