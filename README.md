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
