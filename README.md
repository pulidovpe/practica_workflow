# practica_workflow

## Hora de ordenar la chuleta
## Comandos GIT importantes:

- Para ver el estado del proyecto (archivos modificados o nuevos)
```Shell
git status
```

- Para agregar un nuevo archivo, o uno modificado
```Shell
git add archivo.txt
```
- Para agregar varios archivos...
```Shell
git add archivo.txt carpeta/otro_archivo.txt otra_carpeta/otro_archivo.txt
```
- Para agregar todos los archivos del proyecto
```Shell
git add -A

git add --all
```

- Para ver diferencias en un archivo modificado comparando con su versión anterior
```Shell
git diff --staged
```

- Para dar informacion acerca del/los cambio(s) realizado(s)
```Shell
git commit -m "Agregué una lista de comandos git"
```
- Para ver información de los commits hechos
```Shell
git log

git log --name-status
```

- Para bajar cambios de la rama master del repositorio remoto
```Shell
git pull origin master
```
- Para subir cambios a la rama master del repositorio remoto
```Shell
git push origin master
```

- Guardar cambios locales en una "stage" aparte
```Shell
git stash
```
- Para recuperar los cambios guardados en el "stage"
```Shell
git stash apply
```


## En este archivo empezaremos la práctica. 

<<<<<<< HEAD
<<<<<<< HEAD
Rama de Francisco
=======
Rama de Abraham
>>>>>>> rama-abraham

Ahora iniciaremos con el uso de las "branch". O, Ramas.

Lo primero que debemos hacer, es aprender que no solo con git pull
se pueden bajar los cambios actuales de un repositorio.
Pueden bajar cambios de master o de otra rama. Por ejemplo: develop
O el nombre que le haya dado su lider de equipo.

- Para saber que ramas existen en el origin y en tu local. Y en cual estas!
```Shell
git branch -av
```
<<<<<<< HEAD

- Para bajar lo ultimo de una rama, modificando tu "stage"
O sea, tus archivos seran actualizados.
```Shell
git pull origin rama-ejemplo
```

- Para bajar lo ultimo, sin modificar tu "stage"
O sea, tus archivos seguiran intactos
```Shell
git fetch
```

- Para bajar solo una rama especifica
=======
Rama MASTER

Ahora iniciaremos con el uso de las "branch". O, Ramas.

Lo primero que debemos hacer, es aprender que no solo con git pull se pueden bajar los cambios actuales de un repositorio. Pueden bajar cambios de master o de otra rama. Por ejemplo: develop O el nombre que le haya dado su lider de equipo.

Para saber que ramas existen en el origin y en tu local. Y en cual estas!
```Shell
git branch -av
```
Para bajar lo ultimo de una rama, modificando tu "stage" O sea, tus archivos seran actualizados.
```Shell
git pull origin rama-ejemplo
```
Para bajar lo ultimo, sin modificar tu "stage" O sea, tus archivos seguiran intactos
```Shell
git fetch
```
Para bajar solo una rama especifica
>>>>>>> 90b8701fe85d66ebc58b3c0dbfac368eb98eba9c
```Shell
git fetch origin rama-ejemplo
```

<<<<<<< HEAD
- Para crear una rama local que sea copia de una rama remota
Primero deben bajarla con git fetch
```Shell
git branch rama-nueva  origin/rama-nueva
```

=======

- Para bajar lo ultimo de una rama, modificando tu "stage"
O sea, tus archivos seran actualizados.
```Shell
git pull origin rama-ejemplo
```

- Para bajar lo ultimo, sin modificar tu "stage"
O sea, tus archivos seguiran intactos
```Shell
git fetch
```

- Para bajar solo una rama especifica
```Shell
git fetch origin rama-ejemplo
```

- Para crear una rama local que sea copia de una rama remota
Primero deben bajarla con git fetch
```Shell
git branch rama-nueva  origin/rama-nueva
```

>>>>>>> rama-abraham
- Para cambiarte de rama se usa checkout
```Shell
git checkout rama-ejemplo
```
<<<<<<< HEAD

- Para mezclar/fusionar los cambios de otra rama con la tuya se usa merge
```Shell
git checkout rama-mia

git merge rama-pablo
```

## Francisco Sáez
 Oh, ohhh... creo que metí la pata! al parecer, también guardé los cambios de mi rama en el master. El Jefe que por favor nos ilumine cómo resolver esos casos!
=======
Para crear una rama local a partir de otra rama local:
```Shell
git checkout -b rama-nueva master
```

Para crear una rama local que sea copia de una rama remota Primero deben bajarla con git fetch
```Shell
git branch rama-nueva  origin/rama-nueva
```
Para cambiarte de rama se usa checkout
```Shell
git checkout rama-ejemplo
```
Para mezclar/fusionar los cambios de otra rama con la tuya se usa merge
```Shell
git checkout rama-mia

git merge rama-pablo
```

#############################################

## Deshacer el ultimo merge o git pull
```Shell
git reset --hard OCHO_PRIMEROS_CARACTERES_DEL_COMMIT
```
## Deshacer el último commit (sin haber hecho push) SIN PERDER LOS CAMBIOS
```Shell
git reset --soft HEAD~1
```

## Deshacer el último commit 
===> (habiendo hecho ya hecho un push al repositorio) Ej. github
```Shell
git reset HEAD~1
```
CORREGIR LOS ARCHIVOS
```Shell
git add -A
git commit -am "xxx"
git push -f origin rama-destino
``` 
>>>>>>> 90b8701fe85d66ebc58b3c0dbfac368eb98eba9c


##AAGB
modificando readme desde rama_abraham


=======

- Para mezclar/fusionar los cambios de otra rama con la tuya se usa merge
```Shell
git checkout rama-mia

git merge rama-pablo
```
>>>>>>> rama-abraham
