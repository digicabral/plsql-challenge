from fastapi import Depends, APIRouter, status, HTTPException
import random, string
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from .. import models, schemas

router = APIRouter(
        prefix="/cupom",
        tags=['Cupom']
)


@router.get("/", response_model=schemas.CupomOut)
async def get_cupom(db: Session=Depends(get_db)):
    #Busco no banco de dados local (pool de cupons) o codigo de cupom mais antigo que foi consumido da fila
    min_cupom = db.query(func.min(models.Cupom.id)).scalar()
    cupom = db.query(models.Cupom).filter(models.Cupom.id == min_cupom).all()
    if not cupom:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                                    detail=f"Nenhum cupom encontrado")
    return cupom
