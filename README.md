# Docker na Pratica — Ensino Medio Tecnico

Praticas hands-on baseadas no curso **Docker na Pratica** (7 capitulos).

## Estrutura

| Pasta | Aula | Conceito principal |
|-------|------|--------------------|
| [capitulo-01/](capitulo-01/) | O que e Docker? | Criar sua primeira imagem |
| [capitulo-02/](capitulo-02/) | Historia do Docker | Usar imagem do Docker Hub (nginx) |
| [capitulo-03/](capitulo-03/) | Docker vs Maquina Virtual | Comparar Docker e VM na pratica |
| [capitulo-04/](capitulo-04/) | Conceitos Fundamentais | Persistencia de dados com Volumes |
| [capitulo-05/](capitulo-05/) | Instalacao & Comandos | Roteiro de comandos + editar container ao vivo com `exec` |
| [capitulo-06/](capitulo-06/) | Mao na Massa: Site no Nginx | Portfolio pessoal com bind mount (`-v`) pra dev ao vivo |
| [capitulo-07/](capitulo-07/) | Erros Comuns, Curiosidades & DevOps | Desafio de debug: provocar e consertar os erros classicos |

## Projeto Final

| Pasta | O que e |
|-------|---------|
| [projeto-final/](projeto-final/) | Livro de visitas com **Docker Compose**: frontend (nginx) + API (Flask) + banco (PostgreSQL), 3 containers orquestrados juntos, juntando tudo dos 7 capitulos |

## Como comecar

1. Instale o [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Clone o repositorio:
   ```bash
   git clone https://github.com/eversonscherrer/docker-aula.git
   cd docker-aula
   ```
3. Entre na pasta do capitulo desejado e siga o README.
