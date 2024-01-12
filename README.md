## Prueba_Hikko
Prueba para evaluar mi nivel de Python

El proyecto es una API que se inicializa desde un script.


## Objetivos


### Resumido

El objetivo es crear una API que, a partir de datos almacenados en archivos “.json”, los procese y mediante los endpoints necesarios, cumpla con los requerimientos listados en la sección **“Objetivos -> Explayado”** (la siguiente).


### Explayado

El objetivo de este proyecto que crear una API que implemente los endpoints necesarios para cumplir con los siguientes requerimientos

- Un endpoint que devuelva todos los usuarios. Para cada usuario debe proveer sus identificadores (id/ids) y una lista de identificadores de usuarios que lo siguen a él.

- Un endpoint que devuelva el usuario que cuanta con menos seguidores. Debe mostrar tanto el identificador de dicho usuario, como numero de seguidores con el que cuenta.

	- En caso de que haya mas de un usuario que cumpla con dicha condición, se debe devolver 1 al azar. 

Dicha información sobre los usuarios debe obtenerse de un directorio donde se almacenan los usuarios bajo el siguiente formato: 

- Cada usuario se almacena en un archivo en formato JSON, el cual contiene únicamente un usuario

- Para cada usuario, se cuenta con la siguiente información:

    - “user_id”: (string) contiene el identificado del usuario

    - “users_following”: (array de strings) los identificadores de los usuarios a los que este usuario sigue

Ejemplo de usuario:

- Nombre archivo: u01.json

- Contenido:
```
{
    "user_id": "1",
    "users_following": [
        "2",
        "9"
    ]
}
```

Mas ejemplos de pueden encontrar en la carpeta **“./examples/data/”** de este repositorio.


## Pre-Requisitos
- Tener Python 3 instalado 
    - (la aplicación se desarrolló con Python 3.11.3, por lo que se recomienda tener como mínimo esa versión)
