import textwrap

def generate_invoice_text_modern(invoice_number: int, client_name: str, total: float, date: str) -> str:
    """
    Format invoice information
    """
    invoice = f"Invoice #{invoice_number}\n"
    invoice += f"Client : {client_name}\n"
    invoice += f"Date : {date}\n"
    invoice += f"Total : {total} BGN"
    return invoice


# EXERCICE AVANCÉ : Formatage de nombres
def format_financial_report(company: str, revenue: float, expenses: float, profit_margin: float) -> str:
    """
    Crée un rapport financier formaté joliment.
    
    Contraintes :
    - Revenue et expenses avec 2 décimales et séparateur milliers
    - Profit margin avec 1 décimale + symbole %
    - Alignement propre
    
    Exemple output:
    ========================================
    FINANCIAL REPORT - ACME Corp
    ========================================
    Revenue:        10,250.50 BGN
    Expenses:        8,100.30 BGN
    Profit Margin:      21.0%
    ========================================
    """
    report = f"="*40 + "\n"
    report += f"FINANCIAL REPORT - {company}\n"
    report += f"="*40 + "\n"
    report += f"Revenue:"
    report += f"{revenue:>16,.2f} BGN\n"
    report += f"Expenses:"
    report += f"{expenses:>15,.2f} BGN\n"
    report += f"Profit Margin:"
    report += f"{profit_margin:>9.1f}%\n"
    report += f"="*40 + "\n"
    return report

# EXERCICE BONUS : Multi-line f-strings
def generate_email_body(recipient: str, invoice_number: int, amount: float, due_date: str) -> str:
    """
    Génère un email de rappel de paiement.
    Utilise des multi-line f-strings avec indentation propre.
    """
    message = f"""\
        Dear {recipient}, 
        
        Please find attached the invoice #{invoice_number}, for the total amount of {amount} BGN.
        We're waiting for the payment until {due_date}.

        Best regards.
        """
    return textwrap.dedent(message)

if __name__ == "__main__":
    # Test 1
    invoice = generate_invoice_text_modern(12345, "Acme Corp", 1250.50, "2025-10-10")
    print(invoice)
    print("\n" + "="*50 + "\n")
    
    # Test 2
    report = format_financial_report("Xerox Bulgaria", 125000.75, 98500.30, 21.2)
    print(report)
    print("\n" + "="*50 + "\n")
    
    # Test 3
    email = generate_email_body("John Doe", 12345, 1250.50, "2025-10-25")
    print(email)