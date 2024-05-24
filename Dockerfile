# Usa una imagen de Python
FROM python:3.9

# Copia los archivos de tu aplicación al contenedor
COPY . /app

RUN apt-get update && apt-get install -y libmysqlclient-dev
# Instala las dependencias de Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Establece el directorio de trabajo
WORKDIR /app

# Ejecuta la aplicación FastAPI con Uvicorn en el puerto 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
