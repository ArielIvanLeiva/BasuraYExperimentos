from pydantic import BaseModel
from mytypes import Privacidad

class PartidaData(BaseModel):
    nombre: str
    tipo: Privacidad
    iniciada: bool

class PartidaId(PartidaData):
    id: int