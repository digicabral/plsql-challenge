from fastapi import APIRouter
import random, string

router = APIRouter(
        prefix="/cupom",
        tags=['Cupom']
)


@router.get("/")
async def get_cupom():
    #Aqui eu poderia fazer uma requisição à API de cupons ou simplesmente ler de um banco de dados, mas para fim de exemplo vou gerar um aleatorio
    x = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return x
