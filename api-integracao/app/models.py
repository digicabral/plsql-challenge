from sqlalchemy import Column, Integer, String, Boolean, BigInteger, Float
from .database import Base

class Cupom(Base):
    __tablename__ = "cupom"
    __table_args__= {'sqlite_autoincrement': True}

    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True, nullable=False)
    cod_cupom = Column(String, nullable=False)
    usado = Column(Boolean, default=False, nullable=False)

class Movimento(Base):
    __tablename__ = "movimento_estoque"
    __table_args__= {'sqlite_autoincrement': True}

    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True, nullable=False)
    cod_produto = Column(Integer, nullable=False)
    cod_deposito = Column(BigInteger().with_variant(Integer, "sqlite"), nullable=False)
    qt_movimento = Column(Float, nullable=False)
    cd_tipo_operacao = Column(String(length=1), nullable=False)