from database import Base
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

class Partida(Base):
    __tablename__ = 'partidas'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_partida = mapped_column(String(255))
    min_jugadores = mapped_column(Integer, nullable=True)
    max_jugadores = mapped_column(Integer, nullable=True)
    iniciada = mapped_column(Boolean, nullable=False)