from fastapi import (
    APIRouter, 
    HTTPException, 
    Depends, 
    WebSocket,
    WebSocketDisconnect,
    WebSocketException,
    status
)

from sqlalchemy.orm import Session
from http import HTTPStatus

import crud.partidas as crud
from models.partidas import Base
from database import engine, get_db
from schemas.partidas import PartidaData, PartidaId
from schemas.player import PlayerData, PlayerId
from websocketsSetup.manager import ws_manager

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/partidas",
    tags=["partidas"]
)

@router.get('/', response_model=list[PartidaId])
async def get_partidas(db: Session = Depends(get_db)):
    return crud.get_partidas(db)

@router.get('/{id:int}', response_model=PartidaId)
async def get_partida_by_id(id: int, db: Session = Depends(get_db)):
    partida_by_id = crud.get_partida_by_id(db, id=id)

    if partida_by_id:
        return partida_by_id
    else:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

@router.post('/', response_model=PartidaId)
async def create_partida(partida: PartidaData, db: Session = Depends(get_db)):
    return crud.create_partida(db=db, partida=partida)

@router.delete('/{id:int}', response_model=PartidaId)
async def delete_partida(id: int, db: Session = Depends(get_db)):
    partida_by_id = crud.get_partida_by_id(db, id=id)

    if partida_by_id:
        crud.delete_partida(db, id)
    else:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    
    return partida_by_id

@router.websocket('/{partida_id:int}/jugadores/{nombre:str}')
async def join_to_partida(websocket: WebSocket, partida_id: int, nombre: str, db: Session = Depends(get_db)):
    partida_by_id = crud.get_partida_by_id(db, id=partida_id)

    if not partida_by_id:
        raise WebSocketException(code=status.WS_1013_TRY_AGAIN_LATER)
    try:
        player = crud.create_player(db, PlayerData(nombre=nombre, partida_id=partida_id))
        # WARNING: If we leave it like this, then a disconnection could produce "dangling players" (if we don't give a medium for reconnecting)
        await ws_manager.connect((player.partida_id, player.id), websocket)
        return player
    except WebSocketDisconnect:
        ws_manager.disconnect(player.id)