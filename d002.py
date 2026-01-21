"""
DESAFIO – ANÁLISE DE EVENTOS OPERACIONAIS (Python)

Contexto:
Sistema interno que recebe eventos operacionais de unidades
(logística, saúde, integrações).

Entrada:
Lista de eventos no formato:
{
    "event_id": str,
    "unit_id": str,
    "type": "ERROR" | "WARNING" | "INFO",
    "severity": int (1–5),
    "source": "SYSTEM" | "USER" | "INTEGRATION",
    "timestamp": str
}

Regras:
1. Evento é CRÍTICO se:
   - severity >= 4
   - OU (type == "ERROR" e source == "INTEGRATION")

2. Unidade é INSTÁVEL se possuir 3+ eventos críticos.

3. Eventos INFO nunca geram alerta.

Saída esperada:
{
    "total_events": int,
    "critical_events": int,
    "unstable_units": [unit_id],
    "alerts": [
        {
            "event_id": str,
            "unit_id": str,
            "reason": str
        }
    ]
}

Restrições:
- Python puro
- Código claro e explicável
"""
