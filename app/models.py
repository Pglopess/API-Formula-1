from pydantic import BaseModel

class Piloto(BaseModel):
    nome: str
    sobrenome: str
    nacionalidade: str
    nascimento: str