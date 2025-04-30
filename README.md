<h1 style="text-align: center;">Projeto: API de Filmes e Séries</h1>

<p style="text-align: center;">Trabalho de Desenvolvimento Web — 3º ano (Turma 3F)</p>

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

<h2 style="text-align: center;">Endpoints disponíveis</h2>

<h3>/buscar/nome</h3>
<ul>
  <li><strong>Endpoint:</strong> <code>/buscar/nome</code></li>
  <li><strong>Método:</strong> <code>GET</code></li>
  <li><strong>Parâmetro:</strong> <code>nome</code></li>
  <li><strong>Exemplo:</strong>
    <pre><code>GET http://localhost:5000/buscar/nome?nome=Oppenheimer</code></pre>
  </li>
</ul>

<h3>/buscar/id</h3>
<ul>
  <li><strong>Endpoint:</strong> <code>/buscar/id</code></li>
  <li><strong>Método:</strong> <code>GET</code></li>
  <li><strong>Parâmetro:</strong> <code>id</code></li>
  <li><strong>Exemplo:</strong>
    <pre><code>GET http://localhost:5000/buscar/id?id=tt15398776</code></pre>
  </li>
</ul>

<hr>

<h2 style="text-align: center;">Explicação do sistema</h2>

<h3>1. app.py</h3>
<p>Define duas rotas principais para busca:</p>
<ul>
  <li><code>/buscar/nome</code></li>
  <li><code>/buscar/id</code></li>
</ul>
<p>Lógica geral:</p>
<ul>
  <li>Valida parâmetros</li>
  <li>Consulta o banco</li>
  <li>Se não achar, consulta OMDb e armazena</li>
</ul>

<h3>2. db.py</h3>
<ul>
  <li>Funções para conectar ao banco e criar a tabela</li>
</ul>

<h3>3. config.py</h3>
<ul>
  <li>Define variáveis de configuração (segregadas para segurança e organização)</li>
</ul>

<h3>4. omdb_service.py</h3>
<ul>
  <li>Funções para fazer requisições GET para a OMDb por nome ou ID</li>
</ul>

<hr>

<h2 style="text-align: center;">Fluxo de funcionamento</h2>

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