- Tener Pip instalado 
    - Si se instalo Python desde la página oficial (https://www.python.org/) entonces ya está instalado

## Requerimientos
#### Flask 3.0.0
Para instalarlo se usa el siguiente comando:
```
pip install Flask
```
Alternativamente, como se incluyo el “requirements.txt” en la carpta “app”, se puede navegar desde la consola a dicha carpeta y ejecutar el comando:
```
pip install -r requirements.txt
```

## Uso
### Inicialización 
El punto de entrada a la aplicacion es el archivo **app/main.py**. 

Además de descargar el repositorio, también hay que tener preparados los archivos “.json” con los usuario (todos tienen que estar dentro de una misma carpeta). Esta carpeta puede ser la carpeta “/examples/data” de este proyecto, o una carpeta cualquiera del dispositivo local.

Una vez lo anterior este preparado, se ejecuta desde una consola el comando:
```
Python <ruta de /main.py> <Ruta a la carpeta con los archivos “.json”>
```

Se puede omitir el parámetro con la ruta a las carpeta de los archivos (en cuyo caso se usara la ruta por defecto, definida en "./app/config.json"):
```
Python <ruta de /main.py>
```

##### Aclaraciones:
- La capeta por defecto es: **“./examples/data/”**, de este repositorio. 
- La carpeta por defecto se puede cambiar, para hacerlo la ruta a la nueva carpeta por defecto se coloca como valor del atributo **"users_dir_path_form_utils"**, en el archivo **“./app/config.json”**.
	- **IMPORTANTE**: dicha ruta debe ser relativa, empezando desde la carpeta **"./app/utils/"** de este repositorio. Tomar como ejemplo el valor actual:
```
    "users_dir_path_form_utils" : "../../examples/data"
``` 
 

### Endpoints
- Ruta base: no se configuro ni la ruta ni el puerto, por lo que se usaran los por defecto:
    - ruta_base = http://127.0.0.1:5000

Lo requerido se implementó mediante 2 endpoints REST:

- Para obtener todos los usuarios, con los usuarios que los siguen:

| GET | <ruta_base>/api/users |
| ----------- | ----------- |
| HEADERS | NONE |
| PARAMS | NONE |
| BODY | NONE |

- Para obtener el usuario con menos seguidores (aleatorio entre los posibles, si hay mas que 1):

| GET | <ruta_base>/api/users/leastfollowed |
| ----------- | ----------- |
| HEADERS | NONE |
| PARAMS | NONE |
| BODY | NONE |


### Ejemplos de uso

- Los ejemplos se realizaron con los datos provistos para la prueba (también se subieron en la carpeta **/ejemplos/data**) 

---

Obtener el usuario con menos seguidores:

- Request:

![get_all_users_request](documentation/get_all_users_request.PNG)

- Response (no se muestra en la totalidad):

![get_all_users_response](/documentation/get_all_users_response.PNG)

---

Obtener el usuario con menos seguidores:

- Request:

![get_least_followed_user_request](/documentation/get_least_followed_user_request.PNG)

- Response:

![get_least_followed_user_response](/documentation/get_least_followed_user_response.PNG)

---

### Contenidos

|Archivo|Descripcion|
|-------|-----------|
|README.md|Documentación del proyecto|
|.gitignore|Archivos que nos se necesita/quiere subir a git.|
|./examples/data/|Datos de prueba.|
|./documentacion/|Carpeta para archivos usados para complemetar la documentación (en este caso solo imagenes usadas en la seccion **"Ejemplos de uso"**).|
|./app/requirements.txt|Imports (dependencias) del proyecto. No incluye imports estandar de Python como "os", "json", "sys", etc; ni dependencias internas (a otros archivos del mismo proyecto) (se puede usar con "pip install" como se mostro anteriormente para descargar dichas dependencias).|
|./app/main.py|Punto de entrada a la aplicacion, donde se instancian los servicios a utilizar.|
|./app/constants.py|Punto centralizado donde se mantienen las constantes utilizadas en multiples puntos del proyecto.|
|./app/config.json|Archivo de configuracion. Lo unico que se configura es la ruta por defecto de los datos (usuarios)|
|./app/utils/|Carpeta donde se implmenetan funcionalidades genericas que se usan o podrian llegar a usarse en varias partes del proyecto|
|./app/utils/users.py|Funcionalidad referente a los usuarios. En este caso crearlos en distintos formatos o realizar operacion sobre listas de ellos.|
|./app/utils/script_inputs.py|Funcionalidad relacionada a los parametros que el se esperan al inicializar la aplicacion (En este caso, solo la ruta a la carpeta con los archivos ".json" con los usuarios).|
|./app/utils/custom_decorators.py|Decoradores implementados manualmente. En este caso, el unico implementado "**singleton(...)**" permite mantener una unica instancia en toda aplicacion de las calses a la que se aplique.|
|./app/routes/|Carpeta para los archivos donde se defininen los endpoints de la API|
|./app/routes/users.py|Aqui se definien los endpoints correspondiente a la ruta **"/api/users"**.|
|./app/data_access/|Carpeta donde se implementa la lectura de datos externos a la aplicacion.|
|./app/data_access/users.py|Aqui se implementa la carga de usuarios desde archivos **".json"**.|

## ACLARACIONES
1. Se asumió que todos valores de "users_following" se corresponden a un "user_id" que si existe.
2. No se contempló la posibilidad de "user_id" duplicados.
3. Se asumió que todos los archivos “.json” tienen usuarios en el formato mostrado en la letra de la prueba, y que solo hay un usuario por archivo.
4. Puede que haya casos borde sin contemplar.
5. Se asume que en el directorio/carpeta donde se guardan los archivos “.json”, todos los archivos “.json” cumplen con el formato esperado (presentado en la sección de **“Objetivos”**).
    - Los archivos con otras extensiones son ignorados, por lo que su presencia no altera el funcionamiento de la aplicación.

