from pydantic import BaseModel

class MovimentoCreate(BaseModel):
    cod_produto: int = '9850147'
    cod_deposito: int = '15'
    qt_movimento: float = '2'
    cd_tipo_operacao: str = 'B'

    class Config:
        orm_mode = True