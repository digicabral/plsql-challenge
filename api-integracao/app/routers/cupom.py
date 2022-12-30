from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.sql.expression import false
import random, string
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from .. import models, schemas
from ..schemas.cupom import CupomCreate, CupomOut, CupomUpdate

router = APIRouter(
        prefix="/cupom",
        tags=['Cupom']
)

def set_cupom_usado(id):
    db_gen = get_db()
    db = next(db_gen)
    cupom_query = db.query(models.Cupom).filter(models.Cupom.id == id)
    cupom_query.update({'usado':True})
    db.commit()

@router.get("/", response_model=CupomOut)
async def get_cupom(db: Session=Depends(get_db)):
    #Busco no banco de dados local (pool de cupons) o codigo de cupom mais antigo que foi consumido da fila e que nao foi utilizado ainda
    min_cupom = db.query(func.min(models.Cupom.id)).filter(models.Cupom.usado == false()).scalar()
    cupom = db.query(models.Cupom).filter(models.Cupom.id == min_cupom).first()
    if not cupom:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                                    detail=f"Nenhum cupom encontrado.")
    set_cupom_usado(min_cupom)
    return cupom
