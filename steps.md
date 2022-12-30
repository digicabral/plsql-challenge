conda create --name envplsql
conda activate envplsql

pip install fastapi

Para rodar a aplicação
uvicorn main:app --reload

para conseguir usar o routers, será necessário criar o package
Cria a pasta app e coloca tudo la dentro, em seguida cria o __init__.py

Passa a utilizar o comando uvicorn app.main:app --reload

Gera as dependencias
pip freeze > requirements.txt

heroku git: remote -a americanas-backend-api