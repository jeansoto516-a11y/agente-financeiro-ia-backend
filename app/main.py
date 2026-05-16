# Importa o FastAPI
from fastapi import FastAPI

# Importa as rotas da API
from app.api.market_routes import router as market_router

# Importa engine e Base do banco
from app.database.connection import engine, Base

# Importa os models para o SQLAlchemy reconhecer
from app.database import models



# CRIAÇÃO DAS TABELAS NO BANCO
Base.metadata.create_all(bind=engine)


# INICIALIZAÇÃO DA API

app = FastAPI()

# REGISTRO DAS ROTAS

app.include_router(market_router)

# ROTA PRINCIPAL

@app.get("/")
def home():

    """
    Rota principal da API
    """

    return {
        "message": "Financial AI Agent Online"
    }