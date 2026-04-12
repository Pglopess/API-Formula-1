# API Formula 1

API REST construída com FastAPI como mini-projeto final da Fase 3 do plano de estudos backend Python.

Utiliza dados reais de F1 (1950–2024), banco SQLite, processamento com Pandas e validação com Pydantic.

---

## Endpoints

### Geral

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Verifica se a API está no ar |

### Pilotos

| Método | Rota | Parâmetros | Descrição |
|--------|------|------------|-----------|
| GET | `/pilotos` | `nacionalidade` (query, opcional) | Lista todos os pilotos, com filtro opcional por nacionalidade |
| GET | `/pilotos/{piloto_id}` | `piloto_id` (path, obrigatório) | Busca um piloto pelo ID |
| POST | `/pilotos` | body JSON | Cadastra um piloto novo |

**Exemplo de body para POST /pilotos:**
```json
{
  "nome": "Ayrton",
  "sobrenome": "Senna",
  "nacionalidade": "Brazilian",
  "nascimento": "1960-03-21"
}
```

### Corridas

| Método | Rota | Parâmetros | Descrição |
|--------|------|------------|-----------|
| GET | `/corridas` | `temporada` (query, opcional) | Lista corridas, com filtro opcional por temporada |

### Análises

| Método | Rota | Parâmetros | Descrição |
|--------|------|------------|-----------|
| GET | `/analises/artilheiros` | `temporada` (query, opcional) | Top 10 pilotos por pontos |
| GET | `/analises/equipes` | `temporada` (query, opcional) | Pontuação total por temporada |

---

## Como instalar e rodar

**Pré-requisitos:** Python 3.10+

**1. Clone o repositório**
```bash
git clone https://github.com/Pglopess/API-Formula-1.git
cd "API Formula 1"
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Baixe os dados**

Acesse [este dataset no Kaggle](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020) e baixe os arquivos `drivers.csv`, `races.csv` e `results.csv`. Coloque-os na pasta `data/`.

**5. Popule o banco de dados**
```bash
python scripts/populate_db.py
```

**6. Rode a API**
```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`

---

## Documentação automática

Com a API rodando, acesse:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## Estrutura do projeto

```
API Formula 1/
├── app/
│   ├── main.py          # instância do FastAPI e inclusão dos routers
│   ├── database.py      # conexão com SQLite
│   ├── models.py        # modelos Pydantic
│   └── routers/
│       ├── pilotos.py   # rotas de pilotos
│       ├── corridas.py  # rotas de corridas
│       └── analises.py  # rotas de análise com Pandas
├── scripts/
│   └── populate_db.py   # popula o banco com dados reais
├── .gitignore
├── requirements.txt
└── README.md
```