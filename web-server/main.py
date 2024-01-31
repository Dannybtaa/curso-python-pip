import store

# intalar:
# pip3 install fastapi
# pip3 install "uvicorn[standard]"
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# creamos la instancia
app = FastAPI()

# sintaxis decorador, se le dice la ruta
@app.get('/')
def get_list():
    return [1,2,3,]

# otra ruta
# @app.get('/contact')

# retornar un html
@app.get('/contact', response_class=HTMLResponse)
def get_list():
    # return {'name': "platzi"}
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()

# ver la pagina fakeapi.platzi.com

# para correr esto se hace en la terminal
# uvicorn main:app --reload

# buscamos el localhost que nos indica en el navegador ami me dio
# http://localhost:8000/

