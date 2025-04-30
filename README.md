<h1 style="text-align: center;">API: Cache de Filmes e Séries com OMDb</h1>

<p style="text-align: center;">Desenvolvimento Web — Turma 3F</p>

<p>Este projeto consiste em uma API feita com Flask que permite <strong>buscar filmes e séries</strong> pelo nome ou pelo ID do IMDb.</p>
<p>Os dados são consultados primeiro em um <strong>banco de dados PostgreSQL</strong>. Caso não estejam armazenados, a API consulta a <strong>OMDb API</strong> e salva os resultados para buscas futuras.</p>

<hr>

<h2 style="text-align: center;">Tecnologias utilizadas</h2>
<ul>
  <li>Python 3</li>
  <li>Flask</li>
  <li>PostgreSQL</li>
  <li>psycopg</li>
  <li>requests</li>
  <li>OMDB API</li>
</ul>

<hr>

<h2 style="text-align: center;">Estrutura do projeto</h2>
<pre><code>
|-- app.py               # Código principal do Flask
|-- db.py                # Conexão e inicialização do banco de dados
|-- omdb_service.py      # Comunicação com a API OMDB
|-- config.py            # Configurações (chave da API OMDB, informações do banco)
|-- requirements.txt     # Dependências do projeto
|-- README.md            # Documentação do projeto
</code></pre>

<hr>

<h2 style="text-align: center;">Configuração do ambiente</h2>
<ol>
  <li><strong>Clone o repositório</strong>
    <pre><code>git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio</code></pre>
  </li>

  <li><strong>Crie e ative o ambiente virtual (.venv)</strong>
    <pre><code>python -m venv .venv</code></pre>
    <p><strong>No Windows:</strong></p>
    <pre><code>.venv\Scripts\activate</code></pre>
    <p><strong>No Linux/Mac:</strong></p>
    <pre><code>source .venv/bin/activate</code></pre>
  </li>

  <li><strong>Instale as dependências</strong>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>

  <li><strong>Configure o arquivo <code>config.py</code></strong>
    <p>Crie um arquivo <code>config.py</code> na raiz do projeto com o seguinte conteúdo:</p>
    <pre><code>DB_NAME = 'seu_banco'
DB_USER = 'seu_usuario'
DB_PASSWORD = 'sua_senha'
DB_HOST = 'localhost'
DB_PORT = '5432'

OMDB_API_KEY = 'sua_chave_omdb'</code></pre>
    <p>Você pode obter sua chave da OMDB em: 
    <a href="http://www.omdbapi.com/apikey.aspx" target="_blank">http://www.omdbapi.com/apikey.aspx</a></p>
  </li>

  <li><strong>Configure o banco de dados PostgreSQL</strong>
    <p>Certifique-se de que o PostgreSQL esteja rodando localmente.</p>
    <p>O projeto automaticamente cria a tabela <code>filmes_series</code> ao iniciar.</p>
  </li>
</ol>

<hr>

<h2 style="text-align: center;">Executando a aplicação</h2>

<p style="text-align: center;"><strong>No terminal da pasta do projeto:</strong></p>
<pre style="text-align: center;"><code>python app.py</code></pre>

<p style="text-align: center;">Acesse em:</p>
<pre style="text-align: center;"><code>http://localhost:5000</code></pre>

<hr>

<h2 style="text-align: center;">Fluxo geral de funcionamento</h2>

<h3>/buscar/nome</h3>
<ol>
  <li>Valida o parâmetro <code>nome</code></li>
  <li>Consulta local com <code>ILIKE</code></li>
  <li>Se não encontrado:
    <ul>
      <li>Consulta OMDb</li>
      <li>Se encontrado, armazena e retorna</li>
      <li>Se não, retorna 404</li>
    </ul>
  </li>
</ol>

<h3>/buscar/id</h3>
<ol>
  <li>Valida o parâmetro <code>id</code></li>
  <li>Consulta local</li>
  <li>Se não encontrado:
    <ul>
      <li>Consulta OMDb</li>
      <li>Se encontrado, armazena e retorna</li>
      <li>Se não, retorna 404</li>
    </ul>
  </li>
</ol>

<hr>

<h2 style="text-align: center;">Explicação do Sistema</h2>

<h3><code>app.py</code></h3>
<p>Este arquivo define as rotas principais para a busca de filmes ou séries, realizando a consulta tanto no banco de dados quanto na API OMDb, caso necessário.</p>

