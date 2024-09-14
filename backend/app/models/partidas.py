from database import Base
from sqlalchemy import Column, Enum as SQLEnum, Integer, String, Boolean

from mytypes import Privacidad

class Partida(Base):
    __tablename__ = 'partidas'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    tipo = Column(SQLEnum(Privacidad), nullable=False)
    iniciada = Column(Boolean)