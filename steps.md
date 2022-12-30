Abre o CMD como adm e digita python -m venv nomedoambiente
roda o .bat de dentro da pasta do virtualenv 

pip install fastapi

Para rodar a aplicação
uvicorn main:app --reload

para conseguir usar o routers, será necessário criar o package
Cria a pasta app e coloca tudo la dentro, em seguida cria o __init__.py

Passa a utilizar o comando uvicorn app.main:app --reload

Gerar as dependencias
pip install pip_chill
pip-chill --no-version> requirements.txt

heroku git: remote -a americanas-backend-api