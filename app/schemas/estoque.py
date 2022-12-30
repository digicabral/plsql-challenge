from pydantic import BaseModel

class MovimentoCreate(BaseModel):
    cod_produto: int
    cod_deposito: int
    qt_movimento: float
    cd_tipo_operacao: str

    class Config:
        orm_mode = True