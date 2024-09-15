from database import Base
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Player(Base):
    __tablename__ = 'players'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = mapped_column(String(255))
    
    partida_id = mapped_column(Integer, ForeignKey('partidas.id'), primary_key=True)
    partidas: Mapped["Partida"] = relationship(back_populates="players")