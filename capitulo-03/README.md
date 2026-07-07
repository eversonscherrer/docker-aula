# Capitulo 03 — Docker vs Maquina Virtual

> Pratica baseada na aula **"Docker vs Maquina Virtual"**

## Slides da aula

📄 [`03-docker-vs-vm.pdf`](./03-docker-vs-vm.pdf)

## O que vai acontecer aqui?

Diferente dos capitulos anteriores (onde so subimos **um** container), aqui
vamos construir **duas versoes da mesma pagina** e comparar o resultado —
pra sentir na pele a diferenca de peso entre "so o essencial" e "um sistema
operacional completo por baixo do app":

| | `Dockerfile.leve` | `Dockerfile.pesado` |
|---|---|---|
| Imagem base | `nginx:alpine` (~40MB de SO) | `ubuntu:22.04` (~80MB de SO) + nginx instalado |
| Analogia da aula | 📦 Apartamento — so as libs do app | 🏠 Casa inteira — SO completo |

Nenhuma das duas e uma VM de verdade (ambas rodam como container Docker),
mas a diferenca de tamanho entre uma imagem minimalista e uma baseada em
SO completo e a **mesma logica** que faz uma VM (que sempre carrega um
kernel inteiro) ser muito mais pesada que um container bem construido.

---

## Passo a passo

### 1. Construir as duas imagens

```bash
docker build -f Dockerfile.leve -t site-leve .
docker build -f Dockerfile.pesado -t site-pesado .
```

### 2. Comparar o tamanho

```bash
docker images | grep site-
```

Repare quantas vezes a versao `pesado` e maior que a `leve`.

### 3. Comparar o tempo de subida

```bash
time docker run -d --name leve   -p 8080:80 site-leve
time docker run -d --name pesado -p 8081:80 site-pesado
```

### 4. Comparar o consumo de RAM

```bash
docker stats --no-stream leve pesado
```

### 5. Ver as duas paginas no navegador

- Versao leve: http://localhost:8080
- Versao pesada: http://localhost:8081

O conteudo e identico — a diferenca esta toda nos bastidores (tamanho,
tempo, RAM), exatamente como a tabela comparativa da aula mostra.

### 6. Limpar

```bash
docker rm -f leve pesado
```

---

## O que anotar no relatorio da turma

- Tamanho em MB de `site-leve` vs `site-pesado`
- Tempo (em segundos) que cada `docker run` levou
- RAM usada por cada container em `docker stats`
- Conclusao: por que uma VM real (que sempre carrega um SO completo, tipo
  a versao `pesado`) e ainda mais lenta e pesada que qualquer container?

---

## Comparando os 3 capitulos

| | Capitulo 01 | Capitulo 02 | Capitulo 03 |
|---|---|---|---|
| Imagem base | `python:3.12-slim` | `nginx:alpine` | `nginx:alpine` **vs** `ubuntu:22.04` |
| Conceito | criar imagem do zero | usar imagem do Docker Hub | medir o peso: leve vs pesado |
| Porta | 8080 | 80 | 8080 (leve) e 8081 (pesado) |

---

## Pergunta rapida da aula

Qual a principal vantagem de um container sobre uma VM?

- A) Tem mais recursos disponiveis
- B) E mais leve e rapido por compartilhar o kernel do SO host
- C) E mais seguro que qualquer outra coisa
- D) Funciona sem internet

<details>
<summary>Resposta</summary>

**B** — o container compartilha o kernel do sistema operacional host, por
isso e mais leve (MB em vez de GB) e liga em segundos em vez de minutos.
</details>
