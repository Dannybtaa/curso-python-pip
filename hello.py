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