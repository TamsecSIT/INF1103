TAX_RATE = 0.10

total_inventory = 0
rejected_entries = 0


def calculate_tax(amount):
    return amount * TAX_RATE

def process_delivery(current_total, new_value):
    return current_total + new_value

def get_valid_input():
    user_input = input("Enter stock quantity (or 'quit' to exit): ").strip()
    if user_input.lower() == "quit":
        return "quit"

    try:
        val = int(user_input)
        if val < 0:
            print("Quantity cannot be negative.")
            return None
        return val
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None

def generate_report(total_units, failed_attempts):
    print(f"Total units: {total_units}")
    print(f"Rejected entries: {failed_attempts}")


while True:
    entry = get_valid_input()
    
    if entry == 'quit':
        generate_report(total_inventory, rejected_entries)
        break
    if entry is None:
        rejected_entries += 1
        continue
    if entry is not None:
        total_inventory = process_delivery(total_inventory, entry)
        print(f"Current total units: {total_inventory}")
        print(f"Tax on current total: {calculate_tax(total_inventory)}")


