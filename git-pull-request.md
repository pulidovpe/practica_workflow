# Git - Pull Request

PULL REQUEST y FORK

> El programador, una vez reciba su issue, puede seguir alguno de los métodos que describo a coontinuación: <br />

➡️ Primero hagan un FORK (Dar click en el boton Fork que esta arriba a la derecha debajo de su nombre de usuario).

➡️ Esto creara una copia del proyecto en su perfil de github. Descarguenlo y modifiquenlo localmente. Despues al terminar y probar que todo le funciona  pueden subirlo  (subira a su cuenta).

➡️ En su cuenta, en el repo del FORK esta el boton/enlace de crear un pull request. Esta a mano derecha, debajo del boton CLONE.

➡️ En la siguiente pantalla, el pull request les mostrará los cambios de uds en comparacion con el proyecto original. Agreguenle algun mensaje explicando los cambios que hicieron y envienlo.

➡️ El encargado de la rama develop la revisa, la prueba, etc. Luego, la aprueba o rechaza. Al hacer esto, el/ella es quien se encarga de fusionar ese pull request con la rama develop.

# Método usando el programa git-pull-request

➡️ Instalación:

`pip3 install git-pull-request`

## Forma de Uso:

➡️ Si no ha descargado una copia del proyecto, hágalo ahora. 

➡️ Ubíquese dentro de la rama master o la rama principal del proyecto.

➡️ Se hacen los cambios que se pidieron en el issue. Y se hacen los commits necesarios. Luego, se ejecuta:

`git pull-request`

Esta ejecución hará lo siguiente:

1. Hará Fork al repositorio en tu cuenta
2. Agregará el repositorio del Fork como una rama remota en esa misma carpeta. Con el nombre "github".
3. Forzará un push de esa rama remota recien creada. Es decir, no necesitas hacer `git push` después de este comando.
4. Creará un pull-request para tu rama actual a la rama remota, o master por defecto. Es decir, no necesitas hacer más nada sino esperar.
