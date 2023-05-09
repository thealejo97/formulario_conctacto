# Formulario contacto


Aplicación en django desarrollada como prueba técnica

## Informacion de la aplicacion:

Aplicacion desarrollada en Django, usando como motor de base de datos MySQL, como controlador de versiones se tiene github: 'https://github.com/thealejo97/formulario_conctacto', usa plugin de ciudades cities_ligth,
contiene medidas de seguridad separando los datos sensibles en el archivo secrets.json que no se carga a ningun repositorio remoto

## Proceso de instalación:

1. Crear un ambiente de django (O utilizar el ambiente_formulario_contacto)
2. Instalar los requirements ejecutando 'pip install -r requirements.txt' 
3. Crear la base de datos en MySql 
4. Configurar la información de la base de datos en el archivo secrets.json, ejemplo de secrets.json:
 ```
   {
    "FILENAME": "secrets.json",
    "SECRET_KEY": "django-insecure-5po5&8@sso1c0w*1c@jw9g3@+l+uy!__ylw2gt+1@5o=!3op*t",
    "DEBUG": true,
    "DATABASE_DEFAULT": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "formulario_contacto_db",
        "USER": "admin",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": "3306",
        "ATOMIC_REQUESTS": true
    }
}
```
6. Con el ambiente de django ejecutando realizar los siguientes ejecuta los siguientes comandos:
7. python manage.py migrate
8. 'python manage.py cities_light' - Crea las ciudades y paises en la base de datos
9. En caso de error al crear las ciudades ejecuta 'python manage.py cities_light --force-all'



