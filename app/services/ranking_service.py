from app.services.analysis_service import analyze_asset

def get_market_ranking():

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

    for symbol in ativos:

        try:

            analysis = analyze_asset(symbol)

            if "error" in analysis:
                continue

            score = 0

            if analysis["tendencia"] == "ALTA":
                score += 40

            if analysis["forca"] == "FORTE":
                score += 30

            if 45 <= analysis["rsi"] <= 65:
                score += 20

            if analysis["sinal"] == "COMPRA":
                score += 10

            analysis["score"] = score

            ranking.append(analysis)

        except Exception:
            continue

    ranking = sorted(
        ranking,
        key=lambda x: x["score"],
        reverse=True
    )

    return ranking