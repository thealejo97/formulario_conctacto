# Formulario contacto


Aplicación en django desarrollada como prueba técnica

Proceso de instalación:

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



