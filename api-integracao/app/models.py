from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Cupom(Base):
    __tablename__ = "cupom"

    id = Column(Integer, primary_key=True, nullable=False)
    cod_cupom = Column(String, nullable=False)
    usado = Column(Boolean, server_default='FALSE', nullable=False)
