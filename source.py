import json
from datetime import datetime
from tabulate import tabulate

# Sample data structures
inventory = {
    "Gloves": {"quantity": 200, "threshold": 50, "supplier": "MediCorp"},
    "Syringes": {"quantity": 100, "threshold": 30, "supplier": "HealthPlus"},
    "Masks": {"quantity": 80, "threshold": 40, "supplier": "SafeMed"}
}

suppliers = {
    "MediCorp": {"contact": "medicorp@example.com", "phone": "123-456-7890"},
    "HealthPlus": {"contact": "sales@healthplus.com", "phone": "987-654-3210"},
    "SafeMed": {"contact": "support@safemed.com", "phone": "456-789-1230"}
}


def view_inventory():
    table = [[item, data['quantity'], data['threshold'], data['supplier']] for item, data in inventory.items()]
    print(tabulate(table, headers=["Item", "Quantity", "Reorder Threshold", "Supplier"]))


def check_restock():
    print("\nItems that need restocking:")
    for item, data in inventory.items():
        if data['quantity'] < data['threshold']:
            print(f"{item} is below threshold! Contact {data['supplier']}")


def update_inventory(item, quantity):
    if item in inventory:
        inventory[item]['quantity'] += quantity
        print(f"Updated {item} stock to {inventory[item]['quantity']}")
    else:
        print("Item not found.")


def report():
    print("\nGenerating Report...")
    now = datetime.now()
    filename = f"report_{now.strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(inventory, f, indent=4)
    print(f"Report saved as {filename}")


# Main Menu
while True:
    print("\n--- Healthcare Supply Chain Management ---")
    print("1. View Inventory")
    print("2. Check Restock Needs")
    print("3. Update Inventory")
    print("4. Generate Report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_inventory()
    elif choice == "2":
        check_restock()
    elif choice == "3":
        item = input("Enter item name: ")
        qty = int(input("Enter quantity to add: "))
        update_inventory(item, qty)
    elif choice == "4":
        report()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")