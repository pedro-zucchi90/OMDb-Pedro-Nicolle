from flask import Flask, request, jsonify
from db import conexao, init_db
from omdb_service import buscar_filme_nome, buscar_filme_id
import json

app = Flask(__name__)
