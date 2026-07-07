# Capitulo 05 — Instalacao & Comandos

> Pratica baseada na aula **"Instalacao & Comandos"**

## Slides da aula

📄 [`05-instalacao-comandos.pdf`](./05-instalacao-comandos.pdf)

## O que vai acontecer aqui?

Diferente de todos os capitulos anteriores, **esse aqui nao tem Dockerfile**.
A aula 5 e sobre os **comandos**, entao a pratica e um roteiro guiado — um
checklist pra rodar no terminal, usando so imagens prontas do Docker Hub.

O destaque desse capitulo e o `docker exec`: voce vai **entrar dentro de um
container rodando** e editar um arquivo ao vivo, sem precisar rebuildar
nada.

---

## Roteiro — marque cada item conforme for fazendo

### 1. Confirmar a instalacao

```bash
docker --version
```

- [ ] Apareceu a versao do Docker (ex: `Docker version 27.x`)

### 2. Seu primeiro container

```bash
docker run hello-world
```

- [ ] Apareceu a mensagem "Hello from Docker!"

### 3. Baixar uma imagem do Hub

```bash
docker pull nginx:alpine
```

- [ ] A imagem `nginx:alpine` aparece em `docker images`

### 4. Rodar o container (o "canivete suico")

```bash
docker run -d --name meu-web -p 8080:80 nginx:alpine
```

- [ ] `docker ps` mostra o container `meu-web` rodando
- [ ] http://localhost:8080 abre a pagina padrao do nginx

### 5. Ver os logs

```bash
docker logs meu-web
```

- [ ] Apareceu pelo menos uma linha de log (o acesso que voce acabou de fazer)

### 6. Entrar no container e editar ao vivo (`docker exec`)

```bash
docker exec -it meu-web sh
```

Agora voce esta **dentro** do container. Rode:

```sh
echo "<h1>Editado por dentro do container!</h1>" > /usr/share/nginx/html/index.html
exit
```

- [ ] Ao atualizar http://localhost:8080, a pagina mudou pro seu texto

### 7. Parar e iniciar de novo

```bash
docker stop meu-web
docker start meu-web
```

- [ ] Depois do `start`, a pagina em http://localhost:8080 **continua**
      com o texto editado (o container e o mesmo, so pausou e voltou)

### 8. Remover o container e criar um novo

```bash
docker rm -f meu-web
docker run -d --name meu-web -p 8080:80 nginx:alpine
```

- [ ] Agora a pagina **voltou a ser a padrao do nginx** — sua edicao sumiu

> 💡 Reparou? A edicao feita com `exec` morava **dentro do container**, nao
> na imagem nem num volume. Assim que o container foi removido, a edicao
> foi junto — o mesmo principio do capitulo 4 (Volumes), so que agora
> aplicado a arquivos editados na mao em vez de dados gerados pela app.

### 9. Limpar tudo

```bash
docker rm -f meu-web
docker images
docker rmi nginx:alpine
```

- [ ] `docker ps -a` nao mostra mais o `meu-web`
- [ ] `docker images` nao mostra mais o `nginx:alpine`

---

## Cheat sheet usado nesse roteiro

| Acao | Comando |
|---|---|
| Verificar versao | `docker --version` |
| Baixar imagem | `docker pull <imagem>` |
| Rodar container | `docker run -d --name <nome> -p 8080:80 <imagem>` |
| Listar ativos | `docker ps` |
| Listar todos | `docker ps -a` |
| Ver logs | `docker logs <nome>` |
| Entrar dentro | `docker exec -it <nome> sh` |
| Parar | `docker stop <nome>` |
| Iniciar | `docker start <nome>` |
| Remover container | `docker rm -f <nome>` |
| Listar imagens | `docker images` |
| Remover imagem | `docker rmi <imagem>` |

---

## Pergunta rapida da aula

O que faz a flag `-p 8080:80` no comando `docker run`?

- A) Define que o container vai usar 8080 MB de RAM
- B) Mapeia a porta 8080 do PC para a porta 80 do container
- C) Define a prioridade do processo
- D) Roda o container em modo paralelo

<details>
<summary>Resposta</summary>

**B** — `-p <porta do host>:<porta do container>` mapeia uma porta da sua
maquina para a porta que o processo escuta dentro do container.
</details>
