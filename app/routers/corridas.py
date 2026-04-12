from fastapi import APIRouter, HTTPException
from app.database import get_connection

router = APIRouter()

@router.get("/corridas")
def listar_corridas(temporada: int = None):
    conn = get_connection()
    cursor = conn.cursor()

    # Se tiver filtro por temporada
    if temporada is not None:
        cursor.execute("SELECT * FROM corridas WHERE temporada = ?", (temporada,))
    else:
        cursor.execute("SELECT * FROM corridas")

    corridas = cursor.fetchall()

    # Se não encontrou nada
    if not corridas:
        conn.close()
        raise HTTPException(status_code=404, detail="Nenhuma corrida encontrada")

    resultado = [dict(row) for row in corridas]

    conn.close()
    return resultado