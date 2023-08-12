### FastAPI

*Estrutura - Diretórios deste projeto* 
core => Diretório onde está os sources da aplicação
schemas => Arquivos com os serializadores. Converções Object to Json, Json to Object.
models => Contém os arquivos com os modelos dos recursos
routers => Onde está localizado as rotas da API
api => Localizado os endpoints da API


*Instalações*
```python
# fastapi => Servico assíncrono
# uvicorn => Servidor ASGI(async server gateway interface) de alta performance em python para execução de código assíncrono para web.
pip install fastapi uvicorn gunicorn
```

*Executando com servidor uvicorn*
```python 
# uvicorn => Servidor
# main => arquivo raiz
# app => Objeto instanciado com o FastAPI()
uvicorn main:app --reload
```

*Executando servidor Web gunicorn integrando com o Uvicorn*
```python 
# gunicorn => Servidor
# main => arquivo raiz
# app => Objeto instanciado com o FastAPI()
# -w => quantidade de worker
# -k ou --worker-class => classe do Uvicorn dos workers
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

*Instalação de librarys para PDF*
Para gerar arquivos em html para gerar PDF é necessário instalar a library pdfkit no projeto e no servidor onde está hospedado a aplicação instalar a ferramenta whtmltopdf 
```python
# Instalando a lib python 
pip install pdfkit

# Instalando a ferramenta whtmltopdf(Testada a v 0.12.3) no servidor. Site: https://wkhtmltopdf.org/downloads.html
# MAC
brew install homebrew/cask/whtmltopdf  # Mac
# LINUX
sudo apt-get install whtmltopdf
```

*Instalação de librarys para DB PostgreSQL*
Librarys para conexão assíncronas e comunicação por ORM com o banco PostgreSQL. 
```python
pip install sqlalchemy psycopg2-binary asyncpg
```

