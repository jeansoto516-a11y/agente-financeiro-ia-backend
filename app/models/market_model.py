from pydantic import BaseModel


class MarketData(BaseModel):
    data: str
    abertura: float
    maxima: float
    minima: float
    fechamento: float
    volume: float


class MarketResponse(BaseModel):
    ativo: str
    inicio: str
    fim: str
    dados: list[MarketData]