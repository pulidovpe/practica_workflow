# practica_workflow

### Hora de ordenar la chuleta

## Comandos GIT importantes:

### Para ver el estado del proyecto (archivos modificados o nuevos)
```Shell
git status
```

### Para agregar un nuevo archivo, o uno modificado
```Shell
git add archivo.txt
```
### Para agregar varios archivos...
```Shell
git add archivo.txt carpeta/otro_archivo.txt otra_carpeta/otro_archivo.txt
```
### Para agregar todos los archivos del proyecto
```Shell
git add -A

git add --all
```

### Para ver diferencias en un archivo modificado comparando con su versión anterior
```Shell
git diff --staged
```

### Para dar informacion acerca del/los cambio(s) realizado(s)
```Shell
git commit -m "Agregué una lista de comandos git"
```
### Para ver información de los commits hechos
```Shell
git log

git log --name-status
```

### Para bajar cambios de la rama master del repositorio remoto
```Shell
git pull origin master
```
### Para subir cambios a la rama master del repositorio remoto
```Shell
git push origin master
```

### Guardar cambios locales en una "stage" aparte
```Shell
git stash
```
### Para recuperar los cambios guardados en el "stage"
```Shell
git stash apply
```

-------------------------------------------

## En este archivo empezaremos la práctica. 

>Rama MASTER

Ahora iniciaremos con el uso de las "branch". O, Ramas.
Lo primero que debemos hacer, es aprender que no solo con git pull se pueden bajar los cambios actuales de un repositorio. Pueden bajar cambios de master o de otra rama. Por ejemplo: develop O el nombre que le haya dado su lider de equipo.

### Para saber que ramas existen en el origin y en tu local. Y en cual estas!
```Shell
git branch -av
```
### Para bajar lo ultimo de una rama, modificando tu "stage" O sea, tus archivos seran actualizados.
```Shell
git pull origin rama-ejemplo
```
### Para bajar lo ultimo, sin modificar tu "stage" O sea, tus archivos seguiran intactos
```Shell
git fetch
```
### Para bajar solo una rama especifica
```Shell
git fetch origin rama-ejemplo
```

### Para crear una rama local que sea copia de una rama remota
Primero deben bajarla con git fetch
```Shell
git branch rama-nueva  origin/rama-nueva
```

### Para crear una rama a partir de otra local
```Shell
git checkout -b rama-nueva  master
```

### Para cambiarte de rama se usa checkout
```Shell
git checkout rama-ejemplo
```

### Para mezclar/fusionar los cambios de otra rama con la tuya se usa merge
```Shell
git checkout rama-mia

git merge rama-pablo
```

---------------------------------------

### Deshacer el ultimo merge o git pull
```Shell
git reset --hard OCHO_PRIMEROS_CARACTERES_DEL_COMMIT
```
### Deshacer el último commit (sin haber hecho push) SIN PERDER LOS CAMBIOS
```Shell
git reset --soft HEAD~1
```

### Deshacer el último commit, habiendo hecho ya un push. Ej. github
```Shell
git reset HEAD~1
```
Luego corriges los archivos y vuelves a subir todo
```Shell
git add -A
git commit -am "xxx"
git push -f origin rama-destino
``` 

---------------------------

### Resolucion de conflictos

Otra manera para resolver los conflictos es que podemos indicarle de antemano a git que estrategia tomar cuando tiene que decidir un conflicto, esto con las opciones ours y theirs, de esta manera:
```Shell	
git merge -s recursive -X theirs rama-a-fusionar
```

Esto cuando queremos que git resuelva el conflicto usando los cambios de la rama a fusionar (theirs o suyos) y cuando queremos que tome los cambios de la rama donde se está fusionando (ours o nuestros): 
```Shell
git merge -s recursive -X ours rama-a-fusionar
```


--------------------------------------------

## Estructura de los Mensajes en los COMMITS

Al crear un commit luego de añadir los archivos modificados/creados
y estas por agregar informacion sobre lo que hiciste, lo mas práctico
es escribir unas pocas palabras para informar sobre el cambio.
Ej.
```Shell
git commit -am "Agregue la funcion eliminar"
```
Pero, en proyectos mas grandes y complejos, es mejor utilizar los 
estandares propuestos. Ej.
```Shell
git commit
```
Ustedes dirán  "y donde está el mensaje?". Pués al ejecutar el commit
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
