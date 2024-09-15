from typing import List
from database import Base
from sqlalchemy import Enum as SQLEnum, Integer, String, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from mytypes import Privacidad

class Partida(Base):
    __tablename__ = 'partidas'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = mapped_column(String(255))
    tipo = mapped_column(SQLEnum(Privacidad), nullable=False)
    iniciada = mapped_column(Boolean)
    
    players: Mapped[List["Player"]] = relationship(back_populates="partidas")