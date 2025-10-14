from typing import List, Dict
import json
import csv

def read_invoices_json(filepath: str) -> List[Dict]:
    """
    Lit un fichier JSON d'invoices.
    Utilise `with open(...) as f:` (context manager)
    """
    # TON CODE ICI
    with open(filepath, "r", encoding='utf-8') as f:
        invoices = json.load(f)
    return invoices


def write_invoices_json(filepath: str, invoices: List[Dict]) -> None:
    """
    Écrit des invoices dans un JSON.
    Formate joliment avec indent=2
    """
    # TON CODE ICI
    with open(filepath, "w", encoding='utf-8') as f:
        json.dump(invoices, f, indent=2, ensure_ascii=False)

# EXERCICE CSV
def export_invoices_to_csv(invoices: List[Dict], output_file: str) -> None:
    """
    Exporte les invoices vers CSV.
    Colonnes : id, client, total, status, due_date
    
    Utilise le module csv avec DictWriter
    """
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'client', 'total', 'status', 'due_date'])
        writer.writeheader()
        writer.writerows(invoices)

def import_invoices_from_csv(input_file: str) -> List[Dict]:
    """
    Importe depuis CSV vers liste de dicts.
    Convertit 'total' en float
    """
    # TON CODE ICI
    invoices = []
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['total'] = float(row['total'])
            invoices.append(row)
    return invoices

# EXERCICE AVANCÉ : Custom context manager
class DatabaseTransaction:
    """
    Un faux context manager pour simuler une transaction DB.
    
    Usage:
        with DatabaseTransaction() as tx:
            tx.execute("INSERT ...")
            tx.execute("UPDATE ...")
        # Auto-commit si pas d'erreur, sinon rollback
    """
    def __init__(self):
        self.queries = []
    
    def __enter__(self):
        """Appelé quand on entre dans le `with`"""
        print("📝 BEGIN TRANSACTION")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Appelé quand on sort du `with`"""
        if exc_type is None:
            # Pas d'erreur
            print(f"✅ COMMIT - {len(self.queries)} queries exécutées")
        else:
            # Il y a eu une erreur
            print(f"❌ ROLLBACK - Erreur: {exc_val}")
        return False  # Ne pas supprimer l'exception
    
    def execute(self, query: str):
        """Simule l'exécution d'une query"""
        print(f"  > {query}")
        self.queries.append(query)

# TON EXERCICE : Utilise ce context manager
def save_invoice_with_items(invoice: Dict, items: List[Dict]) -> None:
    """
    Sauvegarde une invoice + ses items dans une "transaction".
    
    Utilise DatabaseTransaction comme context manager.
    Simule les queries INSERT.
    """
    # TON CODE ICI
    # with DatabaseTransaction() as tx:
    #     tx.execute(f"INSERT INTO invoices ...")
    #     for item in items:
    #         tx.execute(f"INSERT INTO items ...")
    with DatabaseTransaction() as tx:
        tx.execute(f"INSERT INTO invoices (id, client, total) VALUES ('{invoice["id"]}', '{invoice["client"]}', {invoice["total"]}")
        for item in items:
            tx.execute(f"INSERT INTO items (product, quantity, price) VALUES ('{item["product"]}', '{item["qty"]}', '{item["price"]}')")


if __name__ == "__main__":
    # Créer un fichier JSON de test
    test_data = [
        {"id": 1, "client": "Acme", "total": 1500.0, "status": "paid", "due_date": "2025-09-30"},
        {"id": 2, "client": "Beta", "total": 2500.0, "status": "pending", "due_date": "2025-10-15"}
    ]

    # Test 1 : Write JSON
    write_invoices_json("invoices_test.json", test_data)
    print("✅ JSON écrit !")

    # Test 2 : Read JSON
    loaded = read_invoices_json("invoices_test.json")
    print(loaded)
    print(f"✅ JSON lu ! {len(loaded)} invoices")

    # Test 3 : Write CSV
    export_invoices_to_csv(test_data, 'invoices_test.csv')
    print("✅ CSV créé !")

    # Test 4 : Read CSV
    import_csv = import_invoices_from_csv('invoices_test.csv')
    print(import_csv)
    print(f"Le dictionnaire importé contient {len(import_csv)} factures")
    print(f"Total est de type {type(import_csv[0]['total'])}")


    invoice = {"id": 1, "client": "Acme", "total": 1500.0}
    items = [
        {"product": "Widget", "qty": 2, "price": 500.0},
        {"product": "Gadget", "qty": 5, "price": 100.0}
    ]

    # Test 5 : Simuler des requêtes
    save_invoice_with_items(invoice, items)
    
    print("\n" + "="*50)
    print("Test avec erreur (pour voir le ROLLBACK):")
    try:
        with DatabaseTransaction() as tx:
            tx.execute("INSERT INTO test VALUES (1)")
            raise ValueError("Oops, une erreur !")
            tx.execute("Cette query ne sera jamais exécutée")
    except ValueError:
        pass