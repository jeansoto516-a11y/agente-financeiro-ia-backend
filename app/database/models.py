# IMPORTA BASE DO SQLALCHEMY
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from app.database.connection import Base

# TABELA DE ANÁLISES
class Analysis(Base):

    # Nome da tabela
    __tablename__ = "analyses"

    # ID único
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # Nome do ativo
    ativo = Column(String)

    # Preço atual
    preco_atual = Column(Float)

    # Tendência
    tendencia = Column(String)

    # Força da tendência
    forca = Column(String)

    # Média móvel curta
    mm9 = Column(Float)

    # Média móvel longa
    mm21 = Column(Float)

    # RSI
    rsi = Column(Float)

    # Sinal operacional
    sinal = Column(String)

    # Recomendação final
    recomendacao = Column(String)