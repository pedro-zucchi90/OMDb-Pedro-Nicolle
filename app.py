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
    # Se não achou no banco, busca na OMDB:
    data = buscar_filme_nome(nome)
    if data and data.get('Response') == 'True':
        with conexao() as conn:
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
                            json.dumps(data.get('Ratings')),
                            data.get('Metascore'),
                            data.get('imdbRating'),
                            data.get('imdbVotes')
                        ))
            conn.commit()
        return jsonify(data)
    else:
        return jsonify({"erro": "filme ou série nao encontrado"}), 404

#---------------------------------------------------------------------

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

        # Busca o filme ou série pela API do OMDB:
    data = buscar_filme_id(imdb_id)
    if data and data.get('Response') == 'True':
        with conexao() as conn:
            with conn.cursor() as cur:
                cur.execute("""INSERT INTO filmes_series (imdb_id, titulo, ano, tipo, dados, total_temporadas, idioma, pais, premios, poster, avaliacoes, metascore, avaliacao_imdb, votos_imdb)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT (imdb_id) DO NOTHING;""", 
                            (
                            data.get('imdbID'),
                            data.get('Title'),
                            data.get('Year'),
                            data.get('Type'),
                            json.dumps(data),   
                            data.get('totalSeasons'),
                            data.get('Language'),
                            data.get('Country'),
                            data.get('Awards'),
                            data.get('Poster'),
                            json.dumps(data.get('Ratings')), 
                            data.get('Metascore'),
                            data.get('imdbRating'),
                            data.get('imdbVotes')
                        )) 
            conn.commit() 
        return jsonify(data) 
    else:
        return jsonify({"erro": "filme ou serie nao encontrado"}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True) 
