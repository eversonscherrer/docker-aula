# Docker na Pratica — Capitulo 1

> Pratica baseada na aula **"O que e Docker?"**

## Slides da aula

📄 [`01-o-que-e-docker.pdf`](./01-o-que-e-docker.pdf)

## O que tem aqui?

| Arquivo | O que e |
|---------|---------|
| `app.py` | Servidor web simples em Python |
| `Dockerfile` | A **receita** (imagem / caixa congelada) |

---

## Passo a passo

### 1. Construir a imagem (montar a caixa congelada)

```bash
docker build -t minha-pizza .
```

- `build` — cria a imagem seguindo o Dockerfile
- `-t minha-pizza` — da um nome pra imagem
- `.` — usa o Dockerfile do diretorio atual

### 2. Rodar o container (colocar a pizza no forno)

```bash
docker run -p 8080:8080 minha-pizza
```

- `run` — cria e inicia o container
- `-p 8080:8080` — mapeia a porta do container para a sua maquina

### 3. Abrir no navegador

Acesse: http://localhost:8080

### 4. Ver os containers rodando

```bash
docker ps
```

### 5. Parar o container

```bash
docker stop <ID_DO_CONTAINER>
```

---

## Analogia da pizza

```
Dockerfile  →  receita da pizza
docker build →  congelar a pizza (criar a imagem)
docker run   →  colocar no forno (rodar o container)
Docker Hub   →  mercado (onde ficam as imagens publicas)
```

---

## Comandos extras para explorar

```bash
# Ver todas as imagens que voce tem
docker images

# Rodar em background (modo detached)
docker run -d -p 8080:8080 minha-pizza

# Ver logs do container
docker logs <ID_DO_CONTAINER>

# Entrar dentro do container
docker exec -it <ID_DO_CONTAINER> sh
```
