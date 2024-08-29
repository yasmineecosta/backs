# mkdir hello - criar uma pasta/diretório
from fastapi import FastAPI
# para usar modelo de classes:
from pydantic import BaseModel

# criando uma aplicação:
app = FastAPI() # server:app - server é o nome do arquivo e app er aki

#decorator: é uma função que recebe uma função como argumento e retorna outra função     
@app.get("/")

# criando uma rota: referencia a primeira pagina, como se fosse um dicionario
async def root(): #async: vai ser acionado mas n necessariamente vai acontecer
    return {"message": "Hello World - yasmaino!"}


# http://127.0.0.1:8000
# botando tambem o /docs no final do link, ele vai mostrar a documentação da api com as rotas
# EMERGENCIAS: python -m uvicorn server:app --reload

# GET trás informações e POST enviar informações
# PUT atualiza uma informação e DELETE deleta uma informação

# EX: // path é o q ta entre () - endpoint, rota, ...
@app.get('/')
def home():
    return {"message": "FastAPI funfa"}


@app.get('/saudacao/{nome:}') #{} - parametro dado na url
def saudacao(nome: str):
    texto = f'Olá {nome}, seja bem-vindo ao FastAPI'
    return {"mensagem": texto}


@app.get('/quadrado/{numero}')
def quadrado(numero:int):
    result = numero * numero
    texto = f'O quadrado de {numero} é {result}'
    return {"mensagem": texto}

@app.get('/profile')
def profile():
    return {"nome": "Yasmine Martins"}


@app.post('/profile')
def signup():
    return {"mensagem": "Perfil criado com sucesso!"}


@app.put('/profile')
def att():
    return {"mensagem": "Perfil atualizado com sucesso!"}


@app.delete('/profile')
def remover():
    return {"mensagem": "Perfil deletado com sucesso!"}


@app.get('/dobro')
def dobro(valor: int):
    resultado = 2 * valor
    return {"resultado": f'O dobro de {valor} é {resultado}'}
# http://127.0.0.1:8000/dobro?valor=4
# coloca o nome da variável depois de ? e ai o valor dela depois da igualdade

@app.get('/area-retangulo')
def area_retangulo(largura: int, altura: int = 1):
    area = largura * altura
    return {'area': area}


# @app.post('/produtos')
# def produtos():
#     return {'mensagem':'Produto (Espetinho) cadastrado com sucesso!'}
# Parametros de rotas - resgatar um produto de id x, filtrar...
# @app.get('/hello/{nome}')
# def hello(nome):
#   return nome

# Parametros de query string - ajustar as respostas - configurar modelo, chave, organizar
# @app.get('/hello/{nome}')
# def hello(nome):
#   return 


#criação de classes:
class Produto(BaseModel):
    nome: str
    preco: float

    
@app.post('/produtos')
def produtos(produto: Produto):
    return {'mensagem': f'Produto ({produto.nome} - R$ {produto.preco}) cadastrado com sucesso!'}

# usando insomnia para testar, se cria uma nova pasta e pode-se fzr requisições de post, get, put, delete, etc
# no caso, as requisições são feitas para o endereço http://(endereço da api) e usa-se o json para passar os dados

