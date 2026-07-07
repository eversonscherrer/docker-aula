# A RECEITA (Dockerfile): instrucoes pra construir a imagem
FROM python:3.12-slim

WORKDIR /app

COPY app.py .

# /data e onde o volume vai ser montado (ver README)
EXPOSE 8080

CMD ["python", "app.py"]
