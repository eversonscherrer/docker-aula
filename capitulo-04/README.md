# Capitulo 04 — Conceitos Fundamentais

> Pratica baseada na aula **"Conceitos Fundamentais"** — Imagem, Container,
> Docker Hub, Volume e Dockerfile

## Slides da aula

📄 [`04-conceitos-fundamentais.pdf`](./04-conceitos-fundamentais.pdf)

## O que vai acontecer aqui?

Nos capitulos anteriores ja vimos **imagem**, **container**, **Docker Hub**
e **Dockerfile** na pratica. O conceito que falta sentir de verdade e o
**volume** — "o pen drive do container".

Vamos rodar um contador de visitas que salva o valor num arquivo. Primeiro
**sem** volume (pra ver os dados sumirem) e depois **com** volume (pra ver
os dados sobreviverem).

---

## Passo a passo

### 1. Construir a imagem

```bash
docker build -t contador-visitas .
```

### Etapa 1 — SEM volume (dados presos no container)

```bash
docker run -d -p 8080:8080 --name sem-volume contador-visitas
```

Acesse http://localhost:8080 varias vezes (ou de `curl http://localhost:8080`
umas 5 vezes) e veja o contador subir.

Agora **remova o container** e crie um novo, do zero:

```bash
docker rm -f sem-volume
docker run -d -p 8080:8080 --name sem-volume contador-visitas
```

Acesse http://localhost:8080 de novo.

> ⚠️ O contador **voltou pra 1**. Os dados moravam dentro do container, e
> quando ele foi removido, foram junto.

### Etapa 2 — COM volume (dados persistidos no host)

```bash
mkdir -p dados
docker rm -f sem-volume

docker run -d -p 8080:8080 -v "$(pwd)/dados:/data" --name com-volume contador-visitas
```

Acesse http://localhost:8080 varias vezes.

Agora remova o container e crie um novo, **usando o mesmo volume**:

```bash
docker rm -f com-volume
docker run -d -p 8080:8080 -v "$(pwd)/dados:/data" --name com-volume contador-visitas
```

Acesse http://localhost:8080 de novo.

> ✅ Dessa vez o contador **continuou de onde parou**. O arquivo
> `contador.txt` ficou salvo na pasta `dados/` da sua maquina (o host),
> nao dentro do container.

### 3. Ver o arquivo direto no host

```bash
cat dados/contador.txt
```

Esse e o mesmo arquivo que o container le e escreve — a prova de que o
volume conecta uma pasta do host com uma pasta de dentro do container.

### 4. Limpar

```bash
docker rm -f com-volume
```

---

## Conectando com os 5 conceitos da aula

| Conceito | Onde apareceu nesse exercicio |
|---|---|
| **Imagem** | `contador-visitas`, criada com `docker build` — o molde imutavel |
| **Container** | Cada `docker run` — uma instancia rodando da imagem |
| **Docker Hub** | De onde veio `python:3.12-slim`, a base da nossa imagem |
| **Dockerfile** | O arquivo `Dockerfile` — a receita que gerou a imagem |
| **Volume** | A pasta `dados/` — onde os dados sobreviveram a remocao do container |

---

## Pergunta rapida da aula

Qual a diferenca entre IMAGEM e CONTAINER?

- A) Sao a mesma coisa, so nomes diferentes
- B) Imagem e o molde (parado), Container e o molde rodando
- C) Container e mais antigo que imagem
- D) Imagem so funciona no Linux

<details>
<summary>Resposta</summary>

**B** — a imagem e o molde imutavel (read-only) com tudo que o app precisa;
o container e essa imagem em execucao, uma instancia viva e isolada.
</details>
