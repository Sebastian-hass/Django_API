<img width="1920" height="1080" alt="Django-API" src="https://github.com/user-attachments/assets/054fba68-3cd2-4de3-86a4-c9798398ec63" />

# 📝 Django REST API - BlogPosts

Este es un proyecto de API REST construida con Django y Django REST Framework para gestionar publicaciones de blog. El despliegue se realizó en [Render](https://render.com).

## 🚀 Deploy en Render

🌐 URL de producción:  
👉 [https://django-api-nqex.onrender.com/](https://django-api-nqex.onrender.com/)

---

## ⚙️ Tecnologías usadas

- Python 3.13
- Django 5.2
- Django REST Framework 3.16
- PostgreSQL (proporcionado por Render)
- Gunicorn (servidor WSGI en producción)
- WhiteNoise (servicio de archivos estáticos)
- dj-database-url (gestión de `DATABASE_URL`)
- Render (hosting gratuito con CI/CD)

---

## 🧪 Endpoints

| Método | URL                           | Descripción                     |
|--------|-------------------------------|---------------------------------|
| GET    | `/blogposts/`                 | Lista todas las publicaciones  |
| POST   | `/blogposts/`                 | Crea una nueva publicación     |
| GET    | `/blogposts/<id>/`            | Obtiene una publicación        |
| PUT    | `/blogposts/<id>/`            | Actualiza una publicación      |
| DELETE | `/blogposts/<id>/`            | Elimina una publicación        |

---

## 🛠️ Cómo ejecutar localmente

1. Clona el proyecto:

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

2. Crea un entorno virtual e instala dependencias:

```bash
python -m venv env
source env/bin/activate  # o env\Scripts\activate en Windows
pip install -r requirements.txt
```

3. Aplica migraciones y corre el servidor:

```bash
python manage.py migrate
python manage.py runserver
```

---

## 📦 Deploy en Render

1. Subir tu proyecto a GitHub.
2. En Render, crear un **Web Service** desde ese repo.
3. Configurar:

   - **Build Command:**
     ```bash
     pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
     ```

   - **Start Command:**
     ```bash
     gunicorn misitio.wsgi
     ```

4. Variables de entorno (Environment):
   - `DATABASE_URL`: (Render la genera si usas PostgreSQL)
   - `DEBUG=False`

5. Asegúrate de que Render esté sirviendo archivos estáticos desde `staticfiles/`.

---

## 📁 Estructura clave del proyecto

```
misitio/
│
├── api/
│   └── models.py, views.py, serializers.py, urls.py
│
├── misitio/
│   └── settings.py, urls.py, wsgi.py
│
├── manage.py
├── requirements.txt
└── staticfiles/
```

---

## 🧹 Notas

- Ejecutar `pip freeze > requirements.txt` luego de instalar nuevas dependencias como `gunicorn` o `whitenoise`.
- Ejecutar `python manage.py collectstatic` antes de desplegar.
- Usa la consola de Render para ejecutar comandos como `migrate` o `createsuperuser` en producción.

---

## 📫 Contacto

Si tienes dudas o sugerencias, abre un issue en el repositorio o escríbeme a [jesussebastianalonsoarias@gmail.com].
