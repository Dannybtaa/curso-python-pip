print("helo")


'''
tenia un error asi que busque entre el curso de github se soluciona asi:
1.CREAR LLAVES:

tener en cuenta que LAS LLAVES SON PARA CADA PC, 
no es buena idea compartir las llaves 

para ver que email tengo vinculado
git config -l

mi email de github
danielabetancur.arr@gmail.com

cambiar correo
git config --global user.email "correo@gmail.com"

conectamos la llave
ssh-keygen -t rsa -b 4096 -C "correo@gmail.com"

crea una contraseña si quieres ahi 

mirar si el servido de ssh funciona
eval $(ssh-agent -s)
debe aparecer algo asi
Agent pid  ####

agregar la llave
ssh-add ~/.ssh/id_rsa

en git hub vamos a:
settings
ssh and gpc

en ssh hey pegar la cavle publica que esta en el archivo id_rsa.pub

(como llegar a ese archivo, \\wsl$  vas a unbuntu y a tu home y alli esta el nombre de tu pc y por ahi debe estar la carpeta .ssh)

eso debe funcionar



1. git init

2. pego link de github

I M P O R T A N T E:
DEBES SER LA APRaTE QUE DICE SSH

git remote add origin git@github.com:Dannybtaa/curso-python-pip.git

3. verificamos con 
git remote -v

4. agragar cambio
git add * 

o usar 
git add .

5. commit
git commit -m "mi primer archivo"

6.git push origin master


para hacer los commits se debe estar en al carpeta ppal
salir de la carpeta:
cd .. 
´´´

CREAR UN AmbIENTE VIRTUAL

sudo apt install -y python3-venv

al entrar en al carpeta de la caul deseo el entorno virtual escribo

python3 -m venv env

ahora vemos que se crea la carpeta env/

activar el ambiente

source env/bin/activate

en la terminal aparece un indicativo env

para salir del ambiente virtual escribimos
deactivate

para saber si tengo el ambiente configurado enla carpeta se puede correr
which python3
which pip3


con pip freeze no dara repsuesta porque el ambiente estará aislado

# da las dependcias del proyecto
pip3 freeze

# vamos a crear un archivo txt para instalar las dependecias de manera automatica  y no mabual

requirements.txt

pip3 freeze > requirements.txt

# ver dentro de requirements

cat requirements.txt

para instalar se escribe

pip3 install -r requirements.txt


para correr docker en la carpeta deseada

1.construcciond el contenedor
docker-compose build

2.lanzar el contenedor
docker-compose up -d

3.ver el estadod el contenedor
docker-compose ps

ACA NOS APARECE EL NOMBRE ASI: app-web-server-1 
NAME               IMAGE            COMMAND                  SERVICE      CREATED          STATUS          PORTS
app-web-server-1   app-web-server   "/bin/sh -c 'bash -c…"   web-server   40 seconds ago   Up 39 seconds

EL NOMBRE ENTONCES SERIA SOLO: web-server

4.ingresar al ambienre
docker-compose exec NOMBREDELAMBIENTE  bash

docker-compose exec web-server bash

5.salir del conteneor 
exit


si me equivoco en algo y debo crearlo otra vez:
1.construcciond el contenedor
docker-compose build

2. bajar el contenedor anterior
docker-compose down

3.lanzar el contenedor
docker-compose up -d

4.ver el estadod el contenedor
docker-compose ps

5.ingresar al ambienre
docker-compose exec NOMBREDELAMBIENTE  bash

docker-compose exec web-server bash