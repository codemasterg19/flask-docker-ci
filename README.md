# Docker Flask App

Este es un proyecto básico de una aplicación Flask que se ejecuta en Docker y está preparado para CI/CD con GitHub Actions.

## Requisitos
- Python 3.x
- Docker

## Instalación y ejecución local

1. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En Linux/Mac:
   source .venv/bin/activate
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación Flask:
   ```bash
   flask run
   ```
   La aplicación estará disponible en http://localhost:5000

## Pruebas automáticas

Para ejecutar las pruebas con pytest:
```bash
pytest
```

## Construir la imagen Docker

```bash
docker build -t docker-flask-app .
```

## Ejecutar el contenedor Docker

```bash
docker run -p 5000:5000 docker-flask-app
```

La aplicación estará disponible en http://localhost:5000

## CI/CD

El proyecto incluye un pipeline de ejemplo con GitHub Actions para pruebas y construcción de la imagen Docker.
