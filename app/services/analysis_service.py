# Importa a função que busca os dados históricos
from app.services.market_service import get_historical_data

# FUNÇÃO DE ANÁLISE DO ATIVO

def analyze_asset(symbol: str):

    # BUSCA DADOS HISTÓRICOS

    response = get_historical_data(
        symbol,
        "2025-01-01",
        "2026-01-01"
    )

    # Verifica se houve erro
    if "error" in response:
        return response

    # Pega somente os dados
    data = response["dados"]

    # =====================================
    # REMOVE VALORES INVÁLIDOS
    # =====================================

    # Remove registros onde indicadores ainda são None
    data = [
        item for item in data
        if item["mm9"] is not None
        and item["mm21"] is not None
        and item["rsi"] is not None
    ]

    # Verifica novamente
    if not data:
        return {
            "error": "Dados insuficientes para análise"
        }

    # =====================================
    # ÚLTIMOS INDICADORES
    # =====================================

    # Último fechamento
    ultimo_fechamento = data[-1]["fechamento"]

    # Última média móvel curta
    ultima_mm9 = data[-1]["mm9"]

    # Última média móvel longa
    ultima_mm21 = data[-1]["mm21"]

    # Último RSI
    ultimo_rsi = data[-1]["rsi"]

    # =====================================
    # SINAL OPERACIONAL
    # =====================================

    sinal = "NEUTRO"

    # Tendência de alta
    if ultima_mm9 > ultima_mm21:

        # Mercado sobrecomprado
        if ultimo_rsi > 70:
            sinal = "VENDA"

        # Mercado saudável
        elif 40 <= ultimo_rsi <= 70:
            sinal = "COMPRA"

    # Tendência de baixa
    elif ultima_mm9 < ultima_mm21:

        # Mercado sobrevendido
        if ultimo_rsi < 30:
            sinal = "COMPRA"

        # Continuação de baixa
        else:
            sinal = "VENDA"

    # =====================================
    # FORÇA DA TENDÊNCIA
    # =====================================

    forca = "NEUTRA"

    # Tendência forte
    if ultima_mm9 > ultima_mm21 and ultimo_rsi > 55:
        forca = "FORTE"

    # Tendência fraca
    elif ultimo_rsi < 45:
        forca = "FRACA"

    # =====================================
    # DIREÇÃO DA TENDÊNCIA
    # =====================================

    tendencia = "ALTA"

    if ultima_mm9 < ultima_mm21:
        tendencia = "BAIXA"

    # =====================================
    # RECOMENDAÇÃO INTELIGENTE
    # =====================================

    recomendacao = ""

    if sinal == "COMPRA":

        recomendacao = (
            "Ativo em tendência de alta com momentum positivo."
        )

    elif sinal == "VENDA":

        recomendacao = (
            "Ativo demonstra fraqueza técnica e possível continuação de queda."
        )

    else:

        recomendacao = (
            "Mercado lateralizado sem confirmação clara."
        )

    # =====================================
    # RETORNO FINAL
    # =====================================

    return {
        "ativo": symbol,

        "preco_atual": round(
            float(ultimo_fechamento), 2
        ),

        "tendencia": tendencia,

        "forca": forca,

        "mm9": round(
            float(ultima_mm9), 2
        ),

        "mm21": round(
            float(ultima_mm21), 2
        ),

        "rsi": round(
            float(ultimo_rsi), 2
        ),

        "sinal": sinal,

        "recomendacao": recomendacao
    }