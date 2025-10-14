from typing import List, Dict

def filter_paid_invoices(invoices: List[Dict]) -> List[Dict]:
    """
    Retourne seulement les factures avec status='paid'
    En UNE LIGNE avec list comprehension
    """
    return [invoice for invoice in invoices if invoice["status"] == 'paid']

def get_invoice_totals(invoices: List[Dict]) -> List[float]:
    """
    Extrait tous les totaux en une ligne
    """
    return [invoice['total'] for invoice in invoices]

# EXERCICE INTERMÉDIAIRE : Transformations # Format "YYYY-MM-DD"
def get_overdue_amounts(invoices: List[Dict], current_date: str) -> List[float]:
    """
    Retourne les montants des factures en retard.
    Une facture est en retard si :
    - status != 'paid'
    - due_date < current_date
    
    En UNE LIGNE avec comprehension + conditions
    
    Exemple invoice:
    {
        "id": 1,
        "total": 1500.0,
        "status": "pending",
        "due_date": "2025-09-30"
    }
    """
    return [invoice['total'] for invoice in invoices if invoice['status'] != 'paid' and invoice['due_date'] < current_date]

# EXERCICE AVANCÉ : Dict comprehensions
def create_invoice_lookup(invoices: List[Dict]) -> Dict[int, Dict]:
    """
    Crée un dictionnaire avec invoice_id comme clé.
    
    Input:  [{"id": 1, "total": 100}, {"id": 2, "total": 200}]
    Output: {1: {"id": 1, "total": 100}, 2: {"id": 2, "total": 200}}
    
    En UNE LIGNE avec dict comprehension
    """
    return {invoice["id"]: invoice for invoice in invoices}

def calculate_client_totals(invoices: List[Dict]) -> Dict[str, float]:
    """
    Calcule le total par client.
    
    Input:  [
        {"client": "Acme", "total": 100},
        {"client": "Acme", "total": 200},
        {"client": "Corp", "total": 150}
    ]
    Output: {"Acme": 300.0, "Corp": 150.0}
    
    ATTENTION : Ici tu NE PEUX PAS faire juste une comprehension.
    Utilise une boucle normale MAIS avec un defaultdict ou dict.get()
    """
    from collections import defaultdict
    # TON CODE ICI
    totals_clients = defaultdict(float)
    for invoice in invoices:
        totals_clients[invoice["client"]] += invoice["total"]
    return dict(totals_clients)

# EXERCICE BONUS : Nested comprehensions
def get_all_line_items(invoices: List[Dict]) -> List[str]:
    """
    Extrait TOUS les noms de produits de TOUTES les factures.
    
    Input: [
        {
            "id": 1,
            "items": [
                {"product": "Widget", "qty": 2},
                {"product": "Gadget", "qty": 1}
            ]
        },
        {
            "id": 2,
            "items": [
                {"product": "Tool", "qty": 3}
            ]
        }
    ]
    Output: ["Widget", "Gadget", "Tool"]
    
    En UNE LIGNE avec nested comprehension
    """
    return [item["product"] for invoice in invoices for item in invoice["items"]]


if __name__ == "__main__":
    # Dataset de test
    invoices = [
        {
            "id": 1,
            "client": "Acme Corp",
            "total": 1500.0,
            "status": "paid",
            "due_date": "2025-09-30",
            "items": [
                {"product": "Widget A", "qty": 2},
                {"product": "Widget B", "qty": 1}
            ]
        },
        {
            "id": 2,
            "client": "Acme Corp",
            "total": 2500.0,
            "status": "pending",
            "due_date": "2025-09-15",
            "items": [
                {"product": "Gadget X", "qty": 5}
            ]
        },
        {
            "id": 3,
            "client": "Beta Inc",
            "total": 800.0,
            "status": "paid",
            "due_date": "2025-10-05",
            "items": [
                {"product": "Tool Z", "qty": 3}
            ]
        },
        {
            "id": 4,
            "client": "Beta Inc",
            "total": 1200.0,
            "status": "pending",
            "due_date": "2025-09-20",
            "items": []
        }
    ]

    # Test 1
    paid = filter_paid_invoices(invoices)
    print(paid)
    print(f"Factures payées : {len(paid)}")

    # Test 2
    totals = get_invoice_totals(invoices)
    print(f"Totaux : {totals}")

    # Test 3
    overdue = get_overdue_amounts(invoices, '2025-10-01')
    print(f"Montants en retard : {overdue}")

    # Test 4
    lookup = create_invoice_lookup(invoices)
    print(f"Invoice #2 {lookup[2]['total']}")

    # Test 5
    client_totals = calculate_client_totals(invoices)
    print(f"Totaux par client : {client_totals}")

    # Test 6
    all_products = get_all_line_items(invoices)
    print(f"Tous les produits : {all_products}")