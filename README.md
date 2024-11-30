# Biblioteca Virtual

Este es un proyecto de una biblioteca virtual utilizando Flask y SQLite.

## Requisitos

- Python 3.6 o superior
- pipenv (gestor de entornos virtuales y dependencias)

## Instalación

### Linux y Mac

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/biblioteca-virtual.git
    cd biblioteca-virtual
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```bash
    pipenv install
    ```

3. Activa el entorno virtual:
    ```bash
    pipenv shell
    ```

4. Ejecuta la aplicación:
    ```bash
    python app.py
    ```

### Windows

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/biblioteca-virtual.git
    cd biblioteca-virtual
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```bash
    pipenv install
    ```

3. Activa el entorno virtual:
    ```bash
    pipenv shell
    ```

4. Ejecuta la aplicación:
    ```bash
    python app.py
    ```

## Uso

1. Abre tu navegador web y navega a `http://127.0.0.1:5000/`.
2. Usa el formulario de inicio de sesión para acceder como administrador (usuario: `admin`, contraseña: `admin`).
3. Puedes buscar libros, agregar nuevos libros, actualizar información de libros existentes y eliminar libros.

## Estructura del Proyecto

```zsh
biblioteca-virtual/
│
├── Pipfile
├── [Pipfile.lock](http://_vscodecontentref_/2)
├── [README.md](http://_vscodecontentref_/3)
├── [app.py](http://_vscodecontentref_/4)
├── instance
│   └── library.db
├── model
│   └── book.py
└── templates
    ├── add.html
    ├── all.html
    ├── base.html
    ├── home.html
    ├── login.html
    ├── search.html
    └── update.html