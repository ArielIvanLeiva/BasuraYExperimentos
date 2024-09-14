from pydantic import BaseModel
from utils import Privacidad

class PartidaData(BaseModel):
    nombre: str
    tipo: Privacidad
    iniciada: bool

class PartidaId(PartidaData):
    id: int