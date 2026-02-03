"""
DESAFIO — CONTROLE DE PRESENÇA (REGISTROS DE ACESSO)

Contexto:
Você trabalha em um sistema simples de controle de presença de uma empresa.
O sistema recebe registros de entrada e saída de funcionários ao longo do dia.

Os dados podem vir incompletos ou incorretos e precisam ser processados
para gerar um relatório final.

Cada registro deveria conter:
- employee_id (int)
- action (str): "in" ou "out"
- timestamp (int)

Objetivo:
Implementar uma função que receba uma lista de registros
e gere um relatório consolidado por funcionário.

Regras:
1) Ignore registros inválidos:
   - Faltar alguma chave obrigatória
   - action diferente de "in" ou "out"

2) Para cada funcionário (employee_id), gerar:
   - total_entries  -> quantidade de entradas
   - total_exits    -> quantidade de saídas
   - balance        -> total_entries - total_exits

Observações:
- Um funcionário pode ter apenas entrada, apenas saída ou ambos
- A ordem dos registros não é garantida
- Use apenas lista e dicionário

--------------------------------
SAÍDA ESPERADA
--------------------------------
{
    1: {"total_entries": 2, "total_exits": 1, "balance": 1},
    2: {"total_entries": 2, "total_exits": 0, "balance": 2},
    3: {"total_entries": 0, "total_exits": 1, "balance": -1}
}
"""

# Dataset para testes
records = [
    {"employee_id": 1, "action": "in", "timestamp": 5},
    {"employee_id": 1, "action": "out", "timestamp": 50},
    {"employee_id": 1, "action": "in", "timestamp": 70},

    {"employee_id": 2, "action": "in", "timestamp": 10},
    {"employee_id": 2, "action": "in", "timestamp": 20},

    {"employee_id": 3, "action": "out", "timestamp": 30},

    {"employee_id": 4, "action": "enter", "timestamp": 15},   # inválido
    {"action": "in", "timestamp": 40},                        # inválido
]


def analyze_attendance(records: list[dict]) -> dict:
    result = {}

    for record in records:
        if "employee_id" not in record:
            continue
        if "action" not in record:
            continue
        if "timestamp" not in record:
            continue

        action = record["action"]

        if action != "in" and action != "out":
            continue

        employee_id = record["employee_id"]

        if employee_id not in result:
            result[employee_id] = {
            "total_entries": 0,
            "total_exits" : 0,
            "balance": 0
        }


        if action == "in":
            result[employee_id]["total_entries"] += 1
            result[employee_id]["balance"] += 1
        if action == "out":
            result[employee_id]["total_exits"] += 1
            result[employee_id]["balance"] -=1

    return result


# Chamada de teste
result = analyze_attendance(records)
print(result)