import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator

# =========================
# ANÁLISE INDIVIDUAL
# =========================

def get_stock_data(symbol: str):

    stock = yf.Ticker(symbol)

    data = stock.history(period="3mo")

    if data.empty:
        return {"error": "Ativo não encontrado"}

    last_price = data["Close"].iloc[-1]

    # RSI

    rsi_indicator = RSIIndicator(close=data["Close"], window=14)
    data["RSI"] = rsi_indicator.rsi()

    last_rsi = data["RSI"].iloc[-1]

    if last_rsi > 70:
        signal_rsi = "SOBRECOMPRA"
    elif last_rsi < 30:
        signal_rsi = "SOBREVENDA"
    else:
        signal_rsi = "NEUTRO"

    # MÉDIAS

    data["MA9"] = data["Close"].rolling(window=9).mean()
    data["MA21"] = data["Close"].rolling(window=21).mean()

    ma9 = data["MA9"].iloc[-1]
    ma21 = data["MA21"].iloc[-1]

    # TENDÊNCIA

    if ma9 > ma21:
        trend = "ALTA"
    else:
        trend = "BAIXA"

    return {
        "ativo": symbol,
        "preco": round(float(last_price), 2),
        "rsi": round(float(last_rsi), 2),
        "sinal_rsi": signal_rsi,
        "media_9": round(float(ma9), 2),
        "media_21": round(float(ma21), 2),
        "tendencia": trend
    }

# =========================
# TOP ATIVOS
# =========================

def get_top_assets():

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

    for symbol in ativos:

        try:

            stock = yf.Ticker(symbol)

            data = stock.history(period="3mo")

            if data.empty:
                continue

            # RSI

            rsi_indicator = RSIIndicator(close=data["Close"], window=14)
            data["RSI"] = rsi_indicator.rsi()

            rsi = data["RSI"].iloc[-1]

            # MÉDIAS

            data["MA9"] = data["Close"].rolling(window=9).mean()
            data["MA21"] = data["Close"].rolling(window=21).mean()

            ma9 = data["MA9"].iloc[-1]
            ma21 = data["MA21"].iloc[-1]

            # TENDÊNCIA

            trend = "ALTA" if ma9 > ma21 else "BAIXA"

            # SCORE

            score = 0

            if trend == "ALTA":
                score += 50

            if 40 <= rsi <= 65:
                score += 30

            if rsi < 70:
                score += 20

            resultados.append({
                "ativo": symbol,
                "preco": round(float(data['Close'].iloc[-1]), 2),
                "rsi": round(float(rsi), 2),
                "tendencia": trend,
                "score": score
            })

        except:
            continue

    resultados = sorted(resultados, key=lambda x: x["score"], reverse=True)

    return resultados       

# =========================
# HISTÓRICO DE PREÇOS
# =========================

def get_historical_data(symbol: str, start: str, end: str):

    stock = yf.Ticker(symbol)

    data = stock.history(start=start, end=end)

    if data.empty:
        return {"error": "Dados não encontrados"}

    historical = []

    for index, row in data.iterrows():

        historical.append({
            "data": index.strftime("%Y-%m-%d"),
            "abertura": round(float(row["Open"]), 2),
            "maxima": round(float(row["High"]), 2),
            "minima": round(float(row["Low"]), 2),
            "fechamento": round(float(row["Close"]), 2),
            "volume": int(row["Volume"])
        })

    return {
        "ativo": symbol,
        "inicio": start,
        "fim": end,
        "dados": historical
    }