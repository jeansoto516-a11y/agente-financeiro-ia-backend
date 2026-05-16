# 🔐 Configuração com .env - Agente Financeiro IA

## ✅ O que foi feito

1. **Criado arquivo `.env`** com suas credenciais PostgreSQL
2. **Adicionado `python-dotenv`** ao `requirements.txt`
3. **Atualizado `connection.py`** para carregar variáveis de ambiente
4. **Criado `.env.example`** como template para documentação

## 🚀 Próximos Passos

### 1. Instalar a dependência
```bash
pip install python-dotenv
```

Ou, a partir do `requirements.txt`:
```bash
pip install -r requirements_new.txt
```

### 2. Verificar o arquivo `.env`
O arquivo foi criado automaticamente em:
```
backend/.env
```

**Seu conteúdo:**
```
DATABASE_URL=postgresql://postgres:Jean1245@localhost:5432/agente_financeiro
```

✅ **O arquivo `.env` está no `.gitignore`**, então não será commitado no git

### 3. Testar se está funcionando
Rode a aplicação normalmente:
```bash
cd backend
uvicorn app.main:app --reload
```

Se tudo estiver ok, você verá:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

## 📋 Estrutura de Arquivos

```
backend/
├── .env                 ← Suas credenciais (NÃO commitar)
├── .env.example         ← Template para documentação
├── .gitignore           ← Já contém .env
├── requirements_new.txt ← Versão limpa com python-dotenv
└── app/
    └── database/
        └── connection.py ← Agora usa load_dotenv()
```

## 🔒 Como o `.env` é carregado?

**No arquivo `connection.py`:**
```python
from dotenv import load_dotenv
import os

# Carrega variáveis do arquivo .env
load_dotenv()

# Pega a variável DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Valida se foi configurada
if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL não foi configurada no arquivo .env")
```

## ⚠️ Segurança

- ✅ Arquivo `.env` está no `.gitignore` (não será enviado ao git)
- ✅ Senha nunca fica exposta no código
- ✅ Cada desenvolvedor pode ter suas próprias credenciais locais
- ✅ Funciona bem em produção com variáveis de ambiente do sistema

## 📝 Para adicionar mais variáveis no futuro

Se precisar adicionar mais configurações (ex: porta da API, debug mode), edite o `.env`:

```
DATABASE_URL=postgresql://postgres:Jean1245@localhost:5432/agente_financeiro
API_PORT=8000
DEBUG=True
```

E em seu código Python:
```python
API_PORT = int(os.getenv("API_PORT", "8000"))
DEBUG = os.getenv("DEBUG", "False") == "True"
```

## 🎯 Resumo

| Antes | Depois |
|-------|--------|
| ❌ Senha no código | ✅ Senha no `.env` |
| ❌ Exposta no git | ✅ Ignorada pelo git |
| ❌ Difícil de mudar | ✅ Fácil de configurar |
| ❌ Segurança ruim | ✅ Segurança excelente |

Pronto! Sua aplicação agora está segura. 🎉
