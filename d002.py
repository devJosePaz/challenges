"""
DESAFIO – ANÁLISE DE EVENTOS DE RISCO (Python)

Contexto:
Você recebe uma lista de eventos gerados por sistemas internos.
Cada evento representa uma ocorrência isolada (erro, aviso ou informação).

Entrada:
Lista de eventos no formato:
{
    "event_id": str,
    "type": "ERROR" | "WARNING" | "INFO",
    "severity": int (1–5),
    "source": "SYSTEM" | "USER" | "INTEGRATION"
}

Regras:
1. Um evento deve gerar ALERTA se:
   - severity >= 4
   OU
   - type == "ERROR" e source == "INTEGRATION"

2. Eventos do tipo INFO nunca geram alerta,
   independentemente da severidade.

Saída esperada:
{
    "total_events": int,
    "alerts": [
        {
            "event_id": str,
            "reason": str
        }
    ]
}

Restrições:
- Python puro
- Sem libs externas
- Código simples e fácil de explicar
"""

