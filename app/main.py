from fastapi import FastAPI
from app.api.market_routes import router as market_router

app = FastAPI()

app.include_router(market_router)

@app.get("/")
def home():
    return {"message": "Financial AI Agent Online"}