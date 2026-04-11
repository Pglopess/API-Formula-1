from fastapi import APIRouter, HTTPException
from app.database import get_connection
from app.models import Piloto

router = APIRouter()

@router.get("/pilotos")
def listar_pilotos(nacionalidade: str = None):
    conn = get_connection()
    cursor = conn.cursor()

    if nacionalidade:
        cursor.execute("SELECT * FROM pilotos WHERE nacionalidade = ?", (nacionalidade,))
    else:
        cursor.execute("SELECT * FROM pilotos")

    pilotos = [dict(row) for row in cursor.fetchall()]
    conn.close()

    if not pilotos:
        raise HTTPException(status_code=404, detail="Nenhum piloto encontrado")

    return pilotos

@router.get("/pilotos/{piloto_id}")
def buscar_piloto(piloto_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pilotos WHERE id = ?", (piloto_id,))
    piloto = cursor.fetchone()
    conn.close()

    if piloto is None:
        raise HTTPException(status_code=404, detail="Piloto não encontrado")

    return dict(piloto)

@router.post("/pilotos", status_code=201)
def criar_piloto(piloto: Piloto):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pilotos (nome, sobrenome, nacionalidade, nascimento)
        VALUES (?, ?, ?, ?)
    """, (piloto.nome, piloto.sobrenome, piloto.nacionalidade, piloto.nascimento))

    conn.commit()
    piloto_id = cursor.lastrowid
    conn.close()

    return {"mensagem": "Piloto criado com sucesso", "id": piloto_id, "piloto": piloto}