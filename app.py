from flask import Flask, request, jsonify
from db import conexao, init_db
from omdb_service import buscar_filme_nome, buscar_filme_id
import json

app = Flask(__name__)

@app.route('/buscar/nome', methods=['GET'])
def buscar_por_nome():
    nome = request.args.get('nome') 
    if not nome:
        return jsonify({"erro": "parametro 'nome' eh obrigatorio"}), 400 

    with conexao() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT dados FROM filmes_series WHERE titulo ILIKE %s;", (f'%{nome}%',)) 
            result = cur.fetchone()
            if result:
                return jsonify(result[0])

@app.route('/buscar/id', methods=['GET'])
def buscar_por_id():
    imdb_id = request.args.get('id') 
    if not imdb_id:
        return jsonify({"erro": "parametro 'id' eh obrigatorio"}), 400 

    # Busca o filme ou série pelo ID no banco de dados:
    with conexao() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT dados FROM filmes_series WHERE imdb_id = %s;", (imdb_id,)) 
            result = cur.fetchone()
            if result:
                return jsonify(result[0]) 
