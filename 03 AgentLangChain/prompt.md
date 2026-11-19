Criando agente com o framework LangChain

# Prompt 01: navegador
O que é o LangChain? Quais outros frameworks existem? Como escolher entre eles?

# Prompt 02: navegador
Defina de forma objetiva a estrutura básica da construção de um agente:
entrada, LLM, recuperação de informação, ferramentas, memória e saída.
Inclua um diagrama para facilitar o entendimento.

# Prompt 03: navegador
Crie um tutorial simples, em português, sobre como criar um agente com o framework LangChain (Python).

Escopo:
- Sem ferramentas, sem memória e sem recuperação de dados.
- Apenas entrada do usuário, LLM e saída.
- Use o provedor OpenAI (modelo gpt-4o-mini) e a variável OPENAI_API_KEY.

Inclua:
1. Instalação das dependências.
2. Configuração da chave de API usando um arquivo .env (sem colocar a chave no código).
3. Código completo e comentado, que eu possa copiar e executar.
4. Explicação curta de cada parte do código.
5. Exemplo de execução, com a pergunta e a resposta esperada.

# Prompt 03: vscode
Crie neste projeto um agente simples com o framework LangChain (Python), no arquivo agente.py.

Escopo:
- Sem ferramentas, sem memória e sem recuperação de dados.
- Apenas entrada do usuário, LLM e saída.
- Use o provedor OpenAI (modelo gpt-4o-mini) e a variável OPENAI_API_KEY.

Forma de trabalho (iterativa, passo a passo):
- Execute UM passo por vez. Não avance para o próximo sem a minha confirmação.
- Em cada passo: faça a alteração, explique em linguagem simples o que foi feito e por quê, e comente o código em português.
- Ao final de cada passo, pergunte: "Posso seguir para o próximo passo?" e aguarde a minha resposta.

Passos:
1. Crie o requirements.txt com as dependências.
2. Crie o .env.example com o nome da variável da chave de API (sem a chave real) e adicione o .env ao .gitignore.
3. Crie o agente.py com a configuração do modelo (carregar o .env e instanciar o LLM).
4. Inclua no agente.py a entrada do usuário e a chamada ao LLM.
5. Inclua a exibição da resposta (saída) e finalize o agente.py.
6. Explique como instalar as dependências e executar o agente.


# Prompt 04: vscode
Inclua o uso de memória no arquivo agente.py, para o agente lembrar as mensagens anteriores da conversa.
Mantenha o restante do código e comente as partes novas em português.

Forma de trabalho (iterativa, passo a passo):
- Divida a tarefa em passos pequenos e execute UM por vez.
- Em cada passo: faça a alteração, explique o que foi feito e por quê.
- Ao final de cada passo, pergunte: "Posso seguir para o próximo passo?" e aguarde a minha resposta.

# Prompt 05: vscode
Inclua no arquivo agente.py o uso de ferramentas, com uma ferramenta que soma dois números.
Mantenha a memória e o restante do código, e comente as partes novas em português.

Forma de trabalho (iterativa, passo a passo):
- Divida a tarefa em passos pequenos e execute UM por vez.
- Em cada passo: faça a alteração, explique o que foi feito e por quê.
- Ao final de cada passo, pergunte: "Posso seguir para o próximo passo?" e aguarde a minha resposta.

# Prompt 06: vscode
Inclua no arquivo agente.py uma ferramenta de busca na web (web_search).
Atualize o requirements.txt e o .env.example com o que for necessário (por exemplo, a chave da ferramenta de busca).
Mantenha a memória e a ferramenta de soma, e comente as partes novas em português.

Forma de trabalho (iterativa, passo a passo):
- Divida a tarefa em passos pequenos e execute UM por vez.
- Em cada passo: faça a alteração, explique o que foi feito e por quê.
- Ao final de cada passo, pergunte: "Posso seguir para o próximo passo?" e aguarde a minha resposta.
