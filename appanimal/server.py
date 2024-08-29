from fastapi import FastAPI
from typing import List
from typing import Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

class Animal(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str
    cor: str

banco: List[Animal] = []

@app.get("/animais")
def listar_animais():
    return banco


# pedir dados do backend
@app.get("/animais/{animal_id}")
def obter_animal(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
        
    return {'erro': 'Animal não localizado'}

@app.delete("/animais/{animal_id}")
def remover_animal(animal_id: str):
    posicao = -1
    # buscar a posição do animal no banco
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index
            break
    
    if posicao != -1:
        # remover o animal
        banco.pop(posicao)
        return {'mensagem': 'Animal removido com sucesso'}
    else:
        return {'erro': 'Animal não localizado'}

#enviar dados do backend
@app.post("/animais")
def criar_animal(animal: Animal):
    if animal.id is None or animal.id == '':
        animal.id = str(uuid4())
    banco.append(animal)
    return None
 
