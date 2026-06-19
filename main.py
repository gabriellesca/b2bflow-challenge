 
from services.supabase_service import buscar_contatos
from services.zapi_service import enviar_mensagem

def main():
    print("🚀 Iniciando envio de mensagens...")
    
    contatos = buscar_contatos()
    
    if not contatos:
        print("❌ Nenhum contato encontrado. Encerrando.")
        return
    
    for contato in contatos:
        nome = contato["nome"]
        telefone = contato["telefone"]
        enviar_mensagem(telefone, nome)
    
    print("✅ Processo finalizado!")

if __name__ == "__main__":
    main()