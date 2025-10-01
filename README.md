# Proyecto Back-End 1
### Integrantes: Benjamin Duarte, Marina Martinez, Cristobal Medina, Patricio Villalobos


## Descripcion del proyecto
Queremos tener una pagina en la cual la gente pueda adoptar mascotas de forma mas facil, y que esos animales puedan encontrar un dulce hogar.
En eso consiste este proyecto, una pagina desarrollada con el framework de Django, donde ahora mismo en el repositorio esta la primera version.

Tristemente, por ahora, solo esta los modelos de la base de datos definidos (sujeto a cambios futuros) y la pagina del admin para la supervicion de los modelos y otros administradores.

## Estructura
La estructura basica del proyecto es la de DJango


![image](https://media.discordapp.net/attachments/776863649570226199/1422775775157031022/image.png?ex=68dde6b2&is=68dc9532&hm=20a2e83f5da84e2af55679c6d1a1cb6fc08e4e911f3984918bbf1c6679c5365d&=&format=webp&quality=lossless)

Como se ve en la captura, "pagina" es la carpeta de la app principal, y "ev_backend" la carpeta del proyecto.

Donde hay codigo util es solo en models, donde estan todos las tablas de datos a utilizar. Y en admin definido las tablas del models que se pueden ver desde la pestaña de admin. el resto se mantiene en su mayoria igual.
## Requisitos Previos

- Python - Version 1.13.0 como minimo

- Git - Mas reciente siempre recomendada

Puedes probar que version tienes asi:
```bash
python --version
```
o 
```bash
python3 --version
```
y para Git
```bash
git --version
```


## Instalacion de Requisitos Previos
En caso de no tener Python y Git:

- Para Linux (Con distribuciones basadas en Debian/Ubuntu):
```bash
sudo apt update
sudo apt install python3 git -y
```

- Para Linux (Con distrubuciones basadas en Fedora/CentOS/RHEL):
```bash
sudo dnf install python3 git -y
```

- Y en Windows:
```bash
winget install -e --id Python.Python.3
winget install -e --id Git.Git
```

Aunque tambien puedes instalarlo desde las paginas oficiales
(
[Python](https://www.python.org/downloads/)
) (
[Git](https://git-scm.com/downloads)
)


## Clonar Repositorio
Dentro de una carpeta, abre la terminal y ejecuta el siguiente comando para clonar el proyecto en tu carpeta
```bash
git clone https://github.com/marinamartinezd/ev_backend.git
cd ev_backend
```


## Crear ambiente
Como buena practica, es ideal aislar las dependencias del proyecto
```bash
python -m venv Nombre_Ambiente
```

Una vez creado, activalo:
- En Windows
```bash
.\Nombre_Ambiente\Scripts\activate
```
- En Linux
```bash
source Nombre_Ambiente/bin/activate
```

## Instalar DJango
El proyecto esta hecho con Django, asi que hay que instalarlo en el ambiente
```bash
pip install Django
```


## Aplicar Migraciones
Una vez con Django, hay que crear la base de datos y sus tablas:
```bash
python manage.py migrate
```


# Ejecutar App
Una vez todo listo, ya puedes ejecutar el proyecto con:
```bash
python manage.py runserver
```



Te generara un link donde puedes acceder a la pagina del proyecto
## Extra: Admin
Si en el link agregas al final un /admin, puedes acceder a la pestaña de admin, con las credenciales:
- admin
- contraseñaadmin

## Extra: .dll
El archivo .dll de la base de datos se encuentra en la carpeta dll
