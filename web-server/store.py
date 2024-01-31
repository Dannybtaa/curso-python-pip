import requests

def get_categories():
    # direccion de donde queremos hacer la solicitud
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    # pedimos el estado
    print(r.status_code)
    print(r.text)
    # pedimos ver que tipo es
    print(type(r.text))
    # convertirlo a un formato Json, para iterar con estos diccionarios
    categories = r.json()
    for category in categories:
        print(category['name'])