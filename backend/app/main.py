from fastapi import FastAPI, HTTPException, Depends

from database import engine
from routers import partidas

app = FastAPI()


app.include_router(partidas.router)

@app.get('/')
def root():
    return 'Test String'
