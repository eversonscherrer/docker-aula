# Capitulo 06 — Mao na Massa: Site no Nginx

> Pratica baseada na aula **"Mao na Massa: Site no Nginx"**

## Slides da aula

📄 [`06-projeto-nginx.pdf`](./06-projeto-nginx.pdf)

## O que vai acontecer aqui?

Voce vai subir o seu **proprio portfolio pessoal**, servido pelo Nginx
dentro de um container — e vai editar o site **ao vivo**, sem rebuild e
sem reiniciar nada.

Esse capitulo tambem **nao usa Dockerfile**: usamos a imagem oficial
`nginx` direto do Docker Hub e conectamos nossa pasta `site/` a ela com um
**bind mount** (`-v`). Repare como isso e diferente do que ja vimos:

| Capitulo | Como o HTML chega no container | O que acontece ao editar |
|---|---|---|
| 02 | `COPY` no Dockerfile (build-time) | Precisa `docker build` de novo pra ver a mudanca |
| 04 | Volume so pros **dados** gerados pela app | App escreve, volume guarda — nao e pra editar na mao |
| 05 | `docker exec` editando **dentro** do container | Muda na hora, mas some se o container for removido |
| **06** | **Bind mount** (`-v ./site:/usr/share/nginx/html`) | Muda na hora **e** fica salvo no seu PC, sobrevive a qualquer `docker rm` |

---

## Passo a passo

### 1. Personalize o seu portfolio

Abra `site/index.html` e troque:
- `TROQUE PELO SEU NOME` pelo seu nome
- A frase "Sobre mim" por algo seu

Fique com o navegador fechado por enquanto — vamos ver a magica acontecer
depois que o container estiver no ar.

### 2. Subir o container (o comando magico)

```bash
# Linux / macOS
docker run -d --name meu-portfolio -p 8080:80 \
  -v "$(pwd)/site:/usr/share/nginx/html" nginx

# Windows PowerShell
docker run -d --name meu-portfolio -p 8080:80 `
  -v "${PWD}/site:/usr/share/nginx/html" nginx
```

- `-d` → segundo plano
- `-p 8080:80` → mapeia a porta
- `-v ...` → conecta a pasta `site/` do seu PC ao container (bind mount)

### 3. Acessar

Abra http://localhost:8080 — o seu portfolio personalizado deve aparecer.

### 4. Explorar o container

```bash
docker ps                              # ve se ta rodando
docker logs meu-portfolio              # ve o que o nginx ta fazendo
docker stats --no-stream meu-portfolio # CPU/RAM em tempo real
docker exec -it meu-portfolio bash     # entrar dentro
  ls /usr/share/nginx/html             # ver os arquivos (sao os seus!)
  exit                                 # sair
```

### 5. A magica do volume — teste sem parar o container

Com o container **rodando**, abra `site/index.html` de novo, mude o texto
do "Sobre mim" e salve. Atualize o navegador.

- [ ] A mudanca apareceu **sem** rodar nenhum comando docker

Agora remova o container e crie outro:

```bash
docker rm -f meu-portfolio
docker run -d --name meu-portfolio -p 8080:80 \
  -v "$(pwd)/site:/usr/share/nginx/html" nginx
```

- [ ] A sua edicao **continua la** — diferente do capitulo 5, porque dessa
      vez o arquivo sempre morou no seu PC, nunca dentro do container

### 6. Ciclo de vida

```bash
docker stop meu-portfolio
docker start meu-portfolio
docker rm -f meu-portfolio
```

---

## Pergunta rapida da aula

Por que usamos o flag `-v` no `docker run`?

- A) Pra rodar em modo verboso (verbose)
- B) Pra criar uma VM
- C) Pra mapear uma pasta do PC para uma pasta dentro do container (volume)
- D) Pra mostrar a versao do container

<details>
<summary>Resposta</summary>

**C** — o `-v origem:destino` cria uma ponte entre uma pasta do seu PC
(host) e uma pasta dentro do container. No nosso caso, `site/` (host) foi
conectada a `/usr/share/nginx/html` (container).
</details>

---

## Comparando os capitulos praticos

| | 01 | 02 | 03 | 04 | 05 | 06 |
|---|---|---|---|---|---|---|
| Dockerfile? | Sim | Sim | Sim (x2) | Sim | Nao | Nao |
| Conceito central | criar imagem | usar imagem do Hub | comparar peso | volume de dados | comandos + exec | bind mount pra dev ao vivo |
