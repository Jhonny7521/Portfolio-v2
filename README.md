# PORTFOLIO V2
## DESCRIPCIÓN

__PORTFOLIO V2__ en la versión actual permite registrar varios usuarios y agregar sus proyectos. Unicamente se pueden realizar dichas funcionalidades cuando un usuario esta logueado.

### Credenciales de prueba

Si desea ver la funcionalidades del projecto puede utilizar las credenciales de prueba. Se el pide a los desarrolladores hacer el uso uso correcto en base a las indicaciones aqui mencionadas para verificar las funcionalidades sin cambiar los datos ya registrados.

```sh 
Usuario: Jhonny28 
Password: jhonny_jhonny123
```

## INFORMACIÓN DE USO

__PORTFOLIO V2__ es un producto gratuito y está abierto para su libre uso. Se le pide a los desarrolladores hacer el uso correcto en base a las indicaciones aqui mencionadas.

## REGISTRO DE USUARIO

- __Base url:__  `"https://portfolio-v2-production-c48c.up.railway.app/"`

Inicialmente la solicitud inicial es GET donde se renderiza a un usuario predeterminado que es el mio. Para verificar las funcionalidades del usuario logueado puede registrarse.


## ENDPOINTS DEL PROYECTO

### Para registrarse utilice:

- __GET__  y  __POST__  `"https://portfolio-v2-production-c48c.up.railway.app/user/register/"`

Esta URL redirige a un formulario de registro de un usuario.

Una vez enviado los datos se envía con el método POST, y se crea el usuario. Luego es redirigido a la URL base.


 ### Para crear projectos debe redirigirse a:

- __GET__  y  __POST__ `"https://portfolio-v2-production-c48c.up.railway.app/project/create/"`

Esta url se puede ingresar desde el botón "crear projecto" de las sección Portfolio.

Esta URL redirige a un formulario para creacion de proyectos. Para la creacion de proyctos se esta utilizando dos modelos con una relacion ManyToMany. Las cuales son "Project" y "Task".

Se crea el projectos con los datos enviados y ron redirigidos a la url base, donde se prodrá visualizar el projecto creado.

### Para editar projectos debe redirigirse a:

- __GET__  y  __POST__ `"https://portfolio-v2-production-c48c.up.railway.app/project/edit/<id>"`

Esta url se puede ingresar desde el icono de "editar" del card de cada proyecto.

Aqui se esta enviando como parametro el "id" del proyecto que se quiere editar. Para ello se hace la consulta a la base de datos y se presentan para su edición a traves del formulario

### Para eliminar projectos debe redirigirse a:

- __GET__  y  __POST__ `"https://portfolio-v2-production-c48c.up.railway.app/project/delete/<id>"`

Esta url se puede ingresar desde el icono de "eliminar" del card de cada proyecto.

Aquí se recibe el parametro "id" del proyeci que se desa eliminar.

### Para las IP de las visitas del sitio debe redirigirse a:

- __GET__  `"https://portfolio-v2-production-c48c.up.railway.app/user/see_visits/"`

Esta direccion mostrará en una tabla en orden descendente las IP que han realizado las visitas al sitio.


## CLONACIÓN DE PROYECTO

Para interatuar con el presente proyecto se debe tener en cuenta la versión de python instalada Python 3.9.7. Así tambien, deberá seguir las siguientes indicaciones:

- Clonar el repositorio:
```sh
$ git clone 
```

- Instalar un ambiente virtual
```sh
$ python -m venv venv
```

- Activar el ambiente virtual
```sh
$ source venv/Scripts/activate    --> Windows
$ source venv/bin/activate        --> Linux
```

- Instalar requerimientos:
```sh
$ pip install -r requirements.txt
```

- Ejecutar requerimientos:
```sh
$ cd projectName
```
Debe verificar que se encuentre en la carpeta que contiene el archivo manage.py. Luego debe ingresar el siguiente comando en la terminal
```sh
$ py manage.py runserver
```


### SOBRE EL PROYECTO:

- Lenguaje de programación: __Python__
- Versión de lenguaje: __Python 3.9.7__
- Framework utilizado: __DJango__
- Motor de base de datos: __MySQL__