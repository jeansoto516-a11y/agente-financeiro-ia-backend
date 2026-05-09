from fastapi import APIRouter
from app.services.market_service import (
    get_stock_data,
    get_top_assets,
    get_historical_data
)

router = APIRouter()

# =====================================
# BUSCAR ATIVO INDIVIDUAL
# =====================================

@router.get("/market/{symbol}")
def market(symbol: str):
    return get_stock_data(symbol)

# =====================================
# TABELA DE MELHORES ATIVOS
# =====================================

@router.get("/top-assets")
def top_assets():
    return get_top_assets()

# =====================================
# HISTÓRICO DE PREÇOS
# =====================================

from app.models.market_model import MarketResponse
@router.get("/historico", response_model=MarketResponse)
def historical(
    symbol: str,
    start: str,
    end: str
):
    return get_historical_data(symbol, start, end)