import psycopg
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

# Função para estabelecer uma conexão com o banco de dados
def conexao():
    conn = psycopg.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    ) 
    return conn



# Função para iniciar o banco de dados, criando a tabela filmes_series SE NÃO EXISTIR
def iniciar_db():
    with conexao() as conn: 
        with conn.cursor() as cur: 
            cur.execute("""
                CREATE TABLE IF NOT EXISTS filmes_series (
                    id SERIAL PRIMARY KEY, 
                    imdb_id VARCHAR(20) UNIQUE,
                    titulo TEXT,
                    ano TEXT,
                    tipo TEXT,
                    dados JSONB,
                    total_temporadas INTEGER, 
                    idioma TEXT,
                    pais TEXT,
                    premios TEXT,
                    poster TEXT,
                    avaliacoes JSONB,
                    metascore TEXT,
                    avaliacao_imdb TEXT,
                    votos_imdb TEXT
                );
            """)
        conn.commit()