import requests
from config import OMDB_API_KEY

#buscar um filme ou série pelo nome
def buscar_filme_nome(nome):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={nome}" 
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()
    return None 

#buscar um filme ou série pelo id
def buscar_filme_id(imdb_id):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&i={imdb_id}" 
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()
    return None 
