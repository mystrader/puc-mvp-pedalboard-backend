#!/bin/bash
# ativa o ambiente virtual, instala dependências e sobe o flask

# cria venv se não existir
if [ ! -d "venv" ]; then
  echo "🔧 Criando virtualenv..."
  python3 -m venv venv
fi

# ativa o ambiente virtual
source venv/bin/activate

# instala as dependências
echo "📦 Instalando dependências..."
pip install -r requirements.txt

# roda o flask
echo "🚀 Subindo API Flask em http://localhost:5002"
python main.py