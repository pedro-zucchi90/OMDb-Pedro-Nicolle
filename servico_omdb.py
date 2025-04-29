import requests
from config import OMDB_API_KEY

#buscar um filme ou série pelo nome
def buscar_filme_nome(nome):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={nome}" #constrói a URL para a requisição com a api, passando a api key e o NOME do filme ou série
    resposta = requests.get(url)#envia uma requisição GET para a URL construída

    if resposta.status_code == 200:#verifica se a resposta foi bem-sucedida (odigo 200)
        return resposta.json()#retorna os dados do filme ou série em formato JSON
    return None #se a resposta não foi bem-sucedida, retorna NONE

#buscar um filme ou série pelo id
def buscar_filme_id(imdb_id):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&i={imdb_id}" #constrói a url para a requisição com a API, passando a api key e o ID do filme ou série
    resposta = requests.get(url)#envia uma requisição GET para a url construída

    if resposta.status_code == 200:# verifica se a resposta foi bem-sucedida (codigo 200)
        return resposta.json()#retorna os dados do filme ou série em formato JSON
    return None #se a resposta não foi bem-sucedida, retorna NONE
