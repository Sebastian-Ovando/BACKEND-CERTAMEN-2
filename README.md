ProyectoMesa — Mesa de Ayuda
Una aplicación de mesa de ayuda simple construida con Django.

📋 Requisitos
Python 3.10+
Virtualenv o venv
Git

🚀 Instalación rápida (Windows PowerShell)
Sigue estos pasos para poner en marcha el proyecto localmente.

Clona el repositorio y entra al directorio del proyecto:

Bash

git clone https://github.com/Sebastian-Ovando/BACKEND-CERTAMEN-2
cd ProyectoMesa
Crea y activa un entorno virtual (usando PowerShell):

PowerShell

python -m venv .venv
.venv\Scripts\Activate.ps1
Instala las dependencias:

Bash

pip install -r requirements.txt
Crea el archivo de entorno a partir del ejemplo (usando PowerShell):

PowerShell

Copy-Item .env.example .env
Aplica las migraciones para crear la base de datos:

Bash

python manage.py migrate
Ejecuta el servidor de desarrollo:

Bash

python manage.py runserver
La aplicación estará disponible en http://127.0.0.1:8000/.

⚙️ Configuración de variables de entorno
La configuración local se maneja mediante un archivo .env en la raíz del proyecto.

Variables comunes:

DJANGO_SECRET_KEY: clave secreta de Django.

DEBUG: True/False.

ALLOWED_HOSTS: hosts permitidos separados por comas.

DATABASE_ENGINE, DATABASE_NAME: (si usas SQLite por defecto no es estrictamente necesario cambiar).

USUARIO_DEMO_USERNAME, USUARIO_DEMO_EMAIL, USUARIO_DEMO_PASSWORD: valores para el usuario demo (si usas el comando create_demo_user).

.env.example (Plantilla)
Este es un ejemplo del contenido mínimo para tu archivo .env:

# Archivo: .env
DJANGO_SECRET_KEY= Reemplazar por la clave secreta de Django
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Base de datos
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3

🧪 Usuarios de Demostración
En este proyecto hay dos usuarios de demostración (credenciales proporcionadas):

1. Super Usuario (Admin)
Usuario: paciente-0

Contraseña: cachantun

2. Usuario Normal
Usuario: usuario_normal

Contraseña: Secreto123

⌨️ Cómo usar los usuarios demo
Accede a la página de login de la aplicación (habitualmente en /accounts/login/ o la ruta que defina ProyectoMesa).

Introduce el nombre de usuario y la contraseña de uno de los usuarios de demo anteriores.

Crear los usuarios manualmente (si no existen)
Si necesitas crear estas cuentas manualmente en una instalación nueva:

Abre la shell de Django:

Bash

python manage.py shell
Ejecuta los siguientes comandos:

Python

from django.contrib.auth import get_user_model
User = get_user_model()

User.objects.create_user('paciente-0', email='paciente0@gmail.com', password='cachantun')
User.objects.create_user('usuario_normal', email='usuario_normal@gmail.com', password='Secreto123')

exit()

⚠️ Notas importantes
No uses estas cuentas ni sus contraseñas en producción. Son únicamente para pruebas locales o demos.

Si tu app usa is_staff o permisos especiales para acceder al admin, revisa los flags de usuario (is_staff, is_superuser) y ajústalos si necesitas acceso al panel de administración.

Asegúrate de no commitear el archivo .env.

📦 Notas sobre migraciones
Las migraciones del app Mesa_de_Ayuda deben estar incluidas en Mesa_de_Ayuda/migrations/.

Antes de ejecutar el servidor en un entorno nuevo, asegúrate de:

Ejecutar python manage.py migrate para aplicar migraciones.

Si generas nuevas migraciones, usa python manage.py makemigrations y verifica los cambios.
