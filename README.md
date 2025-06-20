
# 🐾 Animales Masquefa - Plataforma de Adopción y Noticias 📰

> Un completo sistema web en Django para gestionar animales en adopción, publicar noticias, administrar comentarios y conectar con una comunidad solidaria.

## 📚 Documentación

Consulta la guía completa del proyecto, arquitectura, ejemplos de uso y más en:

👉 **[Ver en DeepWiki](https://deepwiki.com/DsevillanoNavarro/ProyectoDjango)**

---

## 🚀 Funcionalidades Principales

- 🐱 Gestión de animales: Crear, editar, eliminar y listar animales con imágenes y edad calculada automáticamente.
- 📰 Noticias: Publicación, edición y búsqueda de noticias con sistema de comentarios.
- 💬 Comentarios: Usuarios registrados pueden comentar y ver el tiempo transcurrido desde su publicación.
- 🏠 Adopciones: Solicitudes de adopción con validación de duplicados, y aceptación/rechazo por parte de administradores.
- 🔐 Sistema de usuarios: Registro, login/logout, panel de usuario personalizado.
- 🧑‍💼 Panel de administrador: Vista segura para gestionar todo el contenido de la web.
- 📄 Formularios inteligentes: Inputs con validaciones y calendarios.
- 🎨 Estilos personalizados con Bootstrap y CSS propio.

---

## 🧱 Estructura del Proyecto

```
dsevillanonavarro-proyectodjango/
├── proyectomustafa/
│   ├── appmustafa/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── templates/
│   │   ├── static/
│   └── settings/
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalación y Ejecución

1. **Clona el repositorio**  
```bash
git clone https://github.com/tuusuario/dsevillanonavarro-proyectodjango.git
cd dsevillanonavarro-proyectodjango
```

2. **Crea y activa un entorno virtual**  
```bash
python -m venv env
source env/bin/activate  # En Windows usa: env\Scripts\activate
```

3. **Instala las dependencias**  
```bash
pip install -r requirements.txt
```

4. **Configura tu base de datos y variables de entorno (.env)**  
Ejemplo:
```
DEBUG=True
SECRET_KEY=tu_clave_secreta
DB_NAME=masquefa
DB_USER=usuario
DB_PASSWORD=contraseña
```

5. **Migraciones y servidor**  
```bash
python manage.py migrate
python manage.py runserver
```

---

## 👤 Acceso al Panel de Administración

Visita `http://localhost:8000/admin` y crea un superusuario:

```bash
python manage.py createsuperuser
```

---

## 🤝 Contribuciones

¡Se aceptan contribuciones! Abre un *pull request* o sugiere mejoras vía *issues*.

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
