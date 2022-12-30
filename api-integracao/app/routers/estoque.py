from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from ..schemas.estoque import MovimentoCreate

router = APIRouter(
    prefix="/movimentaestoque",
    tags=['Movimenta Estoque'],
    
)

@router.post("/", response_model= MovimentoCreate)
async def insere_movimento_estoque(movimento: MovimentoCreate, db: Session = Depends(get_db)):
    new_movimento = models.Movimento(**movimento.dict())
    db.add(new_movimento)
    db.commit()
    db.refresh(new_movimento)
    return new_movimento