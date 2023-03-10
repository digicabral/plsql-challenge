from pydantic import BaseModel

class CupomCreate(BaseModel):
    id: int
    cod_cupom: str
    usado: bool = False

class CupomOut(BaseModel):
    cod_cupom: str

    class Config:
            orm_mode = True

class CupomUpdate(BaseModel):
    usado: bool = True

