"""
DESAFIO — RANKING DE VENDAS DE LOJA ONLINE

Contexto:
Você trabalha no time de analytics de uma loja online.
O sistema recebe registros de vendas de produtos feitos pelos vendedores.
Seu objetivo é gerar um ranking simples de performance de cada vendedor.

Cada registro de venda contém:
- seller_id (int)
- product (str)
- quantity (int)
- price (float)
- timestamp (int)

Objetivo:
Implementar uma função que receba uma lista de vendas
e retorne um relatório por vendedor contendo:
- total_sales -> soma do valor de todas as vendas (quantity * price)
- total_items -> soma da quantidade de itens vendidos
- products   -> lista de produtos distintos vendidos

Regras:
1) Ignore registros inválidos:
   - Faltar alguma chave obrigatória
   - quantity ou price <= 0

2) Para cada vendedor (seller_id), consolidar:
   - total_sales
   - total_items
   - produtos distintos

Observações:
- Um vendedor pode não ter vendido nada (será ignorado)
- A ordem dos registros não é garantida
- Use apenas lista e dicionário

--------------------------------
SAÍDA ESPERADA
--------------------------------
{
    1: {"total_sales": 270.0, "total_items": 4, "products": ["camiseta", "calça"]},
    2: {"total_sales": 230.0, "total_items": 5, "products": ["camiseta", "boné"]}
}
"""

sales = [
    {"seller_id": 1, "product": "camiseta", "quantity": 2, "price": 50.0, "timestamp": 10},
    {"seller_id": 1, "product": "calça", "quantity": 1, "price": 120.0, "timestamp": 15},
    {"seller_id": 2, "product": "camiseta", "quantity": 3, "price": 50.0, "timestamp": 20},
    {"seller_id": 2, "product": "boné", "quantity": 2, "price": 40.0, "timestamp": 25},
    {"seller_id": 3, "product": "camiseta", "quantity": 0, "price": 50.0, "timestamp": 30},  # inválido
    {"seller_id": 4, "product": "jaqueta", "quantity": 1, "price": -100.0, "timestamp": 35}, # inválido
    {"seller_id": 1, "product": "camiseta", "quantity": 1, "price": 50.0, "timestamp": 40},
]


def analyze_sales(sales: list[dict]) -> dict:
    expected_fields = {"seller_id", "product", "quantity", "price", "timestamp"}
    result = {}

    for sale in sales:
        if not expected_fields.issubset(sale):
            continue
        
        quantity = sale["quantity"]
        price = sale["price"]

        if quantity <= 0 or price <= 0:
            continue

        seller_id = sale["seller_id"]

        if seller_id not in result:
            result[seller_id] = {
                "total_sales": 0,
                "total_items": 0,
                "products": []
            }


        products = sale["product"]

        if products not in result[seller_id]["products"]:
            result[seller_id]["products"].append(products)

        result[seller_id]["total_items"] += quantity
        result[seller_id]["total_sales"] += quantity*price

    return result

        

# chamada de teste
result = analyze_sales(sales)
print(result)

