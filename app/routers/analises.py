import pandas as pd
from fastapi import APIRouter
from app.database import get_connection

router = APIRouter()

@router.get("/analises/artilheiros")
def artilheiros(temporada: int = None):
    conn = get_connection()

    if temporada:
        query = """
            SELECT p.nome, p.sobrenome, p.nacionalidade, SUM(r.pontos) as total_pontos
            FROM resultados r
            JOIN pilotos p ON r.piloto_id = p.id
            JOIN corridas c ON r.corrida_id = c.id
            WHERE c.temporada = ?
            GROUP BY p.id
            ORDER BY total_pontos DESC
            LIMIT 10
        """
        df = pd.read_sql_query(query, conn, params=(temporada,))
    else:
        query = """
            SELECT p.nome, p.sobrenome, p.nacionalidade, SUM(r.pontos) as total_pontos
            FROM resultados r
            JOIN pilotos p ON r.piloto_id = p.id
            GROUP BY p.id
            ORDER BY total_pontos DESC
            LIMIT 10
        """
        df = pd.read_sql_query(query, conn)

    conn.close()

    df["total_pontos"] = df["total_pontos"].astype(float)

    return df.to_dict(orient="records")

@router.get("/analises/equipes")
def pontuacao_equipes(temporada: int = None):
    conn = get_connection()

    if temporada:
        query = """
            SELECT r.posicao, SUM(r.pontos) as total_pontos, c.temporada
            FROM resultados r
            JOIN corridas c ON r.corrida_id = c.id
            WHERE c.temporada = ?
            GROUP BY c.temporada
        """
        df = pd.read_sql_query(query, conn, params=(temporada,))
    else:
        query = """
            SELECT c.temporada, SUM(r.pontos) as total_pontos
            FROM resultados r
            JOIN corridas c ON r.corrida_id = c.id
            GROUP BY c.temporada
            ORDER BY c.temporada DESC
        """
        df = pd.read_sql_query(query, conn)

    conn.close()

    df["total_pontos"] = df["total_pontos"].astype(float)

    return df.to_dict(orient="records")