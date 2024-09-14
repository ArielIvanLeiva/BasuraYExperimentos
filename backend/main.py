from fastapi import FastAPI, HTTPException, Depends
from http import HTTPStatus
from sqlalchemy.orm import Session

import crud
from database import engine, localSession
from schemas import PartidaData, PartidaId
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    'http://localhost:3306'
]

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

@app.get('/')
def root():
    return 'Test String'

@app.get('/api/partidas/', response_model=list[PartidaId])
async def get_partidas(db: Session = Depends(get_db)):
    return crud.get_partidas(db)

@app.get('/api/partidas/{id:int}', response_model=PartidaId)
async def get_partida_by_id(id, db: Session = Depends(get_db)):
    partida_by_id = crud.get_partida_by_id(db, id=id)

    if partida_by_id:
        return partida_by_id
    else:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

@app.post('/api/partidas/', response_model=PartidaId)
async def create_partida(partida: PartidaData, db: Session = Depends(get_db)):
    return crud.create_partida(db=db, partida=partida)
