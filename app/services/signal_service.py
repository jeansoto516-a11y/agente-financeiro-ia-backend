# Importa a função de análise
from app.services.analysis_service import analyze_asset

# FUNÇÃO QUE GERA SINAIS DO MERCADO
def get_market_signals():

    # LISTA DE ATIVOS ANALISADOS

    ativos = [
        "PETR4.SA",
        "VALE3.SA",
        "ITUB4.SA",
        "BBAS3.SA",
        "AAPL",
        "TSLA",
        "NVDA",
        "BTC-USD",
        "ETH-USD"
    ]

    # Lista final
    sinais = []

    # ANALISA TODOS OS ATIVOS
    for symbol in ativos:

        try:

            # Executa análise do ativo
            analise = analyze_asset(symbol)

            # Ignora erros
            if "error" in analise:
                continue

            # FILTRO DE SINAIS
            # Adiciona somente sinais relevantes
            if analise["sinal"] != "NEUTRO":

                sinais.append({
                    "ativo": analise["ativo"],
                    "preco": analise["preco_atual"],
                    "tendencia": analise["tendencia"],
                    "forca": analise["forca"],
                    "rsi": analise["rsi"],
                    "sinal": analise["sinal"],
                    "recomendacao": analise["recomendacao"]
                })

        except:
            continue

    # ORDENA PELOS MELHORES SINAIS
    sinais = sorted(
        sinais,
        key=lambda x: (
            x["forca"] == "FORTE",
            x["sinal"] == "COMPRA"
        ),
        reverse=True
    )

    
    # RETORNO FINAL
    return {
        "total_sinais": len(sinais),
        "sinais": sinais
    }