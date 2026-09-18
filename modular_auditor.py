TAX_RATE = 0.10


def calculate_tax(amount):
    return amount * TAX_RATE

def process_delivery(current_total, new_value):
    return current_total + new_value

print(process_delivery(100, 50))