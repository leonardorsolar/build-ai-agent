# Proteger a API Key (OpenRouter)

### 1. Revogar a chave exposta
- Acesse https://openrouter.ai/keys
- Apague a chave antiga e crie uma nova.

### 2. Guardar a chave em um `.env`
```bash
echo 'OPENROUTER_API_KEY=sua_nova_chave' > .env
echo '.env' >> .gitignore
```

### 3. Instalar o python-dotenv (em um ambiente virtual)
O Ubuntu/Debian bloqueia `pip install` global (erro `externally-managed-environment`). Use um venv:
```bash
sudo apt install python3-full python3-venv   # só se faltar
python3 -m venv .venv
source .venv/bin/activate
pip install python-dotenv requests
echo '.venv/' >> .gitignore
```
Sempre rode `source .venv/bin/activate` antes de executar o script.

### 4. Ler a chave no código
```python
import os
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
```
### PIP 
O pip é o instalador de pacotes do Python. O nome vem de "Pip Installs Packages".

Ele baixa bibliotecas feitas por outras pessoas, do repositório público PyPI (pypi.org), e instala no seu ambiente Python. Assim você não precisa escrever tudo do zero.

Exemplos de uso:


pip install requests        # instala uma biblioteca
pip install python-dotenv   # instala outra
pip list                    # mostra o que está instalado
pip uninstall requests      # remove
pip freeze > requirements.txt   # salva a lista de pacotes do projeto
pip install -r requirements.txt # instala tudo de uma lista

### venv 
python3 -m venv .venv cria o ambiente virtual.

python3 -m venv roda o módulo venv do Python, que cria uma cópia isolada do Python.
.venv é o nome da pasta criada. O ponto na frente deixa a pasta oculta, e é o nome mais usado por convenção.
Dentro dela ficam o Python e o pip do projeto, e é lá que os pacotes serão instalados.
Você só roda esse comando uma vez por projeto.

### activate 
source .venv/bin/activate ativa o ambiente.

Ele muda o terminal para usar o Python e o pip da pasta .venv, em vez dos do sistema.
O terminal passa a mostrar (.venv) no começo da linha.
Com o ambiente ativo, pip install instala dentro do .venv. Por isso o erro externally-managed-environment some.
Você precisa ativar de novo toda vez que abrir um terminal novo.

### deactivate 
Para sair do ambiente, use deactivate
