# practica_workflow

## Hora de ordenar la chuleta
## Comandos GIT importantes:

- Para ver el estado del proyecto (archivos modificados o nuevos)

```
git status
```

- Para agregar un nuevo archivo, o uno modificado

```
git add archivo.txt
```

- Para agregar varios archivos...

```
git add archivo.txt carpeta/otro_archivo.txt otra_carpeta/otro_archivo.txt
```

- Para agregar todos los archivos del proyecto

```
git add -A
```

```
git add --all
```

- Para ver diferencias en un archivo modificado comparando con su versión anterior

```
git diff --staged
```

- Para dar informacion acerca del/los cambio(s) realizado(s)

```
git commit -m "Agregué una lista de comandos git"
```

- Para ver información de los commits hechos

```
git log
```

```
git log --name-status
```

- Para bajar cambios de la rama master del repositorio remoto

```
git pull origin master
```

- Para subir cambios a la rama master del repositorio remoto

```
git push origin master
```

- Guardar cambios locales en una "stage" aparte

```
git stash
```

- Para recuperar los cambios guardados en el "stage"

```
git stash apply
```

## En este archivo empezaremos la práctica. 

Rama de **Francisco**

Ahora iniciaremos con el uso de las "branch". O, Ramas.

Lo primero que debemos hacer, es aprender que no solo con git pull
se pueden bajar los cambios actuales de un repositorio.
Pueden bajar cambios de master o de otra rama. Por ejemplo: develop
O el nombre que le haya dado su lider de equipo.

- Para saber que ramas existen en el origin y en tu local. Y en cual estas!

```
git branch -av
```

- Para bajar lo ultimo de una rama, modificando tu "stage". O sea, tus archivos seran actualizados.

```
git pull origin rama-ejemplo
```

- Para bajar lo ultimo, sin modificar tu "stage", O sea, tus archivos seguiran intactos

```
git fetch
```

- Para bajar solo una rama especifica
---
**Rama MASTER**

Ahora iniciaremos con el uso de las "branch"  o Ramas.

Lo primero que debemos hacer, es aprender que no solo con git pull se pueden bajar los cambios actuales de un repositorio. Pueden bajar cambios de master o de otra rama. Por ejemplo: develop O el nombre que le haya dado su lider de equipo.

- Para saber que ramas existen en el origin y en tu local. Y en cual estas!

```
git branch -av
```

- Para bajar lo ultimo de una rama, modificando tu "stage" O sea, tus archivos seran actualizados.

```
git pull origin rama-ejemplo
```

- Para bajar lo ultimo, sin modificar tu "stage" O sea, tus archivos seguiran intactos

```
git fetch
```

- Para bajar solo una rama especifica

```
git fetch origin rama-ejemplo
```
- Para crear una rama local que sea copia de una rama remota. Primero deben bajarla con git fetch

```
git branch rama-nueva  origin/rama-nueva
```

- Para cambiarte de rama se usa checkout

```
git checkout rama-ejemplo
```

- Para mezclar/fusionar los cambios de otra rama con la tuya se usa merge
```
git checkout rama-mia
```
```
git merge rama-pablo
```

- Para crear una rama local a partir de otra rama local:

```
git checkout -b rama-nueva master
```

- Para crear una rama local que sea copia de una rama remota Primero deben bajarla con ```git fetch```

```
git branch rama-nueva  origin/rama-nueva
```

- Para cambiarte de rama se usa checkout

```
git checkout rama-ejemplo
```

- Para mezclar/fusionar los cambios de otra rama con la tuya se usa merge

```
git checkout rama-mia
```

```
git merge rama-pablo
```

## Deshacer el último merge o git pull

```
git reset --hard OCHO_PRIMEROS_CARACTERES_DEL_COMMIT
```

## Deshacer el último commit (sin haber hecho push) SIN PERDER LOS CAMBIOS

```
git reset --soft HEAD~1
```

## Deshacer el último commit 
===> (habiendo hecho ya hecho un push al repositorio) Ej. github

```
git reset HEAD~1
```

##CORREGIR LOS ARCHIVOS

```
git add -A
```

```
git commit -am "xxx"
```

```
git push -f origin rama-destino
``` ---------------------------

### Resolucion de conflictos

Otra manera para resolver los conflictos es que podemos indicarle de antemano a git que estrategia tomar cuando tiene que decidir un conflicto, esto con las opciones ours y theirs, de esta manera:

```
git merge -s recursive -X theirs rama-a-fusionar
```

Esto cuando queremos que git resuelva el conflicto usando los cambios de la rama a fusionar (theirs o suyos) y cuando queremos que tome los cambios de la rama donde se está fusionando (ours o nuestros): 

```
git merge -s recursive -X ours rama-a-fusionar
```

--------------------------------------------

## Estructura de los Mensajes en los COMMITS

Al crear un commit luego de añadir los archivos modificados/creados
y estas por agregar informacion sobre lo que hiciste, lo mas práctico
es escribir unas pocas palabras para informar sobre el cambio.
Ej.

```
git commit -am "Agregue la funcion eliminar"
```

Pero, en proyectos mas grandes y complejos, es mejor utilizar los 
estandares propuestos. Ej.

```
git commit
```

Ustedes dirán "y donde está el mensaje?". Pués al ejecutar el commit
de esa manera, sin parametros ni nada, les abrirá un editor donde
colocar una descripcion mas amplia de lo que hicieron. La siguiente 
documentacion explica la forma de escribir la informacion del commit 
de una forma más detallada y explicita:

- El mensaje de un commit consiste en 3 diferentes partes 
separadas por una linea en blanco: el titulo, un cuerpo 
opcional y un pie opcional. Algo como lo siguiente:

-------------

type: subject 

body 

footer

-------------

El titulo consiste en el tipo y asunto del mensaje.
Type / Tipo

El asunto no debe contener mas de 50 caracteres, 
debe iniciar con una letra mayuscula y no terminar con un punto.
El tipo es contenido en el titulo y puede ser de alguno de los siguientes casos:

- feat: Una nueva caracteristica
- fix: Se soluciono un bug
- docs: Se realizaron cambios en la documentacion
- style: Se aplico formato, comas y puntos faltantes, etc; Sin cambios en el codigo
- refactor: Refactorizacion del codigo en produccion
- perf: Un cambio en el código que mejora el desempeño
- test: Se añadieron pruebas, refactorizacion de pruebas; Sin cambios en el codigo
- chore: Actualizacion de tareas de build, configuracion del admin. de paquetes; sin cambios en el codigo

Al escribir el cuerpo (Body), requerimos de una linea en blanco 
entre el titulo y el cuerpo, ademas debemos limitar la longitud 
de cada linea a no mas de 72 caracteres.

El pie es opcional al igual que el cuerpo, pero este es usado 
para el seguimiento de los IDs con incidencias. Ej:

Resolves: #6113 
Issues: #456, #789

Plantilla ejemplo:

--------------------------------------------------------

feat: Ultima documentacion del Readme

Se agregaron comandos para solucionar conflictos <br />
ademas de la informacion sobre las plantillas de <br />
los mensajes largos en los commit 

Issue: #123

-----------------
##Mi bitácora:

##01/06/2020

- Descargada rama-francisco
- Modificado README.md de rama-francisco
- Subidos los cambios a rama-francisco

##02/06/2020

- Realizando la tarea de hoy
- Agregada una imagen al README.md

![Francisco](fjss.jpg)

##04/06/2020

- Ordenando el README.md

##06/06/2020

- Actualizando el README.md a partir de un merging, lo que ocasionó un conflicto.
- El conflicto fue solucionado manualmente.
