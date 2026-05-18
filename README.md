# Agente Financeiro IA - Backend

## 📌 Sobre o Projeto

O **Agente Financeiro IA** é uma API backend desenvolvida com **Python + FastAPI** focada em análise técnica automatizada de ativos financeiros.

O sistema realiza coleta de dados do mercado em tempo real utilizando a biblioteca **yFinance**, executa análises quantitativas com indicadores técnicos e gera sinais inteligentes de compra e venda.

O projeto foi construído seguindo uma arquitetura modular e escalável, utilizando:

* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* Pandas
* TA (Technical Analysis)
* yFinance

---

# 🚀 Funcionalidades

## ✅ Análise técnica automatizada

O sistema analisa ativos financeiros utilizando:

* RSI (Relative Strength Index)
* Médias móveis MM9 e MM21
* Tendência de mercado
* Força da tendência
* Recomendação automática

---

## ✅ Scanner inteligente de mercado

O endpoint `/signals` executa um scanner automático em múltiplos ativos e retorna:

* Sinais de compra
* Sinais de venda
* Tendência do ativo
* Força da tendência
* Score técnico

---

## ✅ Histórico de preços

Consulta histórica de ativos financeiros:

* Abertura
* Fechamento
* Máxima
* Mínima
* Volume
* Indicadores técnicos

---

## ✅ Integração com PostgreSQL

O projeto possui integração completa com banco de dados PostgreSQL utilizando SQLAlchemy ORM.

As análises podem ser persistidas futuramente para:

* Histórico de análises
* Dashboard financeiro
* Machine Learning
* Analytics
* Controle de usuários

---

# 🛠️ Tecnologias Utilizadas

| Tecnologia | Função               |
| ---------- | -------------------- |
| Python     | Linguagem principal  |
| FastAPI    | Framework backend    |
| PostgreSQL | Banco de dados       |
| SQLAlchemy | ORM                  |
| Pandas     | Manipulação de dados |
| yFinance   | Dados financeiros    |
| TA         | Indicadores técnicos |
| Uvicorn    | Servidor ASGI        |

---

# 📂 Estrutura do Projeto

```bash
backend/
│
├── app/
│   ├── api/
│   │   └── market_routes.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── models.py
│   │   └── __init__.py
│   │
│   ├── models/
│   │   └── market_model.py
│   │
│   ├── services/
│   │   ├── market_service.py
│   │   ├── analysis_service.py
│   │   └── signal_service.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── venv/
├── requirements.txt
└── README.md
```

---

# ⚙️ Instalação do Projeto

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/jeansoto516-a11y/agente-financeiro-ia-backend.git
```

---

## 2️⃣ Entrar na pasta do projeto

```bash
cd agente-financeiro-ia-backend/backend
```

---

## 3️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

---

## 4️⃣ Ativar ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

---

## 5️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

# 🐘 Configuração do PostgreSQL

## Criar banco de dados

Abra o PostgreSQL e execute:

```sql
CREATE DATABASE agente_financeiro;
```

---

## Configurar conexão

Abra:

```bash
app/database/connection.py
```

Edite a variável:

```python
DATABASE_URL = "postgresql://postgres:SUA_SENHA@localhost:5432/agente_financeiro"
```

Substitua:

```python
SUA_SENHA
```

pela senha do seu PostgreSQL.

---

# ▶️ Executar o Projeto

Execute:

```bash
python -m uvicorn app.main:app --reload
```

A API ficará disponível em:

```bash
http://127.0.0.1:8000
```

Swagger:

```bash
http://127.0.0.1:8000/docs
```

---

# 📡 Endpoints da API

## 🔹 Buscar ativo

```http
GET /market/{symbol}
```

Exemplo:

```http
GET /market/BTC-USD
```

---

## 🔹 Histórico de preços

```http
GET /historico
```

Parâmetros:

* symbol
* start
* end

Exemplo:

```http
GET /historico?symbol=BTC-USD&start=2025-01-01&end=2026-01-01
```

---

## 🔹 Ranking de ativos

```http
GET /top-assets
```

---

## 🔹 Análise técnica

```http
GET /analysis/{symbol}
```

Exemplo:

```http
GET /analysis/BTC-USD
```

---

## 🔹 Scanner de sinais

```http
GET /signals
```

Retorna os principais sinais técnicos do mercado.

---

# 📈 Indicadores Utilizados

## RSI

O RSI mede força e velocidade dos movimentos do mercado.

* RSI > 70 → Sobrecompra
* RSI < 30 → Sobrevenda

---

## Médias Móveis

### MM9

Média móvel curta.

### MM21

Média móvel longa.

Cruzamentos entre MM9 e MM21 são utilizados para identificar tendências.

---

# 🔥 Melhorias Futuras

* Autenticação JWT
* Sistema de usuários
* Dashboard frontend
* Machine Learning
* IA preditiva
* Deploy em nuvem
* Histórico persistente de análises
* WebSockets para sinais em tempo real
* Integração com corretoras

---

# 👨‍💻 Desenvolvedor

Desenvolvido por Jean Carlos Soto Barbosa.

Focado em:

* Engenharia de Software
* Backend Development
* APIs REST
* Inteligência Artificial
* Sistemas Financeiros
* Análise Quantitativa

---

# 📄 Licença

Este projeto está sob a licença MIT.
