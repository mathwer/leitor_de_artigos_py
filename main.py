from bs4 import BeautifulSoup
import requests
import pyttsx3 as tts

url = input('Cole a url do site que você quer ler: ')

try:
    response = requests.get(url)

except:
    print('Não foi encontrado esse site, reveja o link')

text = response.text
site = BeautifulSoup(text, 'html.parser')

artigo = site.find_all(name='p')

# Da forma anterior, o tts falava /p no final de cada parágrafo.
strip = []
for par in artigo:
    par = par.getText().strip()
    strip.append(par)

engine = tts.init()
engine.say(strip)
engine.runAndWait()
