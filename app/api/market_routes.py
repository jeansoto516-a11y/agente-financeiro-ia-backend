from fastapi import APIRouter

# Importa os serviços do sistema
from app.services.market_service import (
    get_stock_data,
    get_top_assets,
    get_historical_data
)

# Importa serviço de análise técnica
from app.services.analysis_service import analyze_asset

# Importa serviço de sinais do mercado
from app.services.signal_service import get_market_signals

# Importa model de resposta
from app.models.market_model import MarketResponse

# Cria o router da API
router = APIRouter()

# BUSCAR ATIVO INDIVIDUAL

@router.get("/market/{symbol}")
def market(symbol: str):

    """
    Retorna os dados de um ativo específico
    """

    return get_stock_data(symbol)

# TABELA DE MELHORES ATIVOS

@router.get("/top-assets")
def top_assets():

    """
    Retorna ranking dos melhores ativos
    """

    return get_top_assets()

# HISTÓRICO DE PREÇOS

@router.get("/historico", response_model=MarketResponse)
def historical(
    symbol: str,
    start: str,
    end: str
):

    """
    Retorna histórico de preços do ativo
    """

    return get_historical_data(symbol, start, end)


# ANÁLISE TÉCNICA

@router.get("/analysis/{symbol}")
def analyze(symbol: str):

    """
    Executa análise técnica do ativo
    """

    return analyze_asset(symbol)


# SINAIS DO MERCADO

@router.get("/signals")
def market_signals():

    """
    Retorna os principais sinais do mercado
    """

    return get_market_signals()