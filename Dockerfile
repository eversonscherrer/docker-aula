# A CAIXA (imagem): receita de como montar o container
FROM python:3.12-slim

# Define o diretorio de trabalho dentro do container
WORKDIR /app

# Copia o codigo para dentro da imagem
COPY app.py .

# Expoe a porta que o servidor usa
EXPOSE 8080

# Comando que roda quando o container (pizza) vai pro forno
CMD ["python", "app.py"]
