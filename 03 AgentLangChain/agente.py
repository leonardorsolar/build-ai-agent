import os
import sys

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.tools import tool
from langchain_tavily import TavilySearch

load_dotenv()


@tool
def somar(a: float, b: float) -> float:
    """Soma dois números e retorna o resultado."""
    return a + b


@tool
def web_search(consulta: str) -> str:
    """Pesquisa na internet e retorna os resultados mais relevantes.
    Use para notícias, fatos recentes ou informações que você não conhece."""
    resultado = busca_tavily.invoke({"query": consulta})

    if isinstance(resultado, str):
        return resultado

    trechos = [
        f"- {item['title']} ({item['url']})\n  {item['content']}"
        for item in resultado.get("results", [])
    ]
    return "\n".join(trechos) or "Nenhum resultado encontrado."


if not os.getenv("OPENAI_API_KEY"):
    sys.exit("Erro: OPENAI_API_KEY não encontrada. Crie o arquivo .env a partir do .env.example.")

if not os.getenv("TAVILY_API_KEY"):
    sys.exit("Erro: TAVILY_API_KEY não encontrada. Adicione a chave do Tavily no arquivo .env.")

busca_tavily = TavilySearch(max_results=3)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
)

ferramentas = [somar, web_search]
ferramentas_por_nome = {f.name: f for f in ferramentas}

llm_com_ferramentas = llm.bind_tools(ferramentas)

historico = [
    SystemMessage(content=(
        "Você é um assistente prestativo que responde em português. "
        "Quando precisar de informações atuais, use a ferramenta web_search "
        "e cite os links das fontes na resposta."
    )),
]

MAX_MENSAGENS = 10

print("Converse com o agente. Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ").strip()

    if pergunta.lower() == "sair":
        print("Encerrando. Até mais!")
        break

    if not pergunta:
        print("Nenhuma pergunta digitada. Tente novamente.")
        continue

    historico.append(HumanMessage(content=pergunta))
    resposta = llm_com_ferramentas.invoke(historico)
    historico.append(resposta)

    while resposta.tool_calls:
        for chamada in resposta.tool_calls:
            ferramenta = ferramentas_por_nome[chamada["name"]]
            print(f"[usando ferramenta {chamada['name']} com {chamada['args']}]")
            historico.append(ferramenta.invoke(chamada))

        resposta = llm_com_ferramentas.invoke(historico)
        historico.append(resposta)

    if len(historico) > MAX_MENSAGENS + 1:
        inicio = len(historico) - MAX_MENSAGENS
        while inicio > 1 and not isinstance(historico[inicio], HumanMessage):
            inicio -= 1
        historico = [historico[0]] + historico[inicio:]

    print(f"Agente: {resposta.content}\n")
