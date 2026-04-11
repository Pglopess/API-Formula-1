from fastapi import FastAPI
from app.routers import pilotos, analises

app = FastAPI(
    title="API Formula 1",
    description="API REST com dados reais de F1 (1950–2024)",
    version="1.0.0"
)

app.include_router(pilotos.router)
app.include_router(analises.router)

@app.get("/")
def root():
    return {"mensagem": "API Formula 1 funcionando!"}