# Ustawienie obrazu bazowego
FROM python:3.10-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie pliku requirements.txt i zainstalowanie zależności
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Skopiowanie reszty kodu aplikacji do kontenera
COPY . .

# Ustawienie zmiennej środowiskowej wskazującej Flaskowi, że działamy w trybie produkcyjnym
ENV FLASK_ENV=production

# Uruchomienie aplikacji Flask na porcie 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
