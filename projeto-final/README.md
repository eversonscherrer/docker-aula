# Projeto Final — Livro de Visitas com Docker Compose

> Junta tudo que voce aprendeu nos 7 capitulos num projeto so, e introduz
> a peca que faltava: **Docker Compose**.

## O que e esse projeto?

Um **livro de visitas** (guestbook): qualquer pessoa deixa um nome e uma
mensagem, e todas as mensagens ficam salvas e visiveis pra sempre — mesmo
se voce desligar e ligar os containers de novo.

Por baixo, sao **3 containers** conversando entre si:

```
                 ┌──────────────────────────────────────────┐
 Browser  ─────▶ │  web (nginx)         :8080 exposto        │
                 │  serve o HTML/CSS/JS                      │
                 │  e repassa /api/* pro container "api"     │
                 └───────────────┬────────────────────────────┘
                                 │ rede interna do Compose
                 ┌───────────────▼────────────────────────────┐
                 │  api (Flask/Python)  so existe na rede      │
                 │  recebe e devolve as mensagens em JSON      │
                 └───────────────┬────────────────────────────┘
                                 │ rede interna do Compose
                 ┌───────────────▼────────────────────────────┐
                 │  db (PostgreSQL)     dados no volume         │
                 │  guarda as mensagens permanentemente        │
                 └──────────────────────────────────────────┘
```

Repare: so o `web` expoe uma porta pro seu PC (`8080`). O `api` e o `db`
so conversam **entre si**, dentro da rede que o Docker Compose cria
automaticamente — e se enxergam pelo **nome do servico** (`db`, `api`),
nao por IP. Isso e Networking na pratica (o proximo passo que o
capitulo 7 sugeriu).

## Conectando com os capitulos anteriores

| Conceito | Capitulo onde apareceu | Onde esta aqui |
|---|---|---|
| Dockerfile / imagem propria | 01 | `backend/Dockerfile` |
| Imagem pronta do Docker Hub | 02, 05 | `postgres:16-alpine` |
| Volume pra persistir dados | 04 | `dados_db` guardando o banco |
| Bind mount pra dev ao vivo | 06 | `./frontend/site` no servico `web` |
| Comandos do dia a dia | 05 | `docker compose ps/logs/exec` |
| Debug de erros | 07 | secao de troubleshooting abaixo |
| **Novo:** orquestrar tudo junto | — | `docker-compose.yml` |

---

## Passo a passo

### 1. Configurar as variaveis de ambiente

```bash
cp .env.example .env
```

(Pode deixar os valores padrao — e so um projeto de estudo.)

### 2. Subir tudo com um comando so

```bash
docker compose up --build -d
```

Isso constroi as imagens de `api` e `web`, baixa o `postgres:16-alpine`
do Docker Hub, cria a rede interna e sobe os 3 containers na ordem certa
(o `api` espera o `db` ficar saudavel antes de iniciar).

### 3. Acessar

Abra http://localhost:8080, escreva seu nome e uma mensagem, e mande.

- [ ] A mensagem aparece na lista logo abaixo
- [ ] Recarregando a pagina (F5), a mensagem continua la

### 4. Explorar os containers

```bash
docker compose ps                 # os 3 servicos rodando
docker compose logs -f api        # logs do backend em tempo real
docker compose exec db psql -U docker -d guestbook -c "SELECT * FROM mensagens;"
```

### 5. Provar que o volume funciona (capitulo 4 na pratica)

```bash
docker compose down     # remove os containers (mas NAO o volume)
docker compose up -d    # sobe tudo de novo
```

- [ ] As mensagens antigas **continuam la** — elas moram no volume
      `dados_db`, nao no container

Agora o teste contrario:

```bash
docker compose down -v  # -v remove TAMBEM os volumes
docker compose up -d
```

- [ ] Dessa vez o livro de visitas volta **vazio** — o volume foi apagado
      junto com o `-v`

### 6. Editar o frontend ao vivo (capitulo 6 na pratica)

Com os containers rodando, edite `frontend/site/style.css` (troque uma
cor, por exemplo), salve e atualize o navegador.

- [ ] A mudanca aparece na hora, sem rebuild — o `web` usa bind mount
      igual ao capitulo 6

### 7. Desligar tudo

```bash
docker compose down
```

---

## Troubleshooting (capitulo 7 na pratica)

| Sintoma | Causa provavel | Solucao |
|---|---|---|
| `api` fica reiniciando | Banco ainda nao estava pronto | O `app.py` ja espera o banco (`esperar_banco()`), mas confira `docker compose logs api` |
| `port is already allocated` no `web` | Porta 8080 ja em uso | Troque `"8080:80"` por `"8081:80"` no `docker-compose.yml` |
| Editei o CSS e nao mudou nada | Container antigo, cache do navegador | De um refresh forcado (Ctrl+Shift+R) |
| `docker compose up` reclama de variavel vazia | Esqueceu de criar o `.env` | Rode `cp .env.example .env` |

---

## Comandos novos que voce aprendeu aqui

| Comando | O que faz |
|---|---|
| `docker compose up --build -d` | Constroi e sobe todos os servicos |
| `docker compose ps` | Lista os servicos do projeto |
| `docker compose logs -f <servico>` | Acompanha os logs de um servico |
| `docker compose exec <servico> <cmd>` | Executa um comando dentro de um servico |
| `docker compose down` | Para e remove os containers (mantem volumes) |
| `docker compose down -v` | Para e remove containers **e** volumes |

🎉 Com isso, voce fechou o ciclo completo: **imagem → container → volume
→ rede → varios containers trabalhando juntos**. Isso e, na pratica, como
a maioria dos sistemas reais roda em producao hoje em dia.
