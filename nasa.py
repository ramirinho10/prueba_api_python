import requests
import json
from string import Template

url_nasa = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=25&api_key=DEMO_KEY'
headers = {}
payload = {}

def request_get(url):
    return json.loads(requests.get(url).text)

response = request_get(url_nasa)

lista = response['photos'][0:25]

fotos = []

for i in lista: 
    for k,v in i.items():
        if k == "img_src":
            fotos.append(v)


img_template = Template('<img src="$url" width="300" height="300">')
imagen = img_template.substitute(url = 'Hola')

html_template = Template('''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prueba Api - Ramiro Silva</title>
    <link rel="stylesheet" href="./style.css">
</head>
<body>
    <h1>Prueba API - FOTOS MARS ROVERS</h1>
    $body
    <footer>
        <p>Todos los derechos reservados</p>
    </footer>
</body>
</html>
                        ''')

print(html_template.substitute(body = imagen))

texto_img = ''

for url in fotos:
    texto_img += '\t' + img_template.substitute(url = url) + '\n'

print(texto_img)

html = html_template.substitute(body = texto_img)
print(html)

with open('output.html', 'w') as f:
    f.write(html)

