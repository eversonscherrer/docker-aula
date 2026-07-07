# Capitulo 02 — Historia do Docker

> Pratica baseada na aula **"Historia do Docker"**

## Slides da aula

📄 [`02-historia-do-docker.pdf`](./02-historia-do-docker.pdf)

## O que vai acontecer aqui?

Diferente do capitulo 1 (onde criamos nosso proprio servidor em Python),
agora vamos usar uma imagem **pronta do Docker Hub** — o `nginx`.

Isso demonstra na pratica o conceito de:
> **Docker Hub = mercado de imagens prontas**

---

## Passo a passo

### 1. Construir a imagem

```bash
docker build -t historia-docker .
```

O Docker vai buscar o `nginx:alpine` direto do **Docker Hub** (internet).
Voce vera algo como:

```
[+] Building ...
 => FROM nginx:alpine   ← baixando do Docker Hub
 => COPY index.html ... ← copiando nossa pagina
```

### 2. Rodar o container

```bash
docker run -p 80:80 historia-docker
```

### 3. Abrir no navegador

Acesse: http://localhost

Voce vera a timeline interativa da historia do Docker!

---

## Comparando com o Capitulo 01

| | Capitulo 01 | Capitulo 02 |
|---|---|---|
| Imagem base | `python:3.12-slim` | `nginx:alpine` |
| Codigo | servidor Python proprio | HTML estatico |
| Porta | 8080 | 80 |
| Conceito | criar imagem do zero | usar imagem do Docker Hub |

---

## Por que nginx:alpine?

- `nginx` — servidor web profissional (usado pela Netflix, Airbnb...)
- `alpine` — versao minima do Linux, imagem com menos de 10MB

```bash
# Compare o tamanho das imagens:
docker images
```

---

## Comandos extras

```bash
# Rodar em background
docker run -d -p 80:80 historia-docker

# Ver containers rodando
docker ps

# Parar o container
docker stop <ID>

# Ver o tamanho da imagem nginx:alpine
docker image inspect nginx:alpine --format '{{.Size}}'
```
