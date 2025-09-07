#!/bin/bash
# para processos do Flask e desativa ambiente virtual

# mata processos do Flask na porta 5002
echo "🛑 Parando servidor Flask..."
pkill -f "python.*main.py" 2>/dev/null || echo "Nenhum processo Flask encontrado."

# mata processos na porta 5002
lsof -ti:5002 | xargs kill -9 2>/dev/null || echo "Porta 5002 liberada."

# desativa ambiente virtual se ativo
if [ -n "$VIRTUAL_ENV" ]; then
  deactivate 2>/dev/null || echo "Ambiente virtual desativado."
else
  echo "⚠️ Nenhum ambiente virtual ativo."
fi

echo "✅ Projeto parado com sucesso!"