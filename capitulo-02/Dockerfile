# Baixamos o nginx direto do Docker Hub (o "mercado de imagens")
FROM nginx:alpine

# Copiamos nossa pagina HTML para dentro do container
COPY index.html /usr/share/nginx/html/index.html

# O nginx ja expoe a porta 80 por padrao
EXPOSE 80
