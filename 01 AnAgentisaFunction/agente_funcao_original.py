# -*- coding: utf-8 -*-
a = 5
b = 3

somar = a + b
print(somar)

def somar(a, b):
    return a + b

resultado = somar(5,2)
print(resultado)

OPENROUTER_API_KEY= "sua_nova_chave"
print("ok")

import requests
import json

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
          "content": "Qual a capital do brasil?"
        }
      ],
    "reasoning": {"enabled": True}
  })
)

# Extract the assistant message with reasoning_details
response = response.json()
response = response['choices'][0]['message']['content']
print(response)

import requests
import json

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