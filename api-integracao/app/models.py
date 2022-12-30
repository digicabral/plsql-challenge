from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from .database import Base

class Cupom(Base):
    __tablename__ = "cupom"
    __table_args__= {'sqlite_autoincrement': True}

    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True, nullable=False)
    cod_cupom = Column(String, nullable=False)
    usado = Column(Boolean, default=False, nullable=False)