<h4>Lógica Geral:</h4>
<ul>
  <li><strong>Validação de Parâmetros:</strong> Verifica se os parâmetros necessários (nome ou id) são fornecidos na requisição.</li>
  <li><strong>Consulta ao Banco de Dados:</strong> Tenta buscar os dados no banco de dados local.</li>
  <li><strong>Consulta à OMDb:</strong> Se o filme ou série não for encontrado no banco, realiza uma consulta à API OMDb e armazena os dados no banco de dados.</li>
</ul>

<h4>Endpoints Disponíveis</h4>

<h5><code>/buscar/nome</code></h5>
<ul>
  <li><strong>Endpoint:</strong> <code>/buscar/nome</code></li>
  <li><strong>Método:</strong> <code>GET</code></li>
  <li><strong>Parâmetro:</strong> <code>nome</code></li>
  <li><strong>Exemplo:</strong></li>
</ul>

<pre><code>GET http://localhost:5000/buscar/nome?nome=Oppenheimer</code></pre>

<p><strong>Funcionamento:</strong></p>
<ol>
  <li>Recebe o parâmetro <code>nome</code> da requisição.</li>
  <li>Tenta buscar no banco de dados por um título que contenha o nome fornecido.</li>
  <li>Caso não encontre, realiza uma requisição à API OMDb para buscar os dados do filme ou série.</li>
  <li>Se a busca for bem-sucedida, armazena os dados no banco de dados para futuras consultas.</li>
  <li>Retorna os dados do filme ou série em formato JSON.</li>
</ol>

<h5><code>/buscar/id</code></h5>
<ul>
  <li><strong>Endpoint:</strong> <code>/buscar/id</code></li>
  <li><strong>Método:</strong> <code>GET</code></li>
  <li><strong>Parâmetro:</strong> <code>id</code></li>
  <li><strong>Exemplo:</strong></li>
</ul>

<pre><code>GET http://localhost:5000/buscar/id?id=tt15398776</code></pre>

<p><strong>Funcionamento:</strong></p>
<ol>
  <li>Recebe o parâmetro <code>id</code> da requisição.</li>
  <li>Tenta buscar no banco de dados pelo <code>imdb_id</code>.</li>
  <li>Caso não encontre, faz uma requisição à API OMDb com o ID fornecido.</li>
  <li>Se a busca for bem-sucedida, armazena os dados no banco de dados.</li>
  <li>Retorna as informações em formato JSON.</li>
</ol>

<h3><code>db.py</code></h3>
<p>Contém funções responsáveis pela conexão com o banco de dados e pela inicialização da tabela <code>filmes_series</code> se ela não existir.</p>

<ul>
  <li><strong>Função <code>conexao()</code>:</strong> Estabelece uma conexão com o banco de dados utilizando as configurações definidas em <code>config.py</code>.</li>
  <li><strong>Função <code>init_db()</code>:</strong> Cria a tabela <code>filmes_series</code> no banco de dados, caso ela não exista: <code> CREATE TABLE IF NOT EXISTS</code></li>
</ul>

<pre><code>import psycopg
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def conexao():
    conn = psycopg.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    ) 
    return conn

def init_db():
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
        conn.commit()</code></pre>

<h3><code>config.py</code></h3>
<p>Este arquivo contém as variáveis de configuração do sistema, como as credenciais para o banco de dados e a chave da API OMDb. Essas variáveis são segregadas para garantir maior segurança e organização.</p>

<h3><code>omdb_service.py</code></h3>
<p>Contém funções responsáveis por fazer requisições GET para a API OMDb, tanto para buscar filmes e séries pelo nome quanto pelo ID do IMDb.</p>

<h4>Funções:</h4>
<ul>
  <li><strong><code>buscar_filme_nome(nome)</code></strong>: Faz uma requisição GET à API OMDb para buscar um filme ou série pelo nome.</li>
  <li><strong><code>buscar_filme_id(imdb_id)</code></strong>: Faz uma requisição GET à API OMDb para buscar um filme ou série pelo ID do IMDb.</li>
</ul>

<pre><code>import requests
from config import OMDB_API_KEY

def buscar_filme_nome(nome):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={nome}" 
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()
    return None

def buscar_filme_id(imdb_id):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&i={imdb_id}" 
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()
    return None
</code></pre>
