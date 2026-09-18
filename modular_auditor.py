TAX_RATE = 0.10


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

def generate_report(total_inventory, rejected_entries):
    print(f"Total inventory: {total_inventory}")
    print(f"Rejected entries: {rejected_entries}")

generate_report(2500, 100)