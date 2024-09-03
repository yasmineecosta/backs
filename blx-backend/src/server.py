# Rotas e controller
from fastapi import FastAPI, Depends, status, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
# from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.routers import rotas_produtos, rotas_auth, rotas_pedidos
from src.jobs.write_notification import write_notification

# criar_bd()

app = FastAPI()

origins = ["http://127.0.0.1:8000"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, 
                   allow_methods=["*"], allow_headers=["*"])

# # ROTAS DE PRODUTOS
app.include_router(rotas_produtos.router)

# ROTAS DE SEGURANÇA DE USUARIOS: Autenticação e Autorização
app.include_router(rotas_auth.router, prefix="/auth")

# # ROTAS DE PEDIDOS
app.include_router(rotas_pedidos.router)

# Rota send email
@app.post("/send_email/{email}", status_code=status.HTTP_201_CREATED)
def send_email(email:str, background: BackgroundTasks):
    background.add_task(write_notification, email, "Olá, tudo bem?")
    return {"email": "Email enviado com sucesso!"}

# Middlewares
@app.middleware("http")
async def processar_tempo_requisicao(request: Request, next):
    print("Interceptou Chegada...")
    response = await next(request)
    
    print("Interceptou Saída...")
    return response