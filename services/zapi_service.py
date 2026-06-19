import os
import requests
from dotenv import load_dotenv

load_dotenv()

instance = os.getenv("ZAPI_INSTANCE")
token = os.getenv("ZAPI_TOKEN")
client_token = os.getenv("ZAPI_CLIENT_TOKEN")

def enviar_mensagem(telefone, nome):
    url = f"https://api.z-api.io/instances/{instance}/token/{token}/send-text"
    
    headers = {
        "Client-Token": client_token
    }
    
    payload = {
        "phone": telefone,
        "message": f"Olá, {nome} tudo bem com você?"
    }
    
    try:
        resposta = requests.post(url, json=payload, headers=headers)
        if resposta.status_code == 200:
            print(f"✅ Mensagem enviada para {nome} ({telefone})")
        else:
            print(f"❌ Erro ao enviar para {nome}: {resposta.status_code} - {resposta.text}")
    except Exception as e:
        print(f"❌ Erro ao enviar para {nome}: {e}")