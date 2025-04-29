import requests
from config import OMDB_API_KEY

#buscar um filme ou série pelo nome
def buscar_filme_nome(nome):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={nome}" 
    resposta = requests.get(url)
    return resposta.json()

def buscar_filme_id(imdb_id):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&i={imdb_id}" 
    resposta = requests.get(url)
    return resposta.json()
  
