# Image de base
FROM python:3.10-slim

# Dossier de travail
WORKDIR /app

# Copier le code et les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Lancer l'application
CMD ["python", "app.py"]
