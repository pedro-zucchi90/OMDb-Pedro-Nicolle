Este projeto é um trabalho de Desenvolvimento Web do terceiro ano (turma 3F). Foi feita uma API em Flask que permite **buscar filmes e séries** pelo nome ou pelo ID do IMDb.  
Os dados são consultados primeiro em um **banco de dados PostgreSQL** local. Se não forem encontrados, a API **consulta o OMDB** (Open Movie Database) e **armazena automaticamente** os dados para futuras buscas.

---

## Tecnologias utilizadas

- Python 3
- Flask
- PostgreSQL
- psycopg
- requests
- OMDB API

---

## Estrutura do projeto

```
|-- app.py               # Código principal do Flask
|-- db.py                # Conexão e inicialização do banco de dados
|-- omdb_service.py      # Comunicação com a API OMDB
|-- config.py            # Configurações (chave da API OMDB, informações do banco)
|-- requirements.txt     # Dependências do projeto
|-- README.md            # Documentação do projeto

```

--- 

## Configuração do ambiente
1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie e ative o ambiente virtual (.venv)**

   ```bash
   python -m venv .venv
   ```

   - **No Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **No Linux/Mac**:
     ```bash
     source .venv/bin/activate
     ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o arquivo `config.py`**

   Crie um arquivo `config.py` na raiz do projeto com o seguinte conteúdo:

   ```python
   # config.py

   DB_NAME = 'seu_banco'
   DB_USER = 'seu_usuario'
   DB_PASSWORD = 'sua_senha'
   DB_HOST = 'localhost'
   DB_PORT = '5432'

   OMDB_API_KEY = 'sua_chave_omdb'
   ```

   > Você pode obter sua chave da OMDB em [http://www.omdbapi.com/apikey.aspx](http://www.omdbapi.com/apikey.aspx).

5. **Configure o banco de dados PostgreSQL**

   Certifique-se de ter o PostgreSQL rodando localmente.  
   O projeto automaticamente cria a tabela `filmes_series` se ela não existir ao iniciar.

---

## Executando a aplicação

Com todas as configurações feitas, e no terminal da pasta `cache-filmes-series`:

```bash
python app.py
```

A aplicação ficará disponível em:

```
http://localhost:5000
```

---

## Endpoints disponíveis:

### Buscar filme ou série pelo **nome**

- **Endpoint**: `/buscar/nome`
- **Método**: `GET`
- **Parâmetro**: `nome`
- **Exemplo**:
  ```
  GET http://localhost:5000/buscar/nome?nome=Oppenheimer
  ```

---

### Buscar filme ou série pelo **ID do IMDb**

- **Endpoint**: `/buscar/id`
- **Método**: `GET`
- **Parâmetro**: `id`
- **Exemplo**:
  ```
  GET http://localhost:5000/buscar/id?id=tt15398776
  ```

---

## EXPLICAÇÃO DO SISTEMA

### 1. `app.py`

Esse arquivo é o que juntoa tudo na aplicação. Ele define duas rotas:
- `/buscar/nome`: que busca por nome do filme ou série.
- `/buscar/id`: que busca por ID do IMDb.

Ambas seguem esta **lógica geral**:
- Validam o parâmetro fornecido na URL.
- Buscam no banco de dados usando SQL.
- Se encontrarem, retornam os dados armazenados.
- Se **não** encontrarem, usam a OMDb API.
- Salvam a resposta no banco de dados para futuras requisições.
- Retornam os dados como JSON.

A função `init_db()` é chamada ao iniciar o app: ela cria a tabela no banco **se ainda não existir uma com o mesmo nome**.

---

### 2. `db.py`

Esse arquivo centraliza duas funções:
- `conexao()`: retorna uma instância de conexão PostgreSQL, usando as configurações do `config.py`.
- `init_db()`: cria a tabela `filmes_series` com colunas específicas como `imdb_id`, `titulo`, `ano`, `tipo`, `dados` (JSON), etc. Usa `CREATE TABLE IF NOT EXISTS`, ou seja, **não cria duplicatas**.

A vantagem é que a estrutura é definida apenas uma vez e reaproveitada pelo app.

---

### 3. `config.py`

Contém:
- Dados da conexão com o banco de dados (nome, usuário, senha, host, porta).
- A chave da API do OMDb.

Esse arquivo isola informações sensíveis e facilita a alteração do ambiente sem tocar na lógica do app.

---

### 4. `omdb_service.py`

Esse arquivo oferece duas funções:
- `buscar_filme_nome(nome)`: consulta a API OMDb passando o **título**.
- `buscar_filme_id(imdb_id)`: consulta a API OMDb passando o **ID do IMDb**.

Ambas funções:
- Constroem a URL com base nos parâmetros e na chave da API.
- Enviam uma requisição HTTP.
- Se a resposta for 200 (sucesso), retornam os dados convertidos de JSON.
- Caso contrário, retornam `None`.

---

## DETALHAMENTO DAS REQUISIÇÕES

### `/buscar/nome`
1. Verifica se o parâmetro `nome` está presente na URL.
2. Usa o `ILIKE` (case-insensitive) para procurar no banco o campo `titulo`.
3. Se encontrar, retorna o conteúdo da coluna `dados` (JSONB).
4. Se não encontrar:
   - Chama `buscar_filme_nome()` para consultar a OMDb API.
   - Se encontrar:
     - Insere os dados completos na tabela com `INSERT ... ON CONFLICT DO NOTHING` (evita duplicatas pelo `imdb_id`).
     - Retorna os dados ao usuário.
   - Se a OMDb não encontrar, retorna erro 404.

### `/buscar/id`
1. Verifica se o parâmetro `id` está presente na URL.
2. Procura no banco o `imdb_id` correspondente.
3. Se encontrar, retorna os dados.
4. Se não encontrar:
   - Chama `buscar_filme_id()` na OMDb API.
   - Se encontrar:
     - Insere os dados na tabela.
     - Retorna ao usuário.
   - Se a OMDb não encontrar, retorna erro 404.

