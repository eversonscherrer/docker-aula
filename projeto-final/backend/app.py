import os
import time

import psycopg2
from flask import Flask, jsonify, request
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_NAME = os.environ.get("DB_NAME", "guestbook")
DB_USER = os.environ.get("DB_USER", "docker")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "docker")


def conectar():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        cursor_factory=RealDictCursor,
    )


def esperar_banco(tentativas=10, espera_segundos=2):
    for tentativa in range(1, tentativas + 1):
        try:
            conexao = conectar()
            conexao.close()
            return
        except psycopg2.OperationalError:
            print(f"Banco ainda nao esta pronto ({tentativa}/{tentativas})...")
            time.sleep(espera_segundos)
    raise RuntimeError("Nao foi possivel conectar ao banco de dados")


def criar_tabela():
    conexao = conectar()
    with conexao, conexao.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS mensagens (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(80) NOT NULL,
                mensagem VARCHAR(280) NOT NULL,
                criado_em TIMESTAMP DEFAULT NOW()
            )
            """
        )
    conexao.close()


esperar_banco()
criar_tabela()


@app.route("/mensagens", methods=["GET"])
def listar_mensagens():
    conexao = conectar()
    with conexao.cursor() as cursor:
        cursor.execute(
            "SELECT nome, mensagem, criado_em FROM mensagens ORDER BY id DESC LIMIT 50"
        )
        mensagens = cursor.fetchall()
    conexao.close()
    return jsonify(mensagens)


@app.route("/mensagens", methods=["POST"])
def criar_mensagem():
    dados = request.get_json(silent=True) or {}
    nome = (dados.get("nome") or "").strip()[:80]
    mensagem = (dados.get("mensagem") or "").strip()[:280]

    if not nome or not mensagem:
        return jsonify({"erro": "nome e mensagem sao obrigatorios"}), 400

    conexao = conectar()
    with conexao, conexao.cursor() as cursor:
        cursor.execute(
            "INSERT INTO mensagens (nome, mensagem) VALUES (%s, %s)",
            (nome, mensagem),
        )
    conexao.close()
    return jsonify({"ok": True}), 201


@app.route("/saude", methods=["GET"])
def saude():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
