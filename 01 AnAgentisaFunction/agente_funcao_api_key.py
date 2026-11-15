import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def perguntar_llm(mensagem):
    # First API call with reasoning
    response = requests.post(
      url="https://openrouter.ai/api/v1/chat/completions",
      headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
      },
      data=json.dumps({
        "model": "nvidia/nemotron-3.5-super-vl:free",
        "messages": [
            {
              "role": "user",
              "content": mensagem
            }
          ],
        "reasoning": {"enabled": True}
      })
    )

    # Extract the assistant message with reasoning_details
    response = response.json()
    response = response['choices'][0]['message']['content']
    return response

mensagem = "Qual a capital da Alemanha?"

def agente(mensagem):
    resposta = perguntar_llm(mensagem)
    return resposta

saida = agente(mensagem)
print(saida)