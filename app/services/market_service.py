import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator

# ANÁLISE INDIVIDUAL
def get_stock_data(symbol: str):

    # Cria o objeto do ativo
    stock = yf.Ticker(symbol)

    # Busca os últimos 3 meses
    data = stock.history(period="3mo")

    # Verifica se encontrou dados
    if data.empty:
        return {"error": "Ativo não encontrado"}

    # INDICADOR RSI

    # Calcula o RSI de 14 períodos
    rsi_indicator = RSIIndicator(close=data["Close"], window=14)

    # Cria coluna RSI
    data["RSI"] = rsi_indicator.rsi()

    # Último RSI
    last_rsi = data["RSI"].iloc[-1]

    # MÉDIAS MÓVEIS

    # Média móvel curta
    data["MA9"] = data["Close"].rolling(window=9).mean()

    # Média móvel longa
    data["MA21"] = data["Close"].rolling(window=21).mean()

    # Últimos valores
    ma9 = data["MA9"].iloc[-1]
    ma21 = data["MA21"].iloc[-1]

    # TENDÊNCIA

    if ma9 > ma21:
        trend = "ALTA"
    else:
        trend = "BAIXA"

    # SINAL RSI

    if last_rsi > 70:
        signal_rsi = "SOBRECOMPRA"

    elif last_rsi < 30:
        signal_rsi = "SOBREVENDA"

    else:
        signal_rsi = "NEUTRO"

    # RETORNO FINAL

    return {
        "ativo": symbol,
        "preco": round(float(data["Close"].iloc[-1]), 2),
        "rsi": round(float(last_rsi), 2),
        "sinal_rsi": signal_rsi,
        "media_9": round(float(ma9), 2),
        "media_21": round(float(ma21), 2),
        "tendencia": trend
    }


# TOP ATIVOS
def get_top_assets():

    # Lista de ativos analisados
    ativos = [
        "PETR4.SA",
        "VALE3.SA",
        "ITUB4.SA",
        "BBAS3.SA",
        "AAPL",
        "TSLA",
        "NVDA",
        "BTC-USD"
    ]

    resultados = []

    # Percorre todos os ativos
    for symbol in ativos:

        try:

            stock = yf.Ticker(symbol)

            data = stock.history(period="3mo")

            # Se não houver dados, ignora
            if data.empty:
                continue

            # RSI

            rsi_indicator = RSIIndicator(
                close=data["Close"],
                window=14
            )

            data["RSI"] = rsi_indicator.rsi()

            rsi = data["RSI"].iloc[-1]

            # MÉDIAS

            data["MA9"] = data["Close"].rolling(window=9).mean()

            data["MA21"] = data["Close"].rolling(window=21).mean()

            ma9 = data["MA9"].iloc[-1]
            ma21 = data["MA21"].iloc[-1]

            # TENDÊNCIA
            trend = "ALTA" if ma9 > ma21 else "BAIXA"

            # SCORE INTELIGENTE

            score = 0

            # Tendência positiva
            if trend == "ALTA":
                score += 50

            # RSI saudável
            if 40 <= rsi <= 65:
                score += 30

            # Evita sobrecompra
            if rsi < 70:
                score += 20

            # Adiciona resultado
            resultados.append({
                "ativo": symbol,
                "preco": round(float(data["Close"].iloc[-1]), 2),
                "rsi": round(float(rsi), 2),
                "tendencia": trend,
                "score": score
            })

        except:
            continue

    # Ordena pelo score
    resultados = sorted(
        resultados,
        key=lambda x: x["score"],
        reverse=True
    )

    return resultados

# HISTÓRICO DE PREÇOS
def get_historical_data(symbol: str, start: str, end: str):

    # Cria o objeto do ativo
    stock = yf.Ticker(symbol)

    # Busca dados históricos
    data = stock.history(start=start, end=end)

    # Verifica se encontrou dados
    if data.empty:
        return {"error": "Dados não encontrados"}


    # INDICADORES TÉCNICOS

    # RSI
    rsi_indicator = RSIIndicator(
        close=data["Close"],
        window=14
    )

    data["RSI"] = rsi_indicator.rsi()

    # Média móvel curta
    data["MA9"] = data["Close"].rolling(window=9).mean()

    # Média móvel longa
    data["MA21"] = data["Close"].rolling(window=21).mean()

    # Lista final
    historical = []

    # Percorre cada linha do dataframe
    for index, row in data.iterrows():

        historical.append({

            # Data formatada
            "data": index.strftime("%Y-%m-%d"),

            # Preços
            "abertura": round(float(row["Open"]), 2),
            "maxima": round(float(row["High"]), 2),
            "minima": round(float(row["Low"]), 2),
            "fechamento": round(float(row["Close"]), 2),

            # Volume negociado
            "volume": int(row["Volume"]),

            # Indicadores técnicos
            "rsi": round(float(row["RSI"]), 2)
            if pd.notna(row["RSI"]) else None,

            "mm9": round(float(row["MA9"]), 2)
            if pd.notna(row["MA9"]) else None,

            "mm21": round(float(row["MA21"]), 2)
            if pd.notna(row["MA21"]) else None
        })

    # Retorno final
    return {
        "ativo": symbol,
        "inicio": start,
        "fim": end,
        "dados": historical
    }


