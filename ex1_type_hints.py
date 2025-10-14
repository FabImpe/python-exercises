from typing import List, Dict, Optional

def calculate_invoice_total_modern(items: List[Dict[str, float]]) -> float:
    """
    Calculate total invoice amount from line items.

    Args:
        items: List of dicts with 'price' and 'quantity' keys

    Returns:
        Total amount

    Example:
        >>> items = [{"price": 10, "quantity": 2}]
        >>> calculate_invoice_total_modern(items)
        20.0
    """
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total

def apply_discount_modern(amount: float, discount_percent: float) -> float:
    """
    Apply a discount to a price.
    :param amount: float - The amount to apply the reduction
    :param discount_percent: float - The percentage for reduction
    """
    return amount - (amount * discount_percent / 100)
    

# Bonus : Crée une fonction qui prend un discount optionnel
def calculate_final_price(base_price: float, discount: Optional[float] = None) -> float:
    """
    If discount is set, return apply_discount_modern
    Else return base_price
    """
    # TON CODE ICI
    if discount:
        return apply_discount_modern(base_price, discount)
    return base_price

if __name__ == "__main__":
    items = [
        {"price": 3.5,"quantity": 2},
        {"price": 4, "quantity": 2.5}
    ]
    
    invoice = calculate_invoice_total_modern(items)
    discount = 50
    invoice_amount = calculate_final_price(invoice)
    invoice_discount = calculate_final_price(invoice, discount)

    print(f"La facture est d'un montant de {invoice_amount} € et la réduction est de {discount} %. Le montant de la facture incluant la réduction est de {invoice_discount} €")