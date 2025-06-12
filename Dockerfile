# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Establece directorio de trabajo en el contenedor
WORKDIR /app

# Copia requirements.txt y luego instala dependencias (asumiendo que tienes uno)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de tu proyecto
COPY . .

# Expone el puerto que usará Flask
EXPOSE 8080

# Comando para arrancar la app
CMD ["python", "app.py"]
