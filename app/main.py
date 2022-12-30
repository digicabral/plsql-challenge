import threading
from fastapi import FastAPI
from .routers import cupom, estoque
from . import models
from .database import engine
from .queue_consumer import get_from_queue

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Rotas da API
app.include_router(cupom.router)
app.include_router(estoque.router)

#Aqui crio outra thread para fazer as solicitações à fila enquanto a aplicação principal fica rodando
thr = threading.Thread(target=get_from_queue, args=(), kwargs={})
thr.start()