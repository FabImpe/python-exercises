from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date, timedelta

# ✅ TON EXERCICE : Crée des dataclasses

@dataclass
class InvoiceItem:
    """
    Un item de facture.
    Champs : product (str), quantity (int), unit_price (float)
    
    Ajoute une property `total` qui calcule quantity * unit_price
    """
    product: str
    quantity: int
    unit_price: float
    
    @property
    def total(self) -> float:
        """Calcule le total de la ligne"""
        return self.quantity * self.unit_price

@dataclass
class Invoice:
    """
    Une facture complète.
    
    Champs:
    - id: int
    - client: str
    - status: str
    - due_date: date (pas str !)
    - items: List[InvoiceItem] avec default_factory
    
    Properties:
    - total: float (somme des items)
    - is_overdue: bool (due_date < aujourd'hui ET status != 'paid')
    """
    id: int
    client: str
    status: str
    due_date: date
    items: List[InvoiceItem] = field(default_factory=list)
    
    @property
    def total(self) -> float:
        """Calcule le total de la facture"""
        return sum(item.total for item in self.items)
        
    
    @property
    def is_overdue(self) -> bool:
        """Check si la facture est en retard"""
        """if self.due_date < date.today() and self.status != 'paid':
            return True
        return False"""
        return self.due_date < date.today() and self.status != 'paid' # Plus propre
        
    
    def add_item(self, product: str, quantity: int, unit_price: float) -> None:
        """Ajoute un item à la facture"""
        item = InvoiceItem(product, quantity, unit_price)
        self.items.append(item)

# EXERCICE AVANCÉ : Méthodes de classe
@dataclass
class Payment:
    """
    Un paiement.
    Champs : invoice_id, amount, payment_date, method
    """
    invoice_id: int
    amount: float
    payment_date: date
    method: str  # "card", "bank_transfer", "cash"
    
    @classmethod
    def from_invoice(cls, invoice: Invoice, method: str = "card") -> "Payment":
        """
        Crée un paiement depuis une invoice.
        Utilise le total de l'invoice et la date d'aujourd'hui.
        
        Usage:
            payment = Payment.from_invoice(my_invoice, "bank_transfer")
        """
        return Payment(invoice.id, invoice.total, date.today(), method)
    
    def is_full_payment(self, invoice: Invoice) -> bool:
        """Vérifie si le paiement couvre la facture complète"""
        """if self.amount < invoice.total:
            return False
        return True"""
        return self.amount >= invoice.total


if __name__ == "__main__":

    # Test 1 : InvoiceItem
    item1 = InvoiceItem("Widget Pro", 2, 500.0)
    print(f"Item total: {item1.total}")

    # Test 2 : Invoice
    invoice = Invoice(
        id=1,
        client="Acme Corp",
        status="pending",
        due_date=date(2025, 10, 15)
    )
    invoice.add_item("Widget Pro", 2, 500.0)
    invoice.add_item("Gadget X", 5, 100.0)
    
    print(f"Invoice total: {invoice.total}")  # 1500.0
    print(f"Nombre d'items: {len(invoice.items)}")  # 2
    
    # Test 3 : is_overdue
    old_invoice = Invoice(
        id=2,
        client="Beta Inc",
        status="pending",
        due_date=date.today() - timedelta(days=10)  # Il y a 10 jours
    )
    print(f"Old invoice overdue: {old_invoice.is_overdue}")  # True
    
    paid_old_invoice = Invoice(
        id=3,
        client="Gamma Ltd",
        status="paid",
        due_date=date.today() - timedelta(days=10)
    )
    print(f"Paid old invoice overdue: {paid_old_invoice.is_overdue}")  # False

    # Test 4 : Payment from invoice
    payment = Payment.from_invoice(invoice, "bank_transfer")
    print(f"Payment amount: {payment.amount}")  # 1500.0
    print(f"Payment method: {payment.method}")  # bank_transfer
    print(f"Is full payment: {payment.is_full_payment(invoice)}")  # True
    
    partial_payment = Payment(
        invoice_id=invoice.id,
        amount=500.0,
        payment_date=date.today(),
        method="card"
    )
    print(f"Partial is full: {partial_payment.is_full_payment(invoice)}")  # False