from app_py.operations.repositories.expense_repository import get_expenses_data

def get_total_expenses():
    """retorna o total de gastos registrados no banco de dados."""
    df = get_expenses_data()

    if df is None or df.empty:
        return {"erro": "Nenhum gasto encontrado."}, 404

    total_gastos = df['valor'].sum()  # soma todos os valores dos gastos

    return {
        "total_gastos": float(total_gastos)
    }
