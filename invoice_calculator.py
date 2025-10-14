def calculate_total(items):
    """Calculate invoice total."""
    return sum(item['price'] * item['qty'] for item in items)
def apply_discount(amount, discount_percent):
    """Apply discount to amount."""
    return amount * (1 - discount_percent / 100)
if __name__ == "__main__":
    items = [{"price": 100, "qty": 2}]
    total = calculate_total(items)
    print(f"Total: {total}")
    discounted = apply_discount(total, 10)
    print(f"With 10% discount: {discounted}")
