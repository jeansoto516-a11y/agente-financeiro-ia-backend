# importa funções do SQLALchemy 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# URL DE CONEXÃO DO POSTGRESQL

DATABASE_URL = "postgresql://postgres:Jean1245@localhost:5432/agente_financeiro"

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
