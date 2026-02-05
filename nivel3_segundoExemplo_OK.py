#gerador-texto-ia-python

# -*- coding: utf-8 -*-                  # Acentos funcionando

import sys                               # Acentos funcionando
sys.stdout.reconfigure(encoding="utf-8") # Acentos funcionando

from dotenv import load_dotenv # Carrega sua GROQ_API_KEY do arquivo .env
load_dotenv()                  # Carrega sua GROQ_API_KEY do arquivo .env

from langchain_groq import ChatGroq

# Criar o modelo
llm = ChatGroq(                     # Quero usar um modelo de linguagem
    model="llama-3.1-8b-instant",   # Quero usar um modelo de linguagem
    temperature=0                   # Quero usar um modelo de linguagem
)

# Prompt
prompt = "Explique o que é Python para iniciantes, em poucas linhas." # Testo que você envia para a IA.

# Chamada ao modelo
resposta = llm.invoke(prompt)       # invoke() envia o prompt
texto_resposta = resposta.content   # .content pega só o texto da resposta

# Mostrar no terminal               
print("Resposta da IA:\n")
print(texto_resposta)

# Salvar em arquivo TXT
with open("resposta_python.txt", "w", encoding="utf-8") as arquivo:  # Cria um arquivo, Usa UTF-8, Salva a resposta da IA
    arquivo.write(texto_resposta)                                    # Cria um arquivo, Usa UTF-8, Salva a resposta da IA

print("\n Resposta salva no arquivo resposta_python.txt")
