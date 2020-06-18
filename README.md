práctica_flujo de trabajo
Hora de ordenar la chuleta
Comandos GIT importantes:
Para ver el estado del proyecto (archivos modificados o nuevos)
estado git
Para agregar un nuevo archivo, o uno modificado
git add archivo.txt
Para agregar varios archivos ...
git add archivo.txt carpeta / otro_archivo.txt otra_carpeta / otro_archivo.txt
Para agregar todos los archivos del proyecto
git add -A

git add --todos
Para ver diferencias en un archivo modificado comparando con su versión anterior
git diff --estado
Para dar información acerca del / los cambio (s) realizado (s)
git commit -m " Agregue una lista de comandos git "
Para ver información de los commits hechos
registro de git

git log --name-status
Para bajar cambios de la rama master del repositorio remoto
maestro de origen git pull
Para subir cambios a la rama master del repositorio remoto
maestro de origen de empuje git
Guardar cambios locales en una "etapa" aparte
escondite
Para recuperar los cambios guardados en el "escenario"
git alijo aplicar
________________________________________
En este archivo empezaremos la práctica.
Rama MASTER
Ahora iniciaremos con el uso de las "sucursales". Oh, Ramas. Lo primero que debemos hacer, es aprender que no solo con git pull se pueden bajar los cambios actuales de un repositorio. Pueden bajar cambios de maestro o de otra rama. Por ejemplo: desarrolle O el nombre que le haya dado su lider de equipo.
Para saber que ramas existen en el origen y en tu local. Y en cual estas!
git branch -av
Para bajar lo último de una rama, modificando tu "etapa" O sea, tus archivos seran actualizados.
git pull origin rama-ejemplo
Para bajar lo ultimo, sin modificar tu "etapa" O sea, tus archivos seguiran intactos
git fetch
Para bajar solo una rama especifica
git fetch origin rama-ejemplo
Para crear una rama local que sea copia de una rama remota
Primero deben bajarla con git fetch
git branch rama-nueva origin / rama-nueva
Para crear una rama a partir de otra local
git checkout -b master rama-nueva
Para cambiarte de rama se usa checkout
git checkout rama-ejemplo
Para mezclar / fusionar los cambios de otra rama con la tuya se usa merge
git checkout rama-mia

git merge rama-pablo
________________________________________
Deshacer el ultimo merge o git pull
git reset --hard OCHO_PRIMEROS_CARACTERES_DEL_COMMIT
Deshacer el último commit (sin haber hecho push) SIN PERDER LOS CAMBIOS
git reset --soft HEAD ~ 1
Deshacer el último compromiso, habiendo hecho ya un empujón. Ej. github
git reset HEAD ~ 1
Luego corriges los archivos y vuelves a subir todo
git add -A
git commit -am " xxx " 
git push -f origen rama-destino
________________________________________
Resolucion de conflictos
Otra manera para resolver los conflictos es que podemos indicarle de antemano a git que estrategia tomar cuando tiene que decidir un conflicto, esto con las opciones nuestras y las suyas, de esta manera:
git merge -s recursivo -X suyo rama-a-fusionar
Esto cuando queremos que resuelva el conflicto usando los cambios de la rama a fusionar (suyos o suyos) y cuando queremos que tome los cambios de la rama donde se está fusionando (nuestro o nuestros):
git merge -s recursive -X our rama-a-fusionar
________________________________________
Estructura de los Mensajes en los COMPROMISOS
Al crear un compromiso, luego agregar los archivos modificados / creados y estas por agregar información sobre lo que hiciste, lo más práctico es escribir unas pocas palabras para informar sobre el cambio. Ej.
git commit -am " Agregue la función eliminar "
Pero, en proyectos mas grandes y complejos, es mejor utilizar los estandares propuestos. Ej.
git commit
Ustedes dirán "y donde está el mensaje?". Puede ejecutar el compromiso de esa manera, sin parámetros ni nada, abrir un editor donde colocar una descripción más amplia de lo que hicieron. La siguiente documentación explica la forma de escribir la información del compromiso de una forma más específica y explicita:
•	El mensaje de un compromiso consiste en 3 diferentes partes separadas por una línea en blanco: el título, un cuerpo opcional y un pastel opcional. Algo como lo siguiente:
________________________________________
tipo: sujeto
cuerpo
pie de página
________________________________________
El título consiste en el tipo y asunto del mensaje. Tipo / Tipo
El asunto no debe contener más de 50 caracteres, debe iniciar con una letra mayúscula y no terminar con un punto. El tipo es contenido en el título y puede ser de algunos de los siguientes casos:
•	hazaña: Una nueva caracteristica
•	arreglo: Se soluciono un bug
•	docs: Se modificaron los cambios en la documentación
•	estilo: Se aplico formato, comas y puntos faltantes, etc; Sin cambios en el codigo
•	refactor: Refactorizacion del codigo en produccion
•	perf: Un cambio en el código que mejora el rendimiento
•	prueba: Se añadieron pruebas, refactorización de pruebas; Sin cambios en el codigo
•	tarea: actualización de tareas de construcción, configuración del administrador. de paquetes; sin cambios en el codigo
Al escribir el cuerpo (Cuerpo), requiere una línea en blanco entre el título y el cuerpo, debemos limitar la longitud de cada línea a no más de 72 caracteres.
El pie es opcional al igual que el cuerpo, pero este es usado para el seguimiento de los ID con incidencias. Ej:
Resuelve: # 6113 Problemas: # 456, # 789
Plantilla ejemplo:
________________________________________
hazaña: Ultima documentacion del Readme
Se agregan comandos para solucionar conflictos
ademas de la información sobre las plantillas de
los mensajes largos en los commit
Problema: # 123

### ACTUALIZANDO README EN RAMA-ABRAHAM