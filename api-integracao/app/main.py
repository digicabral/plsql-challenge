from fastapi import FastAPI
from .routers import cupom

app = FastAPI()

app.include_router(cupom.router)
