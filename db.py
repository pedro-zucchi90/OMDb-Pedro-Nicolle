import psycopg
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

# Função para estabelecer uma conexão com o banco de dados
def get_connection():
    conn = psycopg.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    ) #estabelece uma conexão com o banco de dados utilizando as informações de configuração
    return conn

# Função para iniciar o banco de dados, criando a tabela filmes_series SE NÃO EXISTIR
def init_db():
    with get_connection() as conn: #abre uma conexão com o banco de dados
        with conn.cursor() as cur: #abre um cursor para executar comandos SQL
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
            """) #executa um comando SQL para criar a tabela filmes_series se ela não existir
        conn.commit()#confirma as alterações no banco de dados
