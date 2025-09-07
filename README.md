# Backend - Pedalboard

Backend da API para cadastro de pedalboards e pedais.

## Como rodar

### Opção 1: Scripts automatizados

Use os scripts na pasta `scripts/`:

```bash
# Rodar o projeto (instala dependências e inicia servidor)
bash scripts/rodar_projeto.sh

# Parar o projeto
bash scripts/parar_projeto.sh
```

### Opção 2: Manual

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o servidor:

```bash
python main.py
```

A API estará disponível em http://localhost:5002

## Estrutura do Projeto

```
puc-mvp-pedalboard-backend/
├── main.py                    # Aplicação principal
├── model/                     # Modelos SQLAlchemy
│   └── model.py
├── schemas/                   # Schemas Pydantic
│   └── schema.py
├── scripts/                   # Scripts de execução
│   ├── rodar_projeto.sh
│   └── parar_projeto.sh
├── requirements.txt           # Dependências Python
└── README.md                  # Este arquivo
```

## Tecnologias

- Python
- Flask
- SQLite
- SQLAlchemy
- Pydantic
