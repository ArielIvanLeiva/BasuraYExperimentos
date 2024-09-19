from pydantic import BaseModel
from typing import Optional

class PartidaData(BaseModel):
    nombre_partida: str
    min_jugadores: Optional[int] = None
    max_jugadores: Optional[int] = None

class PartidaCreada(PartidaData):
    iniciada: bool
    id: int