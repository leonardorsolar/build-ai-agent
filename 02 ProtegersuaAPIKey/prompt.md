Implementando a proteção da API Key da OpenRouter.

## Prompt – Etapa 01: Criar o arquivo .env

Crie um arquivo chamado .env na raiz do projeto e coloque nele a variável OPENROUTER_API_KEY com a minha chave da OpenRouter.
Não altere o código Python ainda. Apenas crie o arquivo e explique como ele será utilizado.

Configure a leitura da variável `OPENROUTER_API_KEY` pelo arquivo `.env`, utilizando `python-dotenv`.

## Prompt – Etapa 02: Criar e ativar o ambiente virtual

Crie um ambiente virtual Python chamado `.venv` na pasta do projeto e depois ative esse ambiente.

Explique de forma simples os comandos utilizados e como identificar se o ambiente virtual está ativo no terminal.

Não instale nenhuma biblioteca ainda e não altere o código Python.


## Prompt – Etapa 03: Instalar as bibliotecas
Com o ambiente virtual .venv ativado, instale as bibliotecas requests e python-dotenv utilizando o pip.

Explique de forma simples o comando utilizado e como verificar se as duas bibliotecas foram instaladas corretamente.

Não altere o código Python ainda.

## Prompt – Etapa 04: Proteger a chave no código Python

Agora, atualize o código Python para buscar a chave da OpenRouter no arquivo `.env`.

Utilize `import os`, `from dotenv import load_dotenv`, `load_dotenv()` e `os.getenv("OPENROUTER_API_KEY")`.

Substitua a chave que estava escrita diretamente no código pela variável carregada.

Mantenha as funções `perguntar_llm()` e `agente()` e todo o restante do funcionamento original.

Explique de forma simples o que foi alterado e teste se a aplicação continua funcionando.

## Prompt – Etapa 05: Proteger os arquivos do projeto com .gitignore

Crie ou atualize o arquivo `.gitignore` na raiz do projeto.

Adicione as seguintes pastas e arquivos:

- `.env` – impede que a chave da API seja enviada ao GitHub.
- `.venv/` – impede que o ambiente virtual seja enviado ao GitHub.

Explique de forma simples para que serve o `.gitignore` e por que precisamos proteger esses arquivos.

Não altere o código Python.

# Prompt – Etapa 06: Criar o arquivo requirements.txt

Crie o arquivo `requirements.txt` na raiz do projeto contendo as bibliotecas utilizadas:

- `requests`
- `python-dotenv`

Explique de forma simples para que serve esse arquivo e como ele permite instalar todas as dependências do projeto com um único comando.

Não altere o código Python.

# Prompt – Etapa 07: Testar o projeto

Faça um teste final do projeto.

1. Verifique se o arquivo `.env` está sendo carregado corretamente.
2. Confirme se a chave da OpenRouter está sendo encontrada pelo Python, sem exibi-la no terminal.
3. Execute o programa e envie a pergunta: "Qual é a capital da Alemanha?"
4. Verifique se o modelo retorna uma resposta corretamente.

Se encontrar algum erro, explique de forma simples e corrija apenas o necessário.

Ao finalizar, confirme se o projeto está funcionando e se a chave está protegida.

## Prompt – Etapa 08: Documentar como executar o projeto

Atualize o arquivo `README.md` com um tutorial simples explicando como configurar e executar o projeto em outro computador.

Inclua:

1. Como instalar o Python.
2. Como criar e ativar o ambiente virtual `.venv`.
3. Como instalar as bibliotecas usando `pip install -r requirements.txt`.
4. Como criar o arquivo `.env` e configurar a chave da OpenRouter.
5. Como executar o programa Python.

Use uma linguagem simples, pensando em pessoas que estão começando a programar.

Importante: nunca coloque a chave verdadeira da API no README.


## Prompt – Etapa 09: Tratar erros da API

Melhore a função `perguntar_llm()` para tratar possíveis erros na comunicação com a OpenRouter.

Considere situações como:
- Falta da chave da API.
- Falha na conexão com a internet.
- Chave inválida.
- Erro retornado pela API.

Mantenha o código simples e explique cada tratamento de erro.

## Prompt – Etapa 10: Verificar se a chave está protegida

Verifique se a chave da OpenRouter está protegida corretamente.

Confira:
- Se a chave está somente no arquivo `.env`.
- Se o `.env` está no `.gitignore`.
- Se não existe nenhuma chave escrita diretamente nos arquivos Python.
- Se a chave não está sendo exibida nos logs ou no terminal.

Não exponha a chave durante a verificação.


## Prompt – Etapa 11: Preparar o projeto para o GitHub
Prepare o projeto para ser enviado ao GitHub.

Verifique quais arquivos devem ser compartilhados e quais devem ficar apenas no computador do desenvolvedor.

Confira se `.env` e `.venv/` estão protegidos pelo `.gitignore`.

Crie uma lista dos comandos Git necessários para adicionar, salvar e enviar o projeto ao GitHub.

Explique cada comando de maneira simples para um iniciante.

## Prompt – Etapa 12: Criar uma função reutilizável

Verifique se a função perguntar_llm(mensagem) pode ser reutilizada em diferentes partes do projeto.

Crie um pequeno exemplo mostrando como enviar perguntas diferentes para a IA utilizando a mesma função.

Mantenha o código simples e explique por que reutilizar funções facilita a programação.


## Prompt – Etapa 13: Organizar o projeto
Organize os arquivos do projeto de maneira simples e adequada para um iniciante.

Verifique se os arquivos Python, `.env`, `.gitignore`, `.venv`, `requirements.txt` e `README.md` estão nos locais corretos.

Não crie pastas ou arquivos desnecessários. Mostre a estrutura final do projeto e explique a finalidade de cada arquivo.


Depois dessas etapas, considere o projeto concluído. O aluno terá aprendido:
- Como consumir uma API de IA.
- Como criar e utilizar funções Python.
- Como proteger uma API Key.
- Como utilizar ambientes virtuais.
- Como instalar bibliotecas com pip.
- Como organizar dependências.
- Como tratar erros.
- Como preparar um projeto para o GitHub.
Isso já constitui um excelente exercício introdutório de integração com LLMs usando Python.

**Etapa 14 manual: Testar o projeto completo**

Faça uma verificação final do projeto.

1. Confira se o arquivo `.env` está sendo carregado corretamente.
2. Verifique se a chave da OpenRouter está disponível, sem exibi-la.
3. Confira se as dependências estão instaladas.
4. Execute o arquivo `agente_funcao.py`.
5. Envie a pergunta: "Qual é a capital da Alemanha?"
6. Verifique se a resposta retornada pelo modelo está correta.

Se encontrar algum problema, explique o erro e corrija apenas o necessário.

Não exiba a chave verdadeira em nenhum momento.