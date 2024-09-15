from sqlalchemy.orm import Session

from models.partidas import Partida
from schemas.partidas import PartidaData
from models.player import Player
from schemas.player import PlayerData

def get_partidas(db: Session):
    return db.query(Partida).all()

def get_partida_by_id(db: Session, id: int):
    return db.query(Partida).filter(Partida.id == id).first()

def get_partidas_by_name(db: Session, nombre: str):
    return db.query(Partida).filter(Partida.nombre == nombre)

def create_partida(db: Session, partida: PartidaData):
    new_partida = Partida(nombre=partida.nombre, tipo=partida.tipo, iniciada=False)
    db.add(new_partida)
    db.commit()
    db.flush()
    return new_partida

def delete_partida(db: Session, id: int):
    db.query(Partida).filter(Partida.id == id).delete()
    db.commit()

def create_player(db: Session, player: PlayerData):
    new_player = Player(nombre=player.nombre, partida_id=player.partida_id)
    db.add(new_player)
    db.commit()
    db.flush()
    return new_player
