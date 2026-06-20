# b2bflow Challenge — Python + Supabase + Z-API

Este projeto consiste em um script Python que lê contatos cadastrados no Supabase e envia, via Z-API, a mensagem personalizada "Olá, <nome_contato> tudo bem com você?" para cada contato encontrado.

## Tecnologias utilizadas

- Python 3.13
- Supabase (banco de dados)
- Z-API (envio de WhatsApp)
- requests
- python-dotenv

## Setup da tabela no Supabase

Crie um projeto no [Supabase](https://supabase.com) e uma tabela chamada `contatos` com as seguintes colunas:

| Coluna       | Tipo        | Descrição                                            |
|--------------|-------------|-------------------------------------------------------|
| id           | int8        | Gerado automaticamente                                |
| created_at   | timestamptz | Gerado automaticamente                                |
| nome         | text        | Nome do contato                                       |
| telefone     | text        | Telefone no formato 55DDDNUMERO (ex: 5511999999999)   |

Insira de 1 a 3 contatos na tabela antes de rodar o script.

## Variáveis de ambiente (.env)

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
SUPABASE_URL=sua_url_do_projeto_supabase

SUPABASE_KEY=sua_chave_anon_do_supabase

ZAPI_INSTANCE=id_da_sua_instancia_zapi

ZAPI_TOKEN=token_da_sua_instancia_zapi

ZAPI_CLIENT_TOKEN=token_de_seguranca_da_conta_zapi

**Importante:** o arquivo `.env` não deve ser commitado — ele já está listado no `.gitignore`.

## Como rodar

1. Clone o repositório:
git clone https://github.com/gabriellesca/b2bflow-challenge.git

cd b2bflow-challenge

2. Crie e ative o ambiente virtual:
python -m venv venv

venv\Scripts\activate

3. Instale as dependências:
pip install -r requirements.txt

4. Configure o arquivo `.env` (veja seção acima).

5. Execute o script:
python main.py

## Estrutura do projeto
b2bflow-challenge/

├── services/

│   ├── supabase_service.py   # Busca os contatos no Supabase

│   └── zapi_service.py       # Envia mensagens via Z-API

├── main.py                   # Orquestra o fluxo completo

├── .env                      # Credenciais (não versionado)

└── .gitignore

## Tratamento de erros

O script possui tratamento de erros (`try/except`) tanto na busca dos contatos no Supabase quanto no envio das mensagens via Z-API, com logs no console indicando sucesso (✅) ou falha (❌) em cada etapa.
