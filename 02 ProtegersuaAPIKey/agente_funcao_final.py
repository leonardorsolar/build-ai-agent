import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def perguntar_llm(mensagem):
    # 1) Falta da chave: avisa antes de tentar chamar a API
    if not OPENROUTER_API_KEY:
        return "Erro: a variável OPENROUTER_API_KEY não foi encontrada. Verifique o arquivo .env."

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "nvidia/nemotron-3.5-super-vl:free",
                "messages": [{"role": "user", "content": mensagem}],
                "reasoning": {"enabled": True},
            }),
            timeout=60,  # não fica esperando para sempre
        )
    # 2) Falha de conexão / internet / tempo esgotado
    except requests.exceptions.RequestException as erro:
        return f"Erro de conexão com a OpenRouter: {type(erro).__name__}"

    # 3) Chave inválida
    if response.status_code in (401, 403):
        return "Erro: chave da API inválida ou sem permissão. Confira o valor no .env."

    # 4) Outros erros retornados pela API
    if response.status_code != 200:
        return f"Erro da API (código {response.status_code}): {response.text[:200]}"

    dados = response.json()
    if "choices" not in dados:
        return f"Resposta inesperada da API: {str(dados)[:200]}"

    return dados["choices"][0]["message"]["content"]


def agente(mensagem):
    resposta = perguntar_llm(mensagem)
    return resposta


# Só roda quando o arquivo é executado direto (não quando é importado)
if __name__ == "__main__":
    perguntas = [
        "Qual é a capital da Alemanha?",
        "Quanto é 15 vezes 3?",
        "Escreva uma frase curta sobre programação.",
    ]
    # A mesma função é reutilizada para perguntas diferentes
    for pergunta in perguntas:
        print(f"Pergunta: {pergunta}")
        print(f"Resposta: {agente(pergunta)}\n")
