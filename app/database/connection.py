# importa funções do SQLALchemy 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# URL DE CONEXÃO DO POSTGRESQL - Vem do arquivo .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Validação: garante que a variável está configurada
if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL não foi configurada no arquivo .env")

# ENGENE DE CONEXÃO

engine = create_engine(

    DATABASE_URL,
    pool_pre_ping=True 
)

# SESSÃO DO BANCO 
SessionLocal = sessionmaker(

    autocommit=False,
    autoflush=False,
    bind=engine
)

#BASE DOS MODELOS ORM
Base = declarative_base()
