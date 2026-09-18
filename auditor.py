total_inventory = 0
rejected_entries = 0

while True:
    entry = input("Enter stock quantity (or type 'quit' to finish): ")
    
    if entry.lower() == 'quit':
        break
    if not entry.isdigit():
        if entry.startswith('-') and entry[1:].isdigit():
            print("Invalid entry. Quantity cannot be negative.")
        else:
            print("Invalid entry. Please enter a valid number.")
        rejected_entries += 1
        continue
    quantity = int(entry)
    total_inventory += quantity
    if total_inventory > 500:
        print("Warning: Total inventory exceeds 500 units.")
        break

        
print(f"Total inventory: {total_inventory}")
print(f"Rejected entries: {rejected_entries}")