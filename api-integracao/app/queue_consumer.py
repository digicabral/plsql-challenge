from sqlalchemy.sql.expression import false
import random, string
from .database import get_db
from . import models, schemas
import time


def count_local_cupons():
    db_gen = get_db()
    db = next(db_gen)
    qt_local_disponivel = db.query(models.Cupom).filter(models.Cupom.usado == false()).count()
    return qt_local_disponivel

def get_from_kafka():
    #simula a busca da fonte de dados do kafka e inserção no pool de cupons local
    db_gen = get_db()
    db = next(db_gen)
    new_cupom = models.Cupom()
    #como estou gerando através de uma função local, não vai haver erros, mas se houvesse, poderia inserir em uma tabela para tentar novamente
    new_cupom.cod_cupom = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    db.add(new_cupom)
    db.commit()
    db.refresh(new_cupom)
    print('Cupom ', new_cupom.cod_cupom, ' inserido.')


def get_from_queue():
    # 1 - Verifico quantos cupons tenho no pool local
    # 2 - Se tiver menos de 10 manda buscar até o pool local atingir 10 novamente
    while True:
        #delay de 3 segundos para simular tempo de requisição à fila kafka
        time.sleep(3)
        if count_local_cupons() < 10:
            get_from_kafka()
        