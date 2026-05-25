# IMPORTA BANCO E MODEL 
from app.database.connection import SessionLocal
from app.database.models import Analysis

# HISTÓRICO DE ANÁLISES
def get_analysis_history():
    db = SessionLocal()
    analyses = db.query(Analysis).all()
    history = []

    for item in analyses:
        history.append({
            "id": item.id,
            "ativo": item.ativo,
            "preco_atual": item.preco_atual,
            "tendencia": item.tendencia,
            "forca": item.forca,
            "mm9": item.mm9,
            "mm21": item.mm21,
            "rsi": item.rsi,
            "sinal": item.sinal,
            "recomendacao": item.recomendacao
        })

    return history 