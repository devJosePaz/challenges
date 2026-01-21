"""
DESAFIO — BANCO DIGITAL (PREVENÇÃO A FRAUDES)

Contexto:
Você atua em um time de prevenção a fraudes de um banco digital em São Paulo.
O sistema recebe transações financeiras e precisa gerar alertas simples
para análise humana.

Cada transação possui os seguintes campos:
- transaction_id (str)
- account_id (str)
- amount (float)
- currency (str)
- timestamp (ISO 8601)
- transaction_type (str)

Objetivo:
Implementar uma função que receba uma lista de transações e retorne
um relatório consolidado de risco.

Regras de risco implementadas:
1) Valor da transação maior que R$ 8.000,00
2) Transação do tipo PIX com valor maior que R$ 5.000,00

Comportamento esperado:
- Uma transação pode gerar mais de um alerta
- Cada alerta deve conter:
    - transaction_id
    - account_id
    - reason
- O retorno deve conter métricas resumidas e os detalhes dos alertas

"""

transactions = [
    {
        "transaction_id": "tx1001",
        "account_id": "acc42",
        "amount": 9500.00,
        "currency": "BRL",
        "timestamp": "2025-01-10T14:23:55",
        "transaction_type": "PIX"
    }
]


def analyze_transaction(transactions: list[dict]) -> dict:
    suspicious_details = []
    accounts_flagged = []

    suspicious_transactions = 0
    total_transactions = 0

    for transaction in transactions:
        total_transactions += 1

        # Regra 1 — valor alto
        if transaction["amount"] > 8000.00:
            suspicious_transactions += 1
            accounts_flagged.append(transaction["account_id"])
            suspicious_details.append({
                "transaction_id": transaction["transaction_id"],
                "account_id": transaction["account_id"],
                "reason": "AMOUNT > 8000"
            })

        # Regra 2 — PIX de alto valor
        if transaction["transaction_type"] == "PIX" and transaction["amount"] > 5000.00:
            suspicious_transactions += 1
            accounts_flagged.append(transaction["account_id"])
            suspicious_details.append({
                "transaction_id": transaction["transaction_id"],
                "account_id": transaction["account_id"],
                "reason": "PIX > 5000"
            })

    return {
        "total_transactions": total_transactions,
        "suspecious_transactions": suspicious_transactions,
        "accounts_flagged": accounts_flagged,
        "suspicious_details": suspicious_details
    }


result = analyze_transaction(transactions)
print(result)
