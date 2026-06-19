import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

def buscar_contatos():
    try:
        resposta = supabase.table("contatos").select("*").execute()
        print(f"✅ {len(resposta.data)} contatos encontrados no Supabase")
        return resposta.data
    except Exception as e:
        print(f"❌ Erro ao buscar contatos: {e}")
        return []