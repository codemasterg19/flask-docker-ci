
# Aplicación Flask Dockerizada con CI/CD

## Descripción del proyecto

Este proyecto consiste en una aplicación web simple desarrollada con Flask, containerizada mediante Docker y preparada para integración y entrega continua (CI/CD) usando GitHub Actions. El objetivo es demostrar buenas prácticas de desarrollo, pruebas automatizadas y despliegue eficiente usando contenedores.

## Tecnologías utilizadas

- Python 3
- Flask
- Docker
- Pytest
- GitHub Actions

## Estructura del proyecto

```
DOCKER_FLASK/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── test_app.py
├── README.md
└── .github/
    └── workflows/
        └── pipeline.yml
```

## Dockerfile

El Dockerfile define cómo se construye la imagen de la aplicación Flask. Instala las dependencias, copia el código fuente y configura el entorno para ejecutar la aplicación en el puerto 5000.

## Pipeline CI/CD

El pipeline ubicado en `.github/workflows/pipeline.yml` automatiza el proceso de integración y entrega continua. Realiza las siguientes tareas:
- Instala las dependencias del proyecto.
- Ejecuta las pruebas automatizadas con pytest.
- Construye la imagen Docker.
- Publica la imagen en Docker Hub como `pablocodem/flask-docker-ci:latest`.

## Imagen publicada en Docker Hub

La imagen generada por el pipeline se encuentra disponible en Docker Hub:

```
pablocodem/flask-docker-ci:latest
```

## Ejecución del proyecto

### 1. Descargar la imagen desde Docker Hub

Utiliza el siguiente comando para obtener la imagen:

```bash
docker pull pablocodem/flask-docker-ci:latest
```
Este comando descarga la última versión de la imagen desde Docker Hub.

### 2. Ejecutar el contenedor

Para iniciar la aplicación, ejecuta:

```bash
docker run -p 5000:5000 pablocodem/flask-docker-ci:latest
```
Este comando crea y ejecuta un contenedor, mapeando el puerto 5000 del contenedor al puerto 5000 de tu máquina local.

### 3. Acceder a la aplicación

Abre tu navegador y visita:

```
http://localhost:5000
```
Aquí podrás ver la aplicación Flask funcionando.

## Ejemplo de uso

1. Descarga la imagen:
   ```bash
   docker pull pablocodem/flask-docker-ci:latest
   ```
2. Ejecuta el contenedor:
   ```bash
   docker run -p 5000:5000 pablocodem/flask-docker-ci:latest
   ```
3. Accede a la aplicación en tu navegador:
   ```
   http://localhost:5000
   ```

## Conclusión

Este proyecto muestra cómo desarrollar, probar y desplegar una aplicación Flask usando Docker y CI/CD. La integración con GitHub Actions y Docker Hub permite un flujo de trabajo moderno, eficiente y automatizado.
