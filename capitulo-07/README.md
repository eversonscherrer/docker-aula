# Capitulo 07 — Erros Comuns, Curiosidades & DevOps

> Pratica baseada na aula **"Erros Comuns, Curiosidades & DevOps"** — o
> capitulo final do curso!

## Slides da aula

📄 [`07-erros-curiosidades-devops.pdf`](./07-erros-curiosidades-devops.pdf)

## O que vai acontecer aqui?

Esse e o **ultimo capitulo**, entao a pratica e diferente de todas as
anteriores: em vez de construir algo novo, voce vai **provocar de
proposito** os 5 erros mais comuns da aula, ver a mensagem de erro
de verdade, e corrigir. E um "modo debug" — revisando tudo que voce
aprendeu nos capitulos 1 a 6.

Nao tem Dockerfile nem app nova. So terminal e as imagens que voce ja
conhece (`nginx`, `ubuntu`).

---

## Desafio: provoque e conserte os 5 erros

### Erro 1 — Esquecer de mapear a porta

```bash
docker run -d --name teste-porta nginx
```

- [ ] Tente abrir http://localhost:8080 — nao vai funcionar. Por que?
      (dica: rode `docker port teste-porta` e veja que porta nenhuma foi
      mapeada)

**Conserte:**

```bash
docker rm -f teste-porta
docker run -d --name teste-porta -p 8080:80 nginx
```

- [ ] Agora http://localhost:8080 funciona

### Erro 2 — Esquecer de dar nome

```bash
docker run -d -p 8081:80 nginx
```

- [ ] Rode `docker ps` e repare no nome aleatorio gerado (tipo
      `naughty_einstein`)

**Conserte:** remova esse container e recrie com `--name`:

```bash
docker rm -f <nome-aleatorio-que-apareceu>
docker run -d --name site-nomeado -p 8081:80 nginx
```

### Erro 3 — Porta ja em uso

```bash
docker run -d --name outro-site -p 8081:80 nginx
```

- [ ] Deu erro `port is already allocated`? Isso porque a porta 8081 ja
      esta ocupada pelo `site-nomeado` do passo anterior.

**Conserte:** troque a porta do host:

```bash
docker run -d --name outro-site -p 8082:80 nginx
```

- [ ] Agora http://localhost:8082 funciona ao lado do 8081

### Erro 4 — Remover container ativo sem `-f`

```bash
docker rm outro-site
```

- [ ] Deu erro `cannot remove running container`? Faz sentido — ele ainda
      esta rodando.

**Conserte** de duas formas possiveis:

```bash
docker stop outro-site && docker rm outro-site
# OU, direto:
docker rm -f outro-site
```

### Erro 5 — Confundir imagem com container

```bash
docker images
docker ps -a
```

- [ ] Quantas **imagens** (`nginx`) aparecem em `docker images`?
- [ ] Quantos **containers** aparecem em `docker ps -a` (mesmo os parados)?

Voce deve ver **1 imagem** `nginx`, mas **varios containers** diferentes
(`teste-porta`, `site-nomeado`, etc) — todos criados a partir da mesma
imagem. Essa e a diferenca na pratica: imagem e o molde, container e cada
instancia dele.

### Bonus — Container que morre sozinho

```bash
docker run --name ubuntu-teste ubuntu
docker ps -a
```

- [ ] Repare que o `ubuntu-teste` aparece como `Exited` quase que
      instantaneamente. O Ubuntu sozinho nao tem nenhum processo pra ficar
      rodando em primeiro plano.

**Conserte** rodando interativo:

```bash
docker rm ubuntu-teste
docker run -it --name ubuntu-teste ubuntu bash
# voce esta dentro do Ubuntu! rode: ls, whoami, exit
```

---

## Limpeza final

Depois do desafio, sua maquina deve estar cheia de containers e imagens de
teste. Confira e limpe:

```bash
docker ps -a
docker images

# Remove todos os containers parados, redes e imagens sem uso:
docker system prune -a
```

- [ ] `docker ps -a` e `docker images` voltaram limpos (ou quase)

---

## Pergunta rapida da aula

Qual ferramenta orquestra MUITOS containers Docker em producao?

- A) Docker Hub
- B) Kubernetes (K8s)
- C) Visual Studio Code
- D) Git

<details>
<summary>Resposta</summary>

**B** — o Kubernetes (K8s) e o "porto" que organiza milhares de containers
Docker rodando ao mesmo tempo, cuidando de escala, rede e recuperacao de
falhas.
</details>

---

## Pra onde ir depois

1. **Domine o Dockerfile** — `FROM`, `RUN`, `COPY`, `CMD` (ja praticado nos
   capitulos 01-04)
2. **Aprenda Docker Compose** — rodar varios containers com um comando so
3. **Estude Networking** — como containers conversam entre si
4. **Conheca o Kubernetes** — orquestracao em escala
5. **Pratique CI/CD** — GitHub Actions, GitLab CI, Jenkins

---

## Resumo do curso — Docker na Pratica

| Capitulo | Tema | O que ficou |
|---|---|---|
| 01 | O que e Docker? | Criar sua primeira imagem |
| 02 | Historia do Docker | Usar imagem do Docker Hub |
| 03 | Docker vs VM | Medir peso: leve vs pesado |
| 04 | Conceitos Fundamentais | Volumes e persistencia de dados |
| 05 | Instalacao & Comandos | Ciclo de vida do container + `exec` |
| 06 | Mao na Massa: Nginx | Bind mount pra desenvolvimento ao vivo |
| 07 | Erros, Curiosidades & DevOps | Debugar os erros mais comuns |

🎉 **Parabens!** Voce praticou uma das skills mais valorizadas do mercado
de TI. Agora e treinar: erre, conserte, repita.
