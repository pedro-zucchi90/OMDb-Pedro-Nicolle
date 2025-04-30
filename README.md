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
