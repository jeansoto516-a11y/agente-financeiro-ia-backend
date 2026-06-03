# IMPORTA SERVIÇOS
from app.services.analysis_service import analyze_asset

def get_market_ranking():

    # Lista de ativos monitorados
    ativos = [
        "PETR4.SA",
        "VALE3.SA",
        "ITUB4.SA",
        "BBAS3.SA",
        "AAPL",
        "TSLA",
        "NVDA",
        "MSFT",
        "BTC-USD",
        "ETH-USD"
    ]

    ranking = []

    # Analisa cada ativo
    for symbol in ativos:

        try:

            analysis = analyze_asset(symbol)

            # Ignora erros
            if "error" in analysis:
                continue

            # Score inicial
            score = 0

            # Tendência
            if analysis["tendencia"] == "ALTA":
                score += 40

            # Força
            if analysis["forca"] == "FORTE":
                score += 30

            # RSI saudável
            if 45 <= analysis["rsi"] <= 65:
                score += 20

            # Sinal de compra
            if analysis["sinal"] == "COMPRA":
                score += 10

            # Adiciona score ao resultado
            analysis["score"] = score

            ranking.append(analysis)

        except Exception:
            continue

    # Ordena do maior para o menor score
    ranking = sorted(
        ranking,
        key=lambda x: x["score"],
        reverse=True
    )

    return ranking