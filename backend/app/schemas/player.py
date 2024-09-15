from pydantic import BaseModel

class PlayerData(BaseModel):  
    partida_id: int
    nombre: str

class PlayerId(PlayerData):
    id: int