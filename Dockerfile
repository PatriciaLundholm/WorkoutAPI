# 1. Basimage
FROM python:3.11-slim

# 2. Sätt arbetskatalog
WORKDIR /app

# 3. Kopiera requirements
COPY requirements.txt .

# 4. Installera dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kopiera all kod
COPY . .

# 6. Exponera port
EXPOSE 8000

# 7. Kör uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
