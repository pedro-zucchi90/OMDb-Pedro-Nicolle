# app.py
from flask import Flask, request, jsonify
from db import get_connection, init_db
from omdb_service import buscar_filme_nome, buscar_filme_id
import json

app = Flask(__name__)

@app.route('/buscar/nome', methods=['GET'])
def buscar_por_nome():
    nome = request.args.get('nome') #obtém o parâmetro 'nome' da requisição
    if not nome:
        return jsonify({"erro": "parametro 'nome' eh obrigatorio"}), 400 #se o parâmetro 'nome' não for fornecido retorna um erro (400 Bad Request)

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT dados FROM filmes_series WHERE titulo ILIKE %s;", (f'%{nome}%',)) #executa uma consulta SQL para buscar o filme ou série pelo nome NO BANCO DE DADOS
            result = cur.fetchone()
            if result:
                return jsonify(result[0]) #se encontrar um resultado no DB retorna os dados 

    # Se não achou no banco, busca na OMDB:
    data = buscar_filme_nome(nome)
    if data and data.get('Response') == 'True':
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""INSERT INTO filmes_series (imdb_id, titulo, ano, tipo, dados, total_temporadas, idioma, pais, premios, poster, avaliacoes, metascore, avaliacao_imdb, votos_imdb)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT (imdb_id) DO NOTHING;
                        """, (
                            data.get('imdbID'),
                            data.get('Title'),
                            data.get('Year'),
                            data.get('Type'),
                            json.dumps(data),  # dados gerais em json
                            data.get('totalSeasons'),
                            data.get('Language'),
                            data.get('Country'),
                            data.get('Awards'),
                            data.get('Poster'),
                            json.dumps(data.get('Ratings')),  #é lista -- salvar como json
                            data.get('Metascore'),
                            data.get('imdbRating'),
                            data.get('imdbVotes')
                        )) # Insere os dados do filme ou série na tabela filmes_series do DB
            conn.commit() #confirma as alterações no banco de dados
        return jsonify(data) #se encontrar um resultado na OMDB, retorna os dados do filme ou série
    else:
        return jsonify({"erro": "filme ou série nao encontrado"}), 404 #se não encontrar o filme ou série retorna um erro


#-----------------------------------------------------------------------------------------


@app.route('/buscar/id', methods=['GET'])
def buscar_por_id():
    imdb_id = request.args.get('id') #obtém o parâmetro 'id' da requisição
    if not imdb_id:
        return jsonify({"erro": "parametro 'id' eh obrigatorio"}), 400 #se o parâmetro 'id' não for fornecido retorna um erro (400 Bad Request)

    # Busca o filme ou série pelo ID no banco de dados:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT dados FROM filmes_series WHERE imdb_id = %s;", (imdb_id,)) #executa uma consulta SQL para buscar o filme ou série pelo ID
            result = cur.fetchone()
            if result:
                return jsonify(result[0]) #se encontrar um resultado, retorna os dados do filme ou série

    # Busca o filme ou série pela API do OMDB:
    data = buscar_filme_id(imdb_id)
    if data and data.get('Response') == 'True':
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""INSERT INTO filmes_series (imdb_id, titulo, ano, tipo, dados, total_temporadas, idioma, pais, premios, poster, avaliacoes, metascore, avaliacao_imdb, votos_imdb)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT (imdb_id) DO NOTHING;""", 
                            (
                            data.get('imdbID'),
                            data.get('Title'),
                            data.get('Year'),
                            data.get('Type'),
                            json.dumps(data),   #dados gerais em json
                            data.get('totalSeasons'),
                            data.get('Language'),
                            data.get('Country'),
                            data.get('Awards'),
                            data.get('Poster'),
                            json.dumps(data.get('Ratings')), #é lista -- salvar como json
                            data.get('Metascore'),
                            data.get('imdbRating'),
                            data.get('imdbVotes')
                        )) #insere os dados do filme ou série na tabela filmes_series
            conn.commit() #confirma as alterações no banco de dados
        return jsonify(data) #se encontrar um resultado na OMDB retorna os dados do filme ou série
    else:
        return jsonify({"erro": "filme ou serie nao encontrado"}), 404 #se não encontrar o filme ou série retorna um erro (404 Not Found)

if __name__ == '__main__':
    init_db() #inicializa o banco de dados
    app.run(debug=True) #executa a aplicação em flask
