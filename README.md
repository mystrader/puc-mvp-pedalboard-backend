<img width="1472" height="376" alt="image" src="https://github.com/user-attachments/assets/8adeb50f-c0ca-4f6c-b89d-4d54a1a136ba" />


# Backend - Pedalboard

Backend da API para cadastro de pedalboards e pedais.

### Link do vídeo de apresentação 

(Link do video de apresentação do projeto)[https://youtu.be/z3Ol0xYJIug] 


---

## Como rodar

### Opção 1: Scripts automatizados

Use os scripts na pasta `scripts/`:

> 🔹 PARA O PROFESSOR:  RODAR O SCRIPT ABAIXO NO BASH  PARA RODAR AUTOMATICAMENTE 

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

## Diagrama

```
┌─────────────────────────────────┐
│           PEDALBOARDS           │
├─────────────────────────────────┤
│ 🔑 id (PK)                     │
│    name                         │
│    description                  │
│    user_id                      │
│    created_at                   │
│    updated_at                   │
└─────────────────────────────────┘
                │
                │ 1:N
                │
                ▼
┌─────────────────────────────────┐
│             PEDALS              │
├─────────────────────────────────┤
│ 🔑 id (PK)                     │
│    name                         │
│    brand                        │
│    category                     │
│    description                  │
│ 🔗 pedalboard_id (FK)          │
│    created_at                   │
│    updated_at                   │
└─────────────────────────────────┘

```



## Tecnologias

- Python
- Flask
- SQLite
- SQLAlchemy
- Pydantic
