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

event_list = [
    # Deve gerar alerta: severity >= 4
    {
        "event_id": "evt_001",
        "type": "WARNING",
        "severity": 4,
        "source": "SYSTEM"
    },

    # Deve gerar alerta: ERROR + INTEGRATION
    {
        "event_id": "evt_002",
        "type": "ERROR",
        "severity": 2,
        "source": "INTEGRATION"
    },

    # NÃO deve gerar alerta: INFO nunca gera alerta
    {
        "event_id": "evt_003",
        "type": "INFO",
        "severity": 5,
        "source": "SYSTEM"
    },

    # NÃO deve gerar alerta: ERROR comum, severity baixa, source USER
    {
        "event_id": "evt_004",
        "type": "ERROR",
        "severity": 2,
        "source": "USER"
    }
]


def event_system(event_list:list[dict]) -> dict:
    total_events = 0
    alerts = []
 

    for event in event_list:
        total_events += 1
        # RULE 02 - IGNORED EVENT WITH TYPE 'INFO'
        if event["type"] == "INFO":
            continue
        # RULE 01 - SEVERITY >= 4
        if event["severity"] >= 4:
            alert_generated = {"event_id": event["event_id"],"reason": "SEVERITY >= 4"}
            alerts.append(alert_generated)

        # RULE 02 - type == "ERROR" and source == "INTEGRATION"
        if event["type"] == "ERROR" and event["source"] == "INTEGRATION":
            alert_generated = {"event_id": event["event_id"], "reason": "ERROR FROM INTEGRATION"}
            alerts.append(alert_generated)

        
    result = {
        "total_events": total_events,
        "alerts": alerts
    }

    return result  

analyze = event_system(event_list)
print(analyze)

