from fastapi import APIRouter
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from http import HTTPStatus

import crud.partidas as crud
from models.partidas import Base
from database import engine, get_db
from schemas.partidas import PartidaData, PartidaId

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/partidas",
    tags=["partidas"]
)

@router.get('/', response_model=list[PartidaId])
async def get_partidas(db: Session = Depends(get_db)):
    return crud.get_partidas(db)

@router.get('/{id:int}', response_model=PartidaId)
async def get_partida_by_id(id, db: Session = Depends(get_db)):
    partida_by_id = crud.get_partida_by_id(db, id=id)

    if partida_by_id:
        return partida_by_id
    else:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

@router.post('/', response_model=PartidaId)
async def create_partida(partida: PartidaData, db: Session = Depends(get_db)):
    return crud.create_partida(db=db, partida=partida)